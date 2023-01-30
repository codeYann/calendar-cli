from typing import List
from google_auth_oauthlib.flow import InstalledAppFlow
import os.path

SCOPES: List[str] = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.settings.readonly",
]


# class BaseAuth:
#     def __init__(
#         self, scopes: List[str] = SCOPES, path: str = "../../credentials.json"
#     ) -> None:
#         dir_name: str = os.path.dirname(__file__)
#         file_name: str = os.path.join(dir_name, path)
#         flow: InstalledAppFlow = InstalledAppFlow.from_client_secrets_file(
#             file_name, scopes=scopes
#         )
#         flow.run_local_server()
#         self.file_path = file_name
#         self.credentials = flow.credentials


class BaseAuth:
    def __init__(self, scopes: List[str]) -> None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(base_dir, "../../credentials.json")
        # flow = InstalledAppFlow.from_client_secrets_file(file_name, scopes=scopes)
        # flow.run_local_server()
        self.file_path = file_name
        # self.credentials = flow.credentials
