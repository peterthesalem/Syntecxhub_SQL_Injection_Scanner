import requests
from payloads import SQL_PAYLOADS
from detector import detect_sql_error

url = input("Enter target URL: ")

for payload in SQL_PAYLOADS:

    print(f"\nTesting payload: {payload}")

    try:
        response = requests.get(url, timeout=5)

        print(f"Status Code: {response.status_code}")

        if detect_sql_error(response.text):
            print("Possible SQL Error Detected!")
        else:
            print("No SQL Errors Found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
