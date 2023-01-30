# Import the base_auth module:w
from cli.api.auth import SCOPES, BaseAuth
import sys
import os

# Add the root folder to the Python search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestIt(BaseAuth):
    def __init__(self):
        super().__init__(SCOPES)
        print(self.file_path)


T = TestIt()
