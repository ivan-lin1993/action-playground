import os
import requests


print(f"hello world { os.environ.get('CRED')}, {os.environ.get('mysecret')}")


res = requests.get(f"http://localhost:8000/?app={os.environ.get('mysecret')}")
print(res.content)