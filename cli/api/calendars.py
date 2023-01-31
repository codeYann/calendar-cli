from googleapiclient.discovery import build
from auth import BaseAuth, SCOPES


class CalendarAPI(BaseAuth):
    def __init__(self, calendar_id: str) -> None:
        super().__init__(scopes=SCOPES)
        self.calendar_id = calendar_id

    def get_calendar(self) -> None:
        with build("calendar", "v3", credentials=self.credentials) as service:
            calendar = (
                service
                .calendars()
                .get(calendarId=self.calendar_id)
                .execute()
            )
            print(calendar)
