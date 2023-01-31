from .auth import BaseAuth, SCOPES
from typing import Dict
from googleapiclient.discovery import build


class EventAPI(BaseAuth):
    def __init__(self, calendar_id: str) -> None:
        super().__init__(scopes=SCOPES)
        self.calendar_id = calendar_id

    def get_event(self, event_id: str) -> Dict[str, str]:
        wrapper: Dict[str, str]
        with build("calendar", "v3", credentials=self.credentials) as service:
            event = (
                service.events()
                .get(calendarId=self.calendar_id, eventId=event_id)
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
                    .list(calendarId=self.calendar_id, pageToken=page_token)
                    .execute()
                )
                for event in events["items"]:
                    print(event["description"])
                break
