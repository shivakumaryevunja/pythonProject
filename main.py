import json
import pyttsx3
import requests

while True:
    engine = pyttsx3.init()

    city = input("Enter the city to check the weather\n")

    if city == "q":
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=3ce25926b94b470b974171301230509&q={city}"

    r = requests.get(url)
    # print(r.text)
    wdata = json.loads(r.text)
    temprature = (wdata["current"]["temp_c"])
    condition = (wdata["current"]["condition"]["text"])
    humidity = (wdata["current"]["humidity"])
    engine.say(
        f"Today in {city} there are chances of {condition} with The temperature of {temprature} degree celestials and Humidity is {humidity} ")
    print("To quit enter q")
    engine.runAndWait()
