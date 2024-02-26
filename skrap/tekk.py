import requests

resp = requests.get("https://www.google.com")

status = resp.status_code

if status == 200:
    print("Tenging náðist")
else:
    print(f"Eikka fokkin sjitt gerðist marr: {status}")

