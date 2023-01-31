from typing import List
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES: List[str] = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.settings.readonly",
]


class BaseAuth:
    def __init__(self, scopes: List[str]) -> None:
        file_name = "/home/codeyan/projects/calendar-cli/credentials.json"
        flow = InstalledAppFlow.from_client_secrets_file(
            file_name,
            scopes=scopes
        )
        flow.run_local_server()
        self.credentials = flow.credentials
