import subprocess
import json
from typing import List, Dict

class DiscoveryService:
    def fetch_latest_youtube(self, channel_url: str, last_processed_id: str = None) -> List[Dict]:
        """Fetch latest videos from a YouTube channel using yt-dlp."""
        try:
            # yt-dlp command to get latest 5 videos metadata
            cmd = [
                'yt-dlp',
                '--get-title',
                '--get-id',
                '--flat-playlist',
                '--playlist-end', '5',
                '--dump-json',
                channel_url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            videos = []
            for line in result.stdout.strip().split('\n'):
                if not line: continue
                data = json.loads(line)
                video_id = data.get('id')
                if video_id == last_processed_id:
                    break
                videos.append({
                    "id": video_id,
                    "title": data.get('title'),
                    "url": f"https://www.youtube.com/watch?v={video_id}"
                })
            return videos
        except Exception as e:
            print(f"Error fetching YouTube videos: {e}")
            return []

    def fetch_latest_x(self, user_handle: str, last_processed_id: str = None) -> List[Dict]:
        """Fetch latest posts from X using browser scraping (Playwright)."""
        # Placeholder for browser-based X scraping
        return []

discovery_service = DiscoveryService()
