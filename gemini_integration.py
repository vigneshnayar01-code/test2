"""
Gemini API Integration for Employee Recommendations
This file contains the complete implementation for integrating Google Gemini API
"""

import google.generativeai as genai
import json
import re
from typing import List, Dict, Any, Optional

class GeminiRecommendationEngine:
    def __init__(self, api_key: str):
        """
        Initialize the Gemini API client
        
        Args:
            api_key (str): Your Google Gemini API key
        """
        self.api_key = api_key
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def generate_employee_recommendations(self, employee_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Generate personalized recommendations for an employee using Gemini API
        
        Args:
            employee_data (dict): Employee data including performance metrics
            
        Returns:
            List[Dict]: List of recommendation objects with title, description, priority, and icon
        """
        try:
            prompt = self._create_recommendation_prompt(employee_data)
            response = self.model.generate_content(prompt)
            recommendations = self._parse_gemini_response(response.text)
            return recommendations
        except Exception as e:
            print(f"Error generating Gemini recommendations: {e}")
            return self._fallback_recommendations(employee_data)
    
    def _create_recommendation_prompt(self, employee_data: Dict[str, Any]) -> str:
        """Create a structured prompt for Gemini API"""
        
        # Calculate risk level
        risk_level = self._calculate_risk_level(employee_data)
        
        prompt = f"""
You are an AI HR consultant analyzing employee performance data. Generate 4 personalized, actionable recommendations.

EMPLOYEE PROFILE:
- Name: {employee_data.get('name', 'Unknown')}
- Designation: {employee_data.get('designation', 'N/A')}
- Efficiency: {employee_data.get('efficiency', 0)}%
- Attendance: {employee_data.get('attendance', 0)}%
- Bay Hours: {employee_data.get('bayHours', 0)} hours/day
- Behavior Type: {employee_data.get('clusterType', 'Unknown')}
- Risk Level: {risk_level}

CONTEXT ANALYSIS:
- If efficiency < 70%: Focus on skill development and training
- If attendance < 85%: Address attendance issues and support needs
- If bayHours > 9: Work-life balance and burnout prevention
- If bayHours < 6: Engagement and collaboration improvement

REQUIREMENTS:
1. Generate exactly 4 recommendations
2. Make them specific to this employee's data
3. Include actionable steps
4. Vary priority levels (high, medium, low)
5. Choose appropriate FontAwesome icons

Return ONLY a valid JSON array in this exact format:
[
  {{
    "icon": "fas fa-chart-line",
    "title": "Performance Enhancement",
    "description": "Specific actionable recommendation based on employee data",
    "priority": "high"
  }},
  {{
    "icon": "fas fa-calendar-check",
    "title": "Another Recommendation",
    "description": "Another specific recommendation",
    "priority": "medium"
  }}
]

AVAILABLE ICONS: fa-chart-line, fa-calendar-check, fa-user-clock, fa-building, fa-balance-scale, fa-trophy, fa-target, fa-users, fa-clock, fa-life-ring, fa-star, fa-graduation-cap, fa-book, fa-lightbulb, fa-heart, fa-cog

Focus on: Performance improvement, Work-life balance, Career development, Team collaboration, Health & wellness.
"""
        return prompt
    
    def _calculate_risk_level(self, employee_data: Dict[str, Any]) -> str:
        """Calculate employee risk level based on metrics"""
        efficiency = employee_data.get('efficiency', 0)
        attendance = employee_data.get('attendance', 0)
        
        if efficiency < 60 or attendance < 75:
            return "High Risk"
        elif efficiency < 80 or attendance < 90:
            return "Medium Risk"
        else:
            return "Low Risk"
    
    def _parse_gemini_response(self, response_text: str) -> List[Dict[str, Any]]:
        """Parse Gemini API response and extract recommendations"""
        try:
            # Clean the response text
            cleaned_text = response_text.strip()
            
            # Try to extract JSON from the response
            json_match = re.search(r'\[.*\]', cleaned_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                recommendations = json.loads(json_str)
                
                # Validate and clean recommendations
                valid_recommendations = []
                for rec in recommendations:
                    if self._validate_recommendation(rec):
                        valid_recommendations.append(rec)
                
                return valid_recommendations[:4]  # Limit to 4 recommendations
            
        except (json.JSONDecodeError, AttributeError) as e:
            print(f"Error parsing Gemini response: {e}")
        
        # If parsing fails, return empty list to trigger fallback
        return []
    
    def _validate_recommendation(self, recommendation: Dict[str, Any]) -> bool:
        """Validate that a recommendation has required fields"""
        required_fields = ['icon', 'title', 'description', 'priority']
        return all(field in recommendation and recommendation[field] for field in required_fields)
    
    def _fallback_recommendations(self, employee_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate fallback recommendations if Gemini API fails"""
        efficiency = employee_data.get('efficiency', 0)
        attendance = employee_data.get('attendance', 0)
        bay_hours = employee_data.get('bayHours', 8)
        
        recommendations = []
        
        # Efficiency-based recommendations
        if efficiency < 70:
            recommendations.append({
                "icon": "fas fa-chart-line",
                "title": "Performance Enhancement",
                "description": f"Current efficiency is {efficiency}%. Consider skills training and workflow optimization.",
                "priority": "high"
            })
        elif efficiency < 85:
            recommendations.append({
                "icon": "fas fa-target",
                "title": "Performance Optimization",
                "description": f"Good efficiency at {efficiency}%. Focus on advanced productivity techniques.",
                "priority": "medium"
            })
        
        # Attendance-based recommendations
        if attendance < 85:
            recommendations.append({
                "icon": "fas fa-calendar-check",
                "title": "Attendance Improvement",
                "description": f"Attendance at {attendance}% needs attention. Consider flexible scheduling.",
                "priority": "high"
            })
        
        # Work hours recommendations
        if bay_hours > 9:
            recommendations.append({
                "icon": "fas fa-balance-scale",
                "title": "Work-Life Balance",
                "description": f"High office hours ({bay_hours}hrs). Focus on time management to prevent burnout.",
                "priority": "high"
            })
        elif bay_hours < 6:
            recommendations.append({
                "icon": "fas fa-building",
                "title": "Office Engagement",
                "description": f"Low office hours ({bay_hours}hrs). Consider increasing collaborative work time.",
                "priority": "medium"
            })
        
        # Default recommendation if none above apply
        if not recommendations:
            recommendations.append({
                "icon": "fas fa-star",
                "title": "Continuous Improvement",
                "description": "Maintain excellent performance and explore leadership opportunities.",
                "priority": "low"
            })
        
        return recommendations[:4]


# Usage example and integration functions
def setup_gemini_api(api_key: str) -> GeminiRecommendationEngine:
    """
    Setup Gemini API client
    
    Args:
        api_key (str): Your Google Gemini API key
        
    Returns:
        GeminiRecommendationEngine: Configured API client
    """
    return GeminiRecommendationEngine(api_key)


def get_employee_recommendations(employee_data: Dict[str, Any], api_key: str) -> List[Dict[str, Any]]:
    """
    Main function to get employee recommendations
    
    Args:
        employee_data (dict): Employee performance data
        api_key (str): Gemini API key
        
    Returns:
        List[Dict]: List of recommendations
    """
    try:
        gemini_engine = setup_gemini_api(api_key)
        return gemini_engine.generate_employee_recommendations(employee_data)
    except Exception as e:
        print(f"Error in Gemini integration: {e}")
        # Return fallback recommendations
        engine = GeminiRecommendationEngine("")  # Empty key for fallback
        return engine._fallback_recommendations(employee_data)


# Example usage:
if __name__ == "__main__":
    # Example employee data
    sample_employee = {
        'id': '123',
        'name': 'John Doe',
        'designation': 'Software Engineer',
        'efficiency': 75,
        'attendance': 88,
        'bayHours': 8.5,
        'clusterType': 'Consistent Performer'
    }
    
    # Your API key (replace with actual key)
    API_KEY = "YOUR_GEMINI_API_KEY_HERE"
    
    # Generate recommendations
    recommendations = get_employee_recommendations(sample_employee, API_KEY)
    
    # Print results
    print("Generated Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['title']} ({rec['priority']} priority)")
        print(f"   {rec['description']}")
        print(f"   Icon: {rec['icon']}\n")