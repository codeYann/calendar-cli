from typing import Any, List, Dict

# from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

SCOPES: List[str] = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.settings.readonly",
]


class EventAPI:
    def __init__(self) -> None:
        dir_name: str = os.path.dirname(__file__)
        file_name: str = os.path.join(dir_name, "../../credentials.json")
        flow: InstalledAppFlow = InstalledAppFlow.from_client_secrets_file(
            file_name, scopes=SCOPES
        )
        flow.run_local_server()
        self.credentials = flow.credentials

    def get_event(self, event_id: str) -> Dict[str, str]:
        wrapper: Dict[str, str]
        with build("calendar", "v3", credentials=self.credentials) as service:
            event = (
                service.events()
                .get(
                    calendarId="ccyan05@alu.ufc.br", eventId=event_id, singleEvents=True
                )
                .execute()
            )
            wrapper = event
        return wrapper

    def list_events(self) -> None:
        with build("calendar", "v3", credentials=self.credentials) as service:
            page_token = None
            while True:
                events = (
                    service.events()
                    .list(
                        calendarId="ccyan05@alu.ufc.br",
                        pageToken=page_token
                    )
                    .execute()
                )
                for event in events["items"]:
                    print(event["description"])
                break


api = EventAPI()
response = api.get_event("6gvbn1l99je9o94ptrp5o333ea")

print(response, type(response))

api.list_events()
