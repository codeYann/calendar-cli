# from googleapiclient.discovery import build

# from .auth import BaseAuth, SCOPES
from auth import BaseAuth, SCOPES


class CalendarApi(BaseAuth):
    def __init__(self, calendar_id: str) -> None:
        super().__init__(scopes=SCOPES)
        self.calendar_id = calendar_id

    def get_calendar(self) -> None:
        print(self.file_path)
        # with build("calendar", "v3") as service:
        # calendar = service.calendars().get(calendarId=self.calendar_id).execute()
        # print(calendar)


tst = CalendarApi("codeyan10@gmail.com")
tst.get_calendar()
