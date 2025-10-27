@echo off
echo Setting up Gemini API Environment Variable...
echo.

REM Set the Gemini API key as an environment variable
set GEMINI_API_KEY=AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA

echo ✅ Environment variable set successfully!
echo GEMINI_API_KEY is now configured for this session.
echo.

echo Starting Flask application...
echo.

REM Start the Flask app
python app.py

pause