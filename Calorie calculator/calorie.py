import requests, json
class Calorie:
    def __init__(self, weight=40, height=140, age=20):
        self.weight = weight
        self.height= height
        self.age= age

    def temperature(self, city='Delhi'):
        self.city = city
        api_key = 'a393840d8dbf72d82b869d7c33dd4441'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + self.city
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"]!= 404:
            return data["main"]["temp"]
        else:
            return -1

    def calculate(self, temp):
        return round(10*self.weight + 6.5*self.height + 5 - 10*(temp -273.15), 2)

    


calorie = Calorie()
print(f'{calorie.temperature("Bangalore")} kelvin or {round(calorie.temperature("Bangalore")-273.15, 2)} celcius ')


