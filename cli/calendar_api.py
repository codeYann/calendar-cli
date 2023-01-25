from typing import List
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import os

SCOPES: List[str] = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.settings.readonly",
]


class AgendaBase:
    def __init__(self, scopes: List[str]) -> None:
        dirname = os.path.dirname(__file__)
        file_name = os.path.join(dirname, "../token.json")
        self.cred: Credentials = Credentials.from_authorized_user_file(
            file_name, scopes
        )

    def agenda_list(self) -> None:
        with build("calendar", "v3", credentials=self.cred) as service:
            event = (
                service.events()
                .get(calendarId="ccyan05@alu.ufc.br", eventId="aaa")
                .execute()
            )
            print(event, event["summary"])


a = AgendaBase(SCOPES)
a.agenda_list()
