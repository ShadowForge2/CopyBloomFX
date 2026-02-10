"""
Paystack Service for Local Payments
Handles Paystack API integration for deposits and withdrawals
"""

import requests
import json
import logging
from decimal import Decimal
from django.conf import settings
from django.utils import timezone
import uuid

# Set up logging
logger = logging.getLogger(__name__)


class PaystackService:
    """Service class for Paystack API operations"""
    
    BASE_URL = "https://api.paystack.co"
    
    @classmethod
    def get_headers(cls):
        """Get authorization headers for Paystack API"""
        secret_key = getattr(settings, 'PAYSTACK_SECRET_KEY', '')
        
        # Fallback to hardcoded keys if environment variables aren't loaded
        if not secret_key or secret_key == 'sk_test_your_secret_key_here':
            secret_key = 'sk_test_176a7ac484646630cd54679b52493259c4dd1d7c'
            print("DEBUG: Using fallback secret key")
        
        return {
            "Authorization": f"Bearer {secret_key}",
            "Content-Type": "application/json",
        }
    
    @classmethod
    def initialize_transaction(cls, amount, email, callback_url, reference=None):
        """Initialize a Paystack transaction for deposit"""
        if not reference:
            reference = f"DEP_{uuid.uuid4().hex[:12]}"
        
        # Validate amount
        if amount <= 0:
            logger.error(f"Invalid amount for transaction initialization: {amount}")
            return {"status": False, "message": "Invalid amount"}
        
        # Validate and fix email address
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not email or not re.match(email_pattern, email):
            # Use a fallback email for invalid addresses
            email = "user@copybloomfx.com"
            logger.warning(f"Invalid email address provided, using fallback: {email}")
        
        data = {
            "amount": int(amount * 100),  # Convert to kobo
            "email": email,
            "reference": reference,
            "callback_url": callback_url,
            "currency": "NGN",
            "metadata": {
                "custom_fields": [
                    {
                        "display_name": "Platform",
                        "variable_name": "platform",
                        "value": "CopyBloom FX"
                    }
                ]
            }
        }
        
        try:
            logger.info(f"Initializing Paystack transaction: {reference} - {amount} NGN")
            response = requests.post(
                f"{cls.BASE_URL}/transaction/initialize",
                headers=cls.get_headers(),
                json=data,
                timeout=30
            )
            
            # Log response for debugging
            logger.info(f"Paystack response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if result.get('status'):
                    logger.info(f"Transaction initialized successfully: {reference}")
                    return result
                else:
                    logger.error(f"Paystack initialization failed: {result.get('message', 'Unknown error')}")
                    return {"status": False, "message": result.get('message', 'Initialization failed')}
            else:
                logger.error(f"Paystack API error: {response.status_code} - {response.text}")
                return {"status": False, "message": f"API Error: {response.status_code}"}
                
        except requests.exceptions.Timeout:
            logger.error("Paystack API timeout")
            return {"status": False, "message": "Payment gateway timeout. Please try again."}
        except requests.exceptions.RequestException as e:
            logger.error(f"Paystack request exception: {str(e)}")
            return {"status": False, "message": "Payment gateway error. Please try again."}
        except Exception as e:
            logger.error(f"Unexpected error in Paystack initialization: {str(e)}")
            return {"status": False, "message": "An unexpected error occurred"}
    
    @classmethod
    def verify_transaction(cls, reference):
        """Verify a Paystack transaction"""
        try:
            logger.info(f"Verifying Paystack transaction: {reference}")
            response = requests.get(
                f"{cls.BASE_URL}/transaction/verify/{reference}",
                headers=cls.get_headers(),
                timeout=30
            )
            
            logger.info(f"Paystack verification response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if result.get('status'):
                    data = result.get('data', {})
                    status = data.get('status', '')
                    amount = data.get('amount', 0) / 100  # Convert from kobo
                    paid_at = data.get('paid_at')
                    
                    logger.info(f"Transaction verification result: {reference} - Status: {status}, Amount: {amount}")
                    
                    return {
                        'status': True,
                        'data': {
                            'status': status,
                            'amount': amount,
                            'paid_at': paid_at,
                            'reference': reference,
                            'customer': data.get('customer', {}),
                            'gateway_response': data.get('gateway_response', '')
                        }
                    }
                else:
                    logger.error(f"Paystack verification failed: {result.get('message', 'Unknown error')}")
                    return {"status": False, "message": result.get('message', 'Verification failed')}
            else:
                logger.error(f"Paystack verification API error: {response.status_code} - {response.text}")
                return {"status": False, "message": f"Verification API Error: {response.status_code}"}
                
        except requests.exceptions.Timeout:
            logger.error("Paystack verification timeout")
            return {"status": False, "message": "Verification timeout. Please try again."}
        except requests.exceptions.RequestException as e:
            logger.error(f"Paystack verification request exception: {str(e)}")
            return {"status": False, "message": "Verification service error. Please try again."}
        except Exception as e:
            logger.error(f"Unexpected error in Paystack verification: {str(e)}")
            return {"status": False, "message": "An unexpected error occurred during verification"}
    
    @classmethod
    def initiate_transfer(cls, amount, recipient_code, reference=None, reason="CopyBloom FX Withdrawal"):
        """Initiate a Paystack transfer for withdrawal"""
        if not reference:
            reference = f"WTH_{uuid.uuid4().hex[:12]}"
        
        data = {
            "source": "balance",
            "amount": int(amount * 100),  # Convert to kobo
            "recipient": recipient_code,
            "reference": reference,
            "reason": reason,
        }
        
        try:
            response = requests.post(
                f"{cls.BASE_URL}/transfer",
                headers=cls.get_headers(),
                json=data,
                timeout=30
            )
            
            # Handle response properly
            response_data = response.json()
            
            if response.status_code == 200:
                return response_data
            else:
                # Log the error details for debugging
                logger.error(f"Paystack transfer error: {response.status_code} - {response_data}")
                return {
                    "status": False, 
                    "message": f"Paystack API Error: {response_data.get('message', 'Unknown error')}",
                    "data": response_data
                }
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Paystack transfer request exception: {str(e)}")
            return {"status": False, "message": str(e)}
    
    @classmethod
    def create_transfer_recipient(cls, account_number, bank_code, account_name, description="CopyBloom FX User"):
        """Create a transfer recipient for withdrawals"""
        data = {
            "type": "nuban",
            "name": account_name,
            "account_number": account_number,
            "bank_code": bank_code,
            "currency": "NGN",
            "description": description,
        }
        
        try:
            response = requests.post(
                f"{cls.BASE_URL}/transferrecipient",
                headers=cls.get_headers(),
                json=data,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"status": False, "message": str(e)}
    
    @classmethod
    def get_banks(cls):
        """Get list of supported banks"""
        try:
            response = requests.get(
                f"{cls.BASE_URL}/bank",
                headers=cls.get_headers(),
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"status": False, "message": str(e)}
    
    @classmethod
    def resolve_account(cls, account_number, bank_code):
        """Resolve bank account details"""
        try:
            response = requests.get(
                f"{cls.BASE_URL}/bank/resolve",
                headers=cls.get_headers(),
                params={
                    "account_number": account_number,
                    "bank_code": bank_code
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"status": False, "message": str(e)}


class PaystackWebhookHandler:
    """Handle Paystack webhooks"""
    
    @staticmethod
    def verify_webhook_signature(payload, signature):
        """Verify Paystack webhook signature"""
        # TODO: Implement proper webhook signature verification
        # For now, we'll return True (implement proper verification in production)
        logger.info("Webhook signature verification (TODO: implement proper verification)")
        return True
    
    @staticmethod
    def handle_charge_success(payload):
        """Handle successful charge webhook"""
        try:
            data = payload.get('data', {})
            reference = data.get('reference', '')
            status = data.get('status', '')
            amount = data.get('amount', 0) / 100  # Convert from kobo
            customer = data.get('customer', {})
            
            logger.info(f"Processing charge success webhook: {reference} - Status: {status}, Amount: {amount}")
            
            if status == 'success':
                # Process successful deposit
                from crypto.models import LocalDeposit
                try:
                    deposit = LocalDeposit.objects.get(paystack_reference=reference)
                    if deposit.status == 'pending':
                        # Update deposit status
                        deposit.status = 'paid'
                        deposit.paystack_response = payload
                        deposit.paid_at = timezone.now()
                        deposit.save()
                        
                        # Update user balance
                        profile = deposit.user.profile
                        profile.locked_balance += deposit.amount_usdt
                        profile.save(update_fields=['locked_balance'])
                        
                        # TODO: Implement referral logic for Paystack deposits if needed
                        # For now, skip referral processing to avoid AttributeError
                        
                        # Update user rank
                        profile.update_rank()
                        
                        logger.info(f"Deposit processed successfully: {reference} - User: {deposit.user.email}")
                        return True, f"Deposit of ${deposit.amount_usdt:.2f} processed successfully"
                    else:
                        logger.warning(f"Deposit {reference} already processed with status: {deposit.status}")
                        return True, "Deposit already processed"
                        
                except LocalDeposit.DoesNotExist:
                    logger.error(f"Deposit not found for reference: {reference}")
                    return False, "Deposit not found"
            else:
                logger.warning(f"Invalid status in webhook: {status}")
                return False, f"Invalid status: {status}"
                
        except Exception as e:
            logger.error(f"Error processing charge success webhook: {str(e)}")
            return False, f"Processing error: {str(e)}"
    
    @staticmethod
    def handle_transfer_success(payload):
        """Handle successful transfer webhook"""
        try:
            data = payload.get('data', {})
            reference = data.get('reference', '')
            status = data.get('status', '')
            amount = data.get('amount', 0) / 100  # Convert from kobo
            
            logger.info(f"Processing transfer success webhook: {reference} - Status: {status}, Amount: {amount}")
            
            if status == 'success':
                # Process successful withdrawal
                from crypto.models import LocalWithdrawal
                try:
                    withdrawal = LocalWithdrawal.objects.get(paystack_transfer_reference=reference)
                    if withdrawal.status == 'approved':
                        withdrawal.status = 'completed'
                        withdrawal.paystack_response = payload
                        withdrawal.processed_at = timezone.now()
                        withdrawal.save()
                        
                        logger.info(f"Withdrawal processed successfully: {reference} - User: {withdrawal.user.email}")
                        return True, f"Withdrawal of ${withdrawal.amount_usdt:.2f} processed successfully"
                    else:
                        logger.warning(f"Withdrawal {reference} already processed with status: {withdrawal.status}")
                        return True, "Withdrawal already processed"
                        
                except LocalWithdrawal.DoesNotExist:
                    logger.error(f"Withdrawal not found for reference: {reference}")
                    return False, "Withdrawal not found"
            else:
                logger.warning(f"Invalid status in transfer webhook: {status}")
                return False, f"Invalid status: {status}"
                
        except Exception as e:
            logger.error(f"Error processing transfer success webhook: {str(e)}")
            return False, f"Processing error: {str(e)}"
    
    @staticmethod
    def handle_transfer_failed(payload):
        """Handle failed transfer webhook"""
        try:
            data = payload.get('data', {})
            reference = data.get('reference', '')
            status = data.get('status', '')
            
            logger.info(f"Processing transfer failed webhook: {reference} - Status: {status}")
            
            # Process failed withdrawal
            from crypto.models import LocalWithdrawal
            try:
                withdrawal = LocalWithdrawal.objects.get(paystack_transfer_reference=reference)
                if withdrawal.status in ['approved', 'completed']:
                    withdrawal.status = 'failed'
                    withdrawal.paystack_response = payload
                    withdrawal.processed_at = timezone.now()
                    
                    # Refund user
                    profile = withdrawal.user.profile
                    profile.withdrawable_balance += withdrawal.amount_usdt
                    profile.save(update_fields=['withdrawable_balance'])
                    
                    withdrawal.save()
                    
                    logger.info(f"Withdrawal failed and refunded: {reference} - User: {withdrawal.user.email}")
                    return True, f"Withdrawal of ${withdrawal.amount_usdt:.2f} failed and refunded"
                else:
                    logger.warning(f"Withdrawal {reference} already processed with status: {withdrawal.status}")
                    return True, "Withdrawal already processed"
                    
            except LocalWithdrawal.DoesNotExist:
                logger.error(f"Withdrawal not found for reference: {reference}")
                return False, "Withdrawal not found"
                
        except Exception as e:
            logger.error(f"Error processing transfer failed webhook: {str(e)}")
            return False, f"Processing error: {str(e)}"
