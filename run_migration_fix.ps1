# Database Migration Fix Script
Write-Host "🚀 Starting Database Migration Fix..." -ForegroundColor Green
Write-Host ""

# Run the migration fix script
try {
    python fix_migrations.py
    Write-Host ""
    Write-Host "🎉 Migration fix completed!" -ForegroundColor Green
} catch {
    Write-Host "❌ Migration fix failed:" -ForegroundColor Red
    Write-Host $_.Exception.Message
}

Write-Host ""
Write-Host "Press any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
