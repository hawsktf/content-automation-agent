#!/usr/bin/env python3
"""Test the second API key."""

import os
import sys

def test_api_key(api_key):
    """Test Google Gemini API connection with provided key."""
    
    print("=" * 70)
    print("Testing Second API Key")
    print("=" * 70)
    print(f"\n🔑 API Key: {api_key[:20]}...{api_key[-4:]}")
    
    try:
        import google.generativeai as genai
        print("✓ Library imported")
    except ImportError:
        print("❌ google-generativeai not installed")
        return False
    
    try:
        genai.configure(api_key=api_key)
        print("✓ API configured")
        
        # List available models
        print("\n📋 Listing available models...")
        models = genai.list_models()
        
        available_models = []
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                available_models.append(model.name)
        
        if available_models:
            print(f"✅ Found {len(available_models)} models")
            for model_name in available_models[:5]:
                print(f"   - {model_name}")
        else:
            print("⚠️  No models available")
            return False
        
        # Test generation with multiple models
        print("\n🧪 Testing content generation...\n")
        
        test_models = [
            "gemini-2.5-flash",
            "gemini-2.5-pro", 
            "gemini-2.0-flash",
        ]
        
        success_count = 0
        for model_name in test_models:
            try:
                print(f"Testing {model_name}...", end=" ")
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(
                    "Reply with just 'OK'",
                    generation_config=genai.GenerationConfig(max_output_tokens=10)
                )
                print(f"✅ SUCCESS")
                success_count += 1
            except Exception as e:
                error_msg = str(e)
                if "quota" in error_msg.lower() or "429" in error_msg:
                    print(f"❌ QUOTA EXCEEDED")
                elif "not found" in error_msg.lower() or "404" in error_msg:
                    print(f"⚠️  Not available")
                else:
                    print(f"❌ ERROR: {error_msg[:60]}")
        
        print("\n" + "=" * 70)
        print(f"Results: {success_count}/{len(test_models)} models working")
        print("=" * 70)
        
        return success_count > 0
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    api_key = ""
    success = test_api_key(api_key)
    sys.exit(0 if success else 1)
