#!/usr/bin/env python3
"""Check Google API quota and project configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

def check_quota_status():
    """Check API quota and configuration."""
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        print("❌ No API key found")
        return
    
    print("=" * 70)
    print("Google API Quota & Configuration Check")
    print("=" * 70)
    print(f"\n🔑 API Key: {api_key[:20]}...{api_key[-4:]}")
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        print("\n📊 Testing API with different models...\n")
        
        test_models = [
            "gemini-2.5-flash",
            "gemini-2.5-pro", 
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ]
        
        for model_name in test_models:
            try:
                print(f"Testing {model_name}...", end=" ")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    "Reply with just 'OK'",
                    generation_config=genai.GenerationConfig(
                        max_output_tokens=10,
                    )
                )
                print(f"✅ SUCCESS - Response: {response.text.strip()}")
            except Exception as e:
                error_msg = str(e)
                if "quota" in error_msg.lower() or "429" in error_msg:
                    print(f"❌ QUOTA EXCEEDED")
                    print(f"   Error: {error_msg[:100]}")
                elif "not found" in error_msg.lower() or "404" in error_msg:
                    print(f"⚠️  Model not available")
                else:
                    print(f"❌ ERROR: {error_msg[:80]}")
        
        print("\n" + "=" * 70)
        print("💡 TROUBLESHOOTING QUOTA ISSUES:")
        print("=" * 70)
        print("""
1. **Check your Google Cloud Console:**
   https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas
   
2. **Verify billing is enabled:**
   https://console.cloud.google.com/billing
   
3. **Common causes of quota errors:**
   - API key is from a FREE tier project (not paid)
   - Billing account not linked to the API project
   - Quota limits set too low in Cloud Console
   - Using experimental models with stricter limits
   
4. **Check which project your API key belongs to:**
   - Go to: https://console.cloud.google.com/apis/credentials
   - Find your API key and check the project name
   - Verify that project has billing enabled
   
5. **Rate limits even on paid tiers:**
   - Tier 1 has limits: ~15 RPM for some models
   - If you're making rapid requests, add delays
   
6. **Try creating a NEW API key:**
   - Sometimes keys get stuck in free tier
   - Create new key in a project with billing enabled
   - https://aistudio.google.com/app/apikey
        """)
        
    except ImportError:
        print("❌ google-generativeai not installed")
        print("   Run: pip install google-generativeai")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    check_quota_status()
