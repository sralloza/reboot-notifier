from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504, 524],
    method_whitelist=["HEAD", "GET", "OPTIONS"],
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = Session()
session.mount("https://", adapter)
session.mount("http://", adapter)
