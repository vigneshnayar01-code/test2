@echo off
echo 🚀 Employee Attendance Analyzer - Git Setup for Vercel Deployment
echo.

echo 📁 Current directory: %CD%
echo.

echo 🔧 Initializing Git repository...
git init

echo 📝 Creating .gitignore...
(
echo # Python
echo __pycache__/
echo *.pyc
echo *.pyo
echo *.pyd
echo.
echo # Environment variables
echo .env
echo .env.local
echo.
echo # IDE files
echo .vscode/
echo .idea/
echo.
echo # OS files
echo .DS_Store
echo Thumbs.db
echo.
echo # Logs
echo *.log
) > .gitignore

echo ➕ Adding files to Git...
git add .

echo 💾 Creating initial commit...
git commit -m "Initial commit: Employee Attendance Analyzer with Vercel support"

echo.
echo ✅ Git repository setup complete!
echo.
echo 📋 Next Steps:
echo 1. Create a new repository on GitHub.com named 'employee-attendance-analyzer'
echo 2. Run this command (replace YOUR_USERNAME):
echo    git remote add origin https://github.com/YOUR_USERNAME/employee-attendance-analyzer.git
echo 3. Push to GitHub:
echo    git branch -M main
echo    git push -u origin main
echo 4. Go to vercel.com and import your GitHub repository
echo 5. Add environment variable: GEMINI_API_KEY = AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA
echo.
echo 📖 For detailed instructions, see: VERCEL_GIT_DEPLOYMENT.md
echo.
pause