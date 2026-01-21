#!/usr/bin/env python3
"""Test script to verify Google API key connectivity and tier status."""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

def test_google_api():
    """Test Google Gemini API connection."""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ ERROR: GOOGLE_API_KEY not found in environment")
        return False
    
    print(f"✓ API Key found: {api_key[:20]}...")
    
    try:
        import google.generativeai as genai
        print("✓ google-generativeai library imported successfully")
    except ImportError:
        print("❌ ERROR: google-generativeai library not installed")
        print("   Run: pip install google-generativeai")
        return False
    
    try:
        # Configure the API
        genai.configure(api_key=api_key)
        print("✓ API configured")
        
        # List available models to verify connection
        print("\n📋 Testing API connection by listing models...")
        models = genai.list_models()
        
        available_models = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
        
        if available_models:
            print(f"✅ SUCCESS! API key is working. Found {len(available_models)} available models:")
            for model_name in available_models[:5]:  # Show first 5
                print(f"   - {model_name}")
            
            # Test a simple generation
            print("\n🧪 Testing content generation...")
            model = genai.GenerativeModel('gemini-2.0-flash')
            response = model.generate_content("Say 'API test successful' if you can read this.")
            print(f"✅ Generation test successful!")
            print(f"   Response: {response.text[:100]}")
            
            return True
        else:
            print("⚠️  WARNING: API connected but no models available for content generation")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: API connection failed")
        print(f"   Error type: {type(e).__name__}")
        print(f"   Error message: {str(e)}")
        
        # Check for common error types
        error_str = str(e).lower()
        if "api key not valid" in error_str or "invalid" in error_str:
            print("\n💡 Possible causes:")
            print("   1. API key is incorrect or has been revoked")
            print("   2. API key doesn't have Gemini API enabled")
            print("   3. Go to: https://makersuite.google.com/app/apikey")
        elif "quota" in error_str or "limit" in error_str:
            print("\n💡 Possible causes:")
            print("   1. API quota exceeded (even paid tiers have limits)")
            print("   2. Billing not properly set up")
            print("   3. Check: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
        elif "permission" in error_str or "403" in error_str:
            print("\n💡 Possible causes:")
            print("   1. Generative Language API not enabled in your project")
            print("   2. Enable it at: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com")
        
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("Google Gemini API Key Test")
    print("=" * 60)
    
    success = test_google_api()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests passed! Your API key is working correctly.")
    else:
        print("❌ Tests failed. Please check the errors above.")
    print("=" * 60)
    
    sys.exit(0 if success else 1)
