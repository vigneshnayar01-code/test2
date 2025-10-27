# Gemini API Integration Setup Guide

This guide will help you set up Google Gemini API integration for AI-powered employee recommendations using REST API calls.

## Quick Start

**The API key is already included in the project for testing purposes.**

### Option 1: Use the Provided Batch Files (Easiest)

#### Windows Command Prompt:
```cmd
start_with_gemini.bat
```

#### Windows PowerShell:
```powershell
.\start_with_gemini.ps1
```

### Option 2: Manual Setup

#### Windows (Command Prompt):
```cmd
set GEMINI_API_KEY=AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA
python app.py
```

#### Windows (PowerShell):
```powershell
$env:GEMINI_API_KEY="AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA"
python app.py
```

#### Linux/Mac:
```bash
export GEMINI_API_KEY="AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA"
python app.py
```

## Prerequisites

1. **Python Dependencies**: Install required packages
2. **Internet Connection**: For API calls to Google Gemini

## Step-by-Step Setup

### 1. Install Dependencies

```bash
pip install requests pandas flask
```

Or install all project dependencies:
```bash
pip install -r requirements.txt
```

### 2. API Key (Already Provided)

The API key `AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA` is already integrated into the project for immediate testing.

For production use, you should:
1. Go to [Google AI Studio](https://aistudio.google.com)
2. Sign in with your Google account
3. Click "Get API key" in the left sidebar
4. Create a new API key
5. Replace the existing key in the environment setup

#### Permanent Setup (recommended):
Create a `.env` file in your project root:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Test the Integration

Run this test script to verify everything works:

```python
from gemini_integration import get_employee_recommendations
import os

# Test employee data
test_employee = {
    'id': '123',
    'name': 'John Doe',
    'designation': 'Software Engineer',
    'efficiency': 75,
    'attendance': 88,
    'bayHours': 8.5,
    'clusterType': 'Consistent Performer'
}

# Get your API key
api_key = os.getenv('GEMINI_API_KEY')

if api_key:
    recommendations = get_employee_recommendations(test_employee, api_key)
    print(f"Generated {len(recommendations)} recommendations!")
    for rec in recommendations:
        print(f"- {rec['title']}: {rec['description']}")
else:
    print("Please set GEMINI_API_KEY environment variable")
```

### 5. Start the Application

```bash
python app.py
```

Now when you view an employee profile, the system will:
1. Try to get AI recommendations from Gemini API
2. Fall back to intelligent rule-based recommendations if API fails
3. Display personalized, actionable suggestions

## Features

### AI-Powered Recommendations
- **Personalized Analysis**: Each recommendation is tailored to the specific employee's performance data
- **Actionable Insights**: Specific steps the employee can take to improve
- **Priority Levels**: High, medium, and low priority recommendations
- **Icon Integration**: FontAwesome icons for better visual presentation

### Fallback System
- **Reliable Operation**: Works even if Gemini API is unavailable
- **Intelligent Rules**: Rule-based system provides meaningful recommendations
- **Seamless Experience**: Users don't notice when fallback is used

### Data Integration
- **Real CSV Data**: Uses actual employee performance metrics
- **Risk Assessment**: Analyzes attendance, efficiency, and work patterns
- **Behavioral Clusters**: Considers employee behavior types
- **Comprehensive Metrics**: Bay hours, attendance, efficiency, and more

## API Usage Limits

- **Free Tier**: 60 requests per minute
- **Rate Limiting**: Built-in handling for API limits
- **Cost**: Check current pricing at [ai.google.dev/pricing](https://ai.google.dev/pricing)

## Troubleshooting

### Common Issues

1. **"Module not found" error**:
   ```bash
   pip install google-generativeai
   ```

2. **"API key not found"**:
   - Verify environment variable is set
   - Check API key is valid
   - Restart your terminal/IDE

3. **"API quota exceeded"**:
   - Wait for quota reset
   - Check your usage in Google AI Studio
   - Consider upgrading your plan

4. **"Invalid response format"**:
   - The system automatically falls back to rule-based recommendations
   - Check console logs for details

### Debug Mode

Enable debug logging by adding this to your app.py:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Security Best Practices

1. **Never commit API keys** to version control
2. **Use environment variables** for sensitive data
3. **Rotate API keys** regularly
4. **Monitor API usage** in Google AI Studio
5. **Set up usage alerts** to avoid unexpected charges

## Example Output

When working correctly, you'll see recommendations like:

```json
[
  {
    "icon": "fas fa-chart-line",
    "title": "Performance Optimization",
    "description": "Your efficiency at 75% shows room for improvement. Consider time-blocking techniques and workflow automation tools.",
    "priority": "medium"
  },
  {
    "icon": "fas fa-balance-scale",
    "title": "Work-Life Balance",
    "description": "With 8.5 daily bay hours, focus on efficient task completion to maintain healthy work boundaries.",
    "priority": "high"
  }
]
```

## Support

If you encounter issues:
1. Check the console logs for error messages
2. Verify your API key is valid
3. Test with the provided example code
4. Review Google AI Studio documentation

The system is designed to work reliably with or without Gemini API, so your application will continue functioning even if there are API issues.