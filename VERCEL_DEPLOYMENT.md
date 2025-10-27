# Vercel Deployment Guide

## Prerequisites
1. Vercel account (free tier available)
2. GitHub repository (optional but recommended)

## Environment Variables Setup
Before deploying, you need to set up environment variables in Vercel:

1. **GEMINI_API_KEY**: Your Google Gemini API key
   - Value: `AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA`

## Deployment Methods

### Method 1: Direct Deployment (Vercel CLI)
1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy from project directory:
   ```bash
   vercel
   ```

4. Follow the prompts:
   - Set up and deploy? **Y**
   - Which scope? Choose your account
   - Link to existing project? **N** (for first deployment)
   - Project name: `employee-attendance-analyzer`
   - In which directory is your code located? `./`

5. Add environment variables:
   ```bash
   vercel env add GEMINI_API_KEY
   ```
   Enter the API key when prompted.

### Method 2: GitHub Integration
1. Push your code to GitHub
2. Connect your GitHub account to Vercel
3. Import the repository
4. Add environment variables in Vercel dashboard
5. Deploy

## Post-Deployment Configuration

### Environment Variables in Vercel Dashboard:
1. Go to your project in Vercel dashboard
2. Navigate to Settings → Environment Variables
3. Add the following:
   - **Name**: `GEMINI_API_KEY`
   - **Value**: `AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA`
   - **Environments**: Production, Preview, Development

### Domain Configuration
- Vercel provides a default domain: `your-project.vercel.app`
- You can add custom domains in Settings → Domains

## Troubleshooting

### Common Issues:
1. **Build fails**: Check Python version in `runtime.txt`
2. **Static files not loading**: Verify `vercel.json` routes configuration
3. **CSV data not found**: File paths should be absolute (already fixed)
4. **Environment variables not working**: Ensure they're set in Vercel dashboard

### File Structure for Deployment:
```
├── app.py                 # Main Flask application (WSGI compatible)
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version specification
├── vercel.json           # Vercel configuration
├── .vercelignore         # Files to ignore during deployment
├── data/
│   └── processed_attendance.csv
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    ├── index.html
    ├── dashboard.html
    ├── employee-view.html
    └── login.html
```

## Performance Optimization
- Static files are served directly by Vercel CDN
- CSV data is loaded efficiently with pandas
- Gemini API calls are optimized with proper error handling

## Security Notes
- API keys are stored as environment variables (not in code)
- Flask app runs in production mode on Vercel
- Debug mode is disabled in production

## Monitoring
- Check Vercel dashboard for deployment logs
- Monitor function execution in Vercel Analytics
- Set up error tracking if needed

## Local Testing Before Deployment
```bash
# Set environment variable
export GEMINI_API_KEY="AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA"

# Run Flask app
python app.py
```

Visit http://localhost:5000 to test locally before deploying.