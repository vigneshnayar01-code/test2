# Flask Employee Attendance Analyzer - Vercel Ready

A professional Flask web application for employee attendance analysis, structured for easy deployment on Vercel.

## 📁 Project Structure

```
website/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment configuration
├── .gitignore               # Git ignore file
├── README_FLASK.md          # This documentation
├── templates/               # HTML templates (Flask standard)
│   ├── index.html          # Home page
│   ├── login.html          # Login page
│   ├── dashboard.html      # Dashboard page
│   ├── employee-view.html  # Employee view page
│   └── organisation-view.html # Organisation view page
└── static/                  # Static files (Flask standard)
    ├── css/
    │   └── styles.css      # Main stylesheet
    └── js/                 # JavaScript files (future use)
```

## 🚀 Local Development

### Prerequisites
- Python 3.7+ installed
- pip package manager

### Setup Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Development Server**
   ```bash
   python app.py
   ```

3. **Access Your Application**
   - Local: `http://localhost:5000`
   - All pages will be available with proper routing

### Available Routes
- **Home**: `/` or `/index.html`
- **Login**: `/login.html`
- **Dashboard**: `/dashboard.html`
- **Employee View**: `/employee-view.html`
- **Organisation View**: `/organisation-view.html`

## 🌐 Vercel Deployment

### Option 1: Vercel CLI (Recommended)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from Project Directory**
   ```bash
   cd "website"
   vercel
   ```

4. **Follow the prompts:**
   - Set up and deploy? **Y**
   - Which scope? Choose your account
   - Link to existing project? **N**
   - Project name: `employee-attendance-analyzer` (or your choice)
   - In which directory? **./  (current directory)**

### Option 2: GitHub + Vercel Dashboard

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Flask Employee Attendance Analyzer"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo.git
   git push -u origin main
   ```

2. **Deploy via Vercel Dashboard**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project
   - Click "Deploy"

### Environment Configuration

Vercel will automatically:
- Detect the Python runtime
- Install dependencies from `requirements.txt`
- Use the `vercel.json` configuration
- Set up proper routing

## 🎯 Features

✅ **Professional Flask Structure** - Follows Flask best practices  
✅ **Vercel Ready** - Configured for seamless deployment  
✅ **Static File Handling** - Proper CSS/JS/image serving  
✅ **Template Engine** - Uses Flask's Jinja2 templating  
✅ **Responsive Design** - Bootstrap-based UI  
✅ **Clean URLs** - SEO-friendly routing  
✅ **Version Control Ready** - Includes .gitignore

## 🔧 Next Steps & Enhancements

### Authentication & Security
- Add user registration/login system
- Implement session management
- Add password hashing with bcrypt
- JWT token authentication for API

### Database Integration
- Connect to PostgreSQL/MySQL database
- User management system
- Attendance data storage
- Analytics and reporting

### API Development
- RESTful API endpoints
- Employee data CRUD operations
- Attendance tracking endpoints
- Data export functionality

### Advanced Features
- Real-time attendance tracking
- Email notifications
- Data visualization with Chart.js
- Employee analytics dashboard
- Export to Excel/PDF reports

## 🛠 Troubleshooting

### Common Issues

**CSS not loading:**
- Check if `static/css/styles.css` exists
- Verify template paths in HTML files

**Templates not found:**
- Ensure HTML files are in `templates/` folder
- Check Flask is using `render_template()`

**Vercel deployment fails:**
- Verify `requirements.txt` has all dependencies
- Check `vercel.json` configuration
- Ensure Python version compatibility

### Support
For issues or questions, check the Flask documentation or Vercel deployment guides.

---
**Ready for Production** 🚀 | **Vercel Optimized** ⚡ | **Flask Powered** 🐍