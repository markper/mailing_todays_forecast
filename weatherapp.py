import requests
import token_key

flag = True

print("This Is A Forecast Program That Shows The Current Weather \n")


def getTemprature():
    # To get the token key you need your own token key from openweathermap website
    location = input("\nPlease Enter Your Desired Location: ")
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" +
                     location + "&appid=" + token_key.token_key)
    j = r.json()
    # print(j)

    # Kelvin temprature to Celsius
    current_temprature = float(j["main"]["temp"]) - 273.15
    min_temprature = float(j["main"]["temp_min"]) - 273.15
    max_temprature = float(j["main"]["temp_max"]) - 273.15
    description = j["weather"][0]["description"]
    message = "\nThe lowest temprature in {} is: {} Celsius \nThe Highest temprature in {} is: {} Celsius \nThe Current temprature in {} is: {} Celsius {} \n".format(
        location, min_temprature, location, max_temprature, location, current_temprature, description)

    # outputs the current temprature within the disired location
    return message


message = getTemprature()

while flag:
    print(message)
    answer = input("would you like to check another locatins current forecast? Y|N ")
    if answer.upper() == "Y":
        getTemprature()
    else:
        flag = False
        print("\nHave a great day!\n")
