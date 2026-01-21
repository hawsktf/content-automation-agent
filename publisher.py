from playwright.async_api import async_playwright
import os
import random
import asyncio
from dotenv import load_dotenv

load_dotenv()

class Publisher:
    def __init__(self):
        self.profile_path = os.getenv("FIREFOX_PROFILE_PATH")

    async def post_to_x(self, text: str):
        """Post to X using authenticated Firefox profile."""
        async with async_playwright() as p:
            context = await p.firefox.launch_persistent_context(
                self.profile_path,
                headless=False # Set to False initially for manual check if needed
            )
            page = await context.new_page()
            try:
                await page.goto("https://x.com/compose/post")
                await page.wait_for_selector('[data-testid="tweetTextarea_0"]')
                await page.fill('[data-testid="tweetTextarea_0"]', text)
                
                # Randomized delay to mimic human behavior
                await asyncio.sleep(random.uniform(5, 15))
                
                await page.click('[data-testid="tweetButtonInline"]')
                await page.wait_for_timeout(3000)
                print("Successfully posted to X")
            except Exception as e:
                print(f"Failed to post to X: {e}")
            finally:
                await context.close()

    async def post_to_nostr(self, text: str):
        """Post to NoSTR using a browser-based client (e.g., Iris or Snort)."""
        # Similar logic to X, targeting a specific NoSTR web client
        print("NoSTR posting placeholder")
        pass

    async def comment_on_youtube(self, video_url: str, comment: str):
        """Post a comment on a YouTube video."""
        async with async_playwright() as p:
            context = await p.firefox.launch_persistent_context(self.profile_path, headless=False)
            page = await context.new_page()
            try:
                await page.goto(video_url)
                # Logic to scroll find comment box and post
                pass
            finally:
                await context.close()
