import gspread
from google.oauth2.service_account import Credentials
import os
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

class SheetsService:
    def __init__(self):
        self.scope = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.sheet_id = os.getenv("GOOGLE_SHEET_ID")
        self.creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
        self._client = None
        self._sheet = None

    @property
    def client(self):
        if not self._client:
            if os.path.exists(self.creds_path):
                creds = Credentials.from_service_account_file(self.creds_path, scopes=self.scope)
                self._client = gspread.authorize(creds)
            else:
                print(f"Warning: credentials.json not found at {self.creds_path}")
        return self._client

    def get_sources(self) -> List[Dict]:
        """Load active sources from Google Sheets."""
        if not self.client: return []
        try:
            sheet = self.client.open_by_key(self.sheet_id).sheet1
            records = sheet.get_all_records()
            return records
        except Exception as e:
            print(f"Error fetching sheets: {e}")
            return []

    def update_status(self, identifier: str, status: str, log: str = ""):
        """Update the status of a specific source or content ID."""
        if not self.client: return
        try:
            # Logic to find row and update cell
            pass
        except Exception as e:
            print(f"Error updating sheet: {e}")

    def log_error(self, message: str):
        """Log system-wide error to sheets."""
        if not self.client: return
        # Logic to append to error log sheet
        pass

# Singleton instance
sheets_service = SheetsService()
