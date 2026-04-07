from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages

class AdminSessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only check timeout for admin URLs
        if request.path.startswith('/admin/') and request.user.is_authenticated:
            current_time = timezone.now().timestamp()
            admin_last_activity = request.session.get('admin_last_activity')
            
            if admin_last_activity:
                session_age = current_time - admin_last_activity
                if session_age > 60:  # 1 minute timeout
                    # Clear session and force re-authentication
                    request.session.flush()
                    messages.warning(request, 'Admin session expired. Please log in again.')
                    return redirect('crypto:admin_login')
            
            # Update last activity time for admin pages
            request.session['admin_last_activity'] = current_time
            request.session.modified = True

        response = self.get_response(request)
        return response
