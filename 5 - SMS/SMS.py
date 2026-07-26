import requests

url =  "https://icanhazdadjoke.com/"

headers = {
    "Accept" : 'application/json'


}

print("Welcome to random joke program")

response = requests.get(url, headers=headers)

data = response.json()

joke = data["joke"]




API_KEY = ""




ques = "Y"
while ques != "N":
    print(f"Joke: {joke}")
    receptor = input("Please enter your recipient number: ")
    kaveurl = f"https://api.kavenegar.com/v1/{API_KEY}/sms/send.json"
    message = joke

    params = {
        "receptor" : receptor,
        "message" : message,
    }

    response = requests.post(kaveurl, data=params)

    print("SMS status: ", response.status_code)
    print(response.text)
    ques = input("Wanna Do That Again: (Y or N) ").strip().upper()