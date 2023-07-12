from dotenv import load_dotenv
from os import getenv

load_dotenv()

URL_MYWORK: str = getenv("URL_MYWORK", None)
MYWORK_USERNAME: str = getenv("MYWORK_USERNAME", None)
MYWORK_PASSWORD: str = getenv("MYWORK_PASSWORD", None)