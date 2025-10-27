#!/bin/bash
# Vercel Deployment Script

echo "🚀 Deploying Employee Attendance Analyzer to Vercel..."

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Login to Vercel (if not already logged in)
echo "🔐 Checking Vercel authentication..."
vercel whoami || vercel login

# Deploy to Vercel
echo "🌐 Deploying to Vercel..."
vercel --prod

echo "✅ Deployment completed!"
echo "📝 Don't forget to set environment variables in Vercel dashboard:"
echo "   - GEMINI_API_KEY: AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA"