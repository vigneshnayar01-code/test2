# PowerShell script to set up Gemini API and start the application
Write-Host "Setting up Gemini API Environment Variable..." -ForegroundColor Green
Write-Host ""

# Set the Gemini API key as an environment variable
$env:GEMINI_API_KEY = "AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA"

Write-Host "✅ Environment variable set successfully!" -ForegroundColor Green
Write-Host "GEMINI_API_KEY is now configured for this session." -ForegroundColor Yellow
Write-Host ""

Write-Host "Starting Flask application..." -ForegroundColor Green
Write-Host ""

# Start the Flask app
python app.py