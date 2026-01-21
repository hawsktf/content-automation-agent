import os
import json
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

class Evaluator:
    def __init__(self, brand_config: Dict):
        self.brand = brand_config
        self.provider = os.getenv("AI_PROVIDER", "google")
        self.api_key = os.getenv("GOOGLE_API_KEY")

    def evaluate(self, transcript: str) -> Dict:
        """Evaluate alignment of transcript with brand rules."""
        # This would be an LLM call in reality
        # For now, a mock scoring logic
        prompt = f"""
        Brand: {self.brand['name']}
        Mission: {self.brand['mission']}
        
        Evaluate this content:
        {transcript[:1000]}...
        """
        
        # MOCK SCORE
        return {
            "score": 85,
            "rationale": "High alignment with brand mission. Content is educational and fits target audience.",
            "approved": True
        }

    def generate_blog(self, transcript: str) -> Dict:
        """Generate a blog post based on the transcript."""
        return {
            "html": "<h1>Generated Post</h1><p>...</p>",
            "slug": "generated-post",
            "excerpt": "A short excerpt...",
            "key_points": ["Point 1", "Point 2", "Point 3"]
        }
