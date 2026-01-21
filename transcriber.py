import asyncio
from playwright.async_api import async_playwright
import os
from dotenv import load_dotenv

load_dotenv()

class Transcriber:
    def __init__(self):
        self.profile_path = os.getenv("FIREFOX_PROFILE_PATH")
        self.output_dir = os.path.join(os.getenv("DATA_PATH"), "transcriptions")
        os.makedirs(self.output_dir, exist_ok=True)

    async def fetch_via_browser(self, video_url: str) -> str:
        """Cheat by using youtubetotranscript.com via browser automation."""
        async with async_playwright() as p:
            # Use persistent context to reuse session/profile
            context = await p.firefox.launch_persistent_context(
                self.profile_path,
                headless=True
            )
            page = await context.new_page()
            try:
                await page.goto("https://youtubetotranscript.com/")
                await page.fill('input[type="text"]', video_url)
                await page.click('button:has-text("Go")')
                
                # Wait for transcript to appear
                await page.wait_for_selector('.transcript-container', timeout=30000)
                transcript = await page.inner_text('.transcript-container')
                
                return transcript
            except Exception as e:
                print(f"Browser transcription failed: {e}")
                return ""
            finally:
                await context.close()

    def save_transcript(self, video_id: str, content: str):
        path = os.path.join(self.output_dir, f"{video_id}.txt")
        with open(path, "w") as f:
            f.write(content)
        return path

# Usage: transcriber = Transcriber(); await transcriber.fetch_via_browser("url")
