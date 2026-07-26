import requests
from pathlib import Path

file_path = Path(__file__).parent / "Numbers.txt"

print("Please Edit The Numbers.txt File for adding numbers before start the program")
message = input("Please write your message: ")

def readphone_numbers(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def send_sms(api_key, receptor, message):
    kaveurl = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"
    params = {
        "receptor": receptor,
        "message": message,
    }
    response = requests.post(kaveurl, data=params)
    return response.status_code, response.text, response.ok

API_KEY = ""

numbers = readphone_numbers(file_path)
for number in numbers:
    status_code, response_text, success = send_sms(API_KEY, number, message)
    print(f"SMS to {number} status: {status_code}, Success: {success}, Response: {response_text}")
