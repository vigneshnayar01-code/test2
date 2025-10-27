#!/usr/bin/env python3
"""
Test script for Gemini API integration
Run this to verify your Gemini API setup is working correctly.
"""

import os
import sys

def test_gemini_integration():
    """Test the Gemini API integration with sample data"""
    
    print("🧪 Testing Gemini API Integration")
    print("=" * 50)
    
    # Check if API key is set
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not found!")
        print("\nTo set it up:")
        print("Windows: set GEMINI_API_KEY=AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA")
        print("Linux/Mac: export GEMINI_API_KEY=AIzaSyBaduO813izLbr48MBYxbCSK8tDQptjfFA")
        return False
    
    print(f"✅ API Key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Import the functions from app.py
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import call_gemini_api, generate_llm_recommendations
    except ImportError as e:
        print(f"❌ Failed to import functions from app.py: {e}")
        return False
    
    # Test data - different employee scenarios
    test_employees = [
        {
            'id': '001',
            'name': 'Sarah Johnson',
            'designation': 'Software Engineer',
            'efficiency': 92,
            'attendance': 96,
            'bayHours': 7.5,
            'clusterType': 'Consistent Performer',
            'punctuality': 94,
            'score': 92,
            'scenario': 'High Performer'
        },
        {
            'id': '002', 
            'name': 'Mike Chen',
            'designation': 'Senior Software Engineer',
            'efficiency': 68,
            'attendance': 78,
            'bayHours': 9.2,
            'clusterType': 'At Risk',
            'punctuality': 75,
            'score': 68,
            'scenario': 'Needs Improvement'
        },
        {
            'id': '003',
            'name': 'Alex Rodriguez',
            'designation': 'Trainee Decision Scientist',
            'efficiency': 85,
            'attendance': 88,
            'bayHours': 6.5,
            'clusterType': 'Late Starter',
            'punctuality': 82,
            'score': 85,
            'scenario': 'Average Performer'
        }
    ]
    
    success_count = 0
    
    for i, employee in enumerate(test_employees, 1):
        print(f"\n🔍 Test {i}: {employee['scenario']}")
        print(f"   Employee: {employee['name']} ({employee['designation']})")
        print(f"   Metrics: {employee['efficiency']}% efficiency, {employee['attendance']}% attendance")
        
        try:
            recommendations = call_gemini_api(employee)
            
            if recommendations:
                print(f"   ✅ Generated {len(recommendations)} recommendations:")
                for j, rec in enumerate(recommendations, 1):
                    priority_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(rec.get('priority', 'low'), '⚪')
                    print(f"      {j}. {priority_emoji} {rec.get('title', 'No title')}")
                    print(f"         {rec.get('description', 'No description')[:80]}...")
                success_count += 1
            else:
                print("   ⚠️ No recommendations generated (API might be down)")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {success_count}/{len(test_employees)} successful")
    
    if success_count == len(test_employees):
        print("🎉 All tests passed! Gemini integration is working perfectly.")
        return True
    elif success_count > 0:
        print("⚠️ Partial success. Some tests worked.")
        return True
    else:
        print("❌ All tests failed. Check your API key and internet connection.")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    print("📦 Checking Dependencies")
    print("-" * 30)
    
    try:
        import requests
        print("✅ requests: Installed")
    except ImportError:
        print("❌ requests: Not installed")
        print("   Install with: pip install requests")
        return False
    
    try:
        import pandas
        print("✅ pandas: Installed")
    except ImportError:
        print("❌ pandas: Not installed")
        return False
    
    return True

if __name__ == "__main__":
    print("🚀 Gemini API Integration Test Suite")
    print("🤖 Testing AI-powered employee recommendations\n")
    
    if not check_dependencies():
        print("\n❌ Missing dependencies. Please install required packages.")
        sys.exit(1)
    
    if test_gemini_integration():
        print("\n✅ Setup complete! Your Gemini integration is ready to use.")
        print("🌟 Start your Flask app with: python app.py")
    else:
        print("\n❌ Setup needs attention. Please check the error messages above.")
        sys.exit(1)