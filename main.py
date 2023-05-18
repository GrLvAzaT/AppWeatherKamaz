import requests
from bs4 import BeautifulSoup

# from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
import math
from kivy.core.window import Window

from kivy.garden.mapview import MapView
from kivy.uix.anchorlayout import AnchorLayout
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


Window.size = (540, 900)  # ширина,высота

class CustomPopup(Popup):
    def update_label(self, mapview):

        api_key = "eb85f5aa9655c4bff15badfb3106d42e"
        # print(mapview.lat)
        # print(mapview.lon)
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={mapview.lat}&lon={mapview.lon}&appid={api_key}"

            response = requests.get(url)
            x = response.json()
            print(x["name"])
            self.ids.maptext.text = x["name"]
        except requests.ConnectionError:
            print("Нет соединения с интернетом")


Builder.load_string(
    """
<CustomPopup>:
    size_hint: 0.8, 1.2 #width, length
    auto_dismiss: False
    title: 'Hello world'
    FloatLayout:
        MapView:
            id: mapview
            lat: 55.718505  # широта
            lon: 52.372104  # долгота
            zoom: 10  # масштаб карты
            size_hint: 0.9, 0.7  # задаем размеры карты
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}  # задаем позицию карты
            on_touch_down: 
                #app.on_touch_down(mapview)
                root.update_label(mapview)
        MDLabel:
            id : maptext
            text: ""
            pos_hint: {"center_x": 0.5, "center_y": .3}
            halign: "center"
            font_size: "30sp"
        Button:
            text: 'Узнать погоду в данной области'
            size_hint: 0.6, 0.1  
            # color: rgba(1,1,1,255)
            # # background_color: rgba(255, 255, 255, 255) 
            font_size: "20sp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}  
            on_press: 
                app.get_coordinates(mapview)
                root.dismiss()
"""
)

kv = """
MDFloatLayout:
    md_bg_color: 255/255, 255/255, 255/255, 1
    Image:
        source: "assets/location.png"
        size_hint: .10, .10
        pos_hint: {"center_x": .16, "center_y": .895}
    MDLabel:
        id:location
        text: ""
        pos_hint: {"center_x": .31, "center_y": .85}
        halign: "center"
        font_size: "25sp"
    Image:
        id: weather_image
        source: ""
        size_hint: .1, .1
        pos_hint: {"center_x": .84, "center_y": .85}
    MDLabel:
        id: temperature
        text: ""
        markup: True
        pos_hint: {"center_x": .7, "center_y": .90}
        halign: "center"
        font_size: "40sp"
    MDLabel:
        id : weather
        text: ""
        pos_hint: {"center_x": .7, "center_y": .85}
        halign: "center"
        font_size: "25sp"
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .70}
        size_hint: .22, .1
        Image:
            source: "assets/humidity.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: humidity
            text: ""
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "18sp"
        MDLabel:
            text: "Влажность воздуха"
            markup: True
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "17sp"
    MDFloatLayout:
        pos_hint: {"center_x": .7, "center_y": .70}
        size_hint: .22, .1
        Image:
            source: "assets/wind.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: wind_speed
            text: ""
            pos_hint: {"center_x": 1.1, "center_y": .7}
            font_size: "16sp"
        MDLabel:
            text: "Скорость ветра"
            pos_hint: {"center_x": 1.1, "center_y": .3}
            font_size: "17"
            
    MDFloatLayout:
        pos_hint: {"center_x": .25, "center_y": .55}
        size_hint: .22, .1
        Image:
            source: "assets/temperature.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: temp_min
            text: ""
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "18sp"
        MDLabel:
            text: "Мин температура"
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "17sp"
    MDFloatLayout:
        pos_hint: {"center_x": .7, "center_y": .55}
        size_hint: .22, .1
        Image:
            source: "assets/temperature.png"
            pos_hint: {"center_x": .1, "center_y": .5}
        MDLabel:
            id: temp_max
            text: ""
            pos_hint: {"center_x": 1, "center_y": .7}
            font_size: "18sp"
        MDLabel:
            text: "Макс температура"
            pos_hint: {"center_x": 1, "center_y": .3}
            font_size: "17sp"
    MDFloatLayout:
        size_hint_y: .50
        canvas:
            Color:
                rgb: rgba(116, 215, 255,255)
            RoundedRectangle:
                size: self.size
                pos:self.pos
                radius: [5,5,0,0]
        
        MDFloatLayout:
            pos_hint: {"center_x": .5, "center_y": .95}
            size_hint: .9, .22
            canvas:
                Color:
                    rgb: rgba(255,255,255, 255)
                RoundedRectangle:
                    size: self.size[0], self.size[1]-20
                    pos: self.pos[0], self.pos[1]-20
                    radius: [5] 
            TextInput:
                id: city_name
                hint_text: "Напишите название города"
                size_hint: 1,None
                pos_hint: {"center_x": .5, "center_y": .2}
                height: self.minimum_height
                multiline: False
                font_size: "20sp"
                hint_text_color: 0,0,0,0.7
                foreground_color: 0,0,0,1
                background_color: 1,1,1,0
                padding: 15
                cursor_color: 1,0.5,0.5,0.9
                cursor_width: "2sp"
        Button:
            text: "Узнать погоду"
            font_size: "20sp"
            size_hint: .7, .25
            pos_hint: {"center_x": .5, "center_y": .60}
            background_color: 1,1,1,0
            color: rgba(138,43,226,255)
            on_release: app.search_weather()
            canvas.before:
                Color:
                    rgb: 1,1,1,1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
        Button:
            text: "Узнать погоду по карте"
            font_size: "20sp"
            size_hint: .7, .25
            pos_hint: {"center_x": .5, "center_y": .34}
            background_color: 1,1,1,0
            color: rgba(1,1,1,255)
            on_release: app.show_popup()
            canvas.before:
                Color:
                    rgb: 1,1,1,1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [6]
     
"""


class Test_Погода(MDApp):
    api_key = "eb85f5aa9655c4bff15badfb3106d42e"
    citymap = ""
    def on_start(self):
        try:
            soup = BeautifulSoup(
                requests.get(
                    f"https://www.google.com/search?q=погода+в+моем+городе"
                ).text,
                "html.parser",
            )
            temp = soup.find("span", class_="BNeawe tAd8D AP7Wnd")

            location = "".join(
                filter(lambda item: not item.isdigit(), temp.text)
            ).split(",", 1)

            self.get_weather(location[0])
        except requests.ConnectionError:
            print("Нет интернет соединения")
            exit()

    def build(self):
        return Builder.load_string(kv)

    def show_popup(self):
        popup_window = CustomPopup()
        popup_window.open()


    # def on_touch_down(self, mapview):
    #     print(mapview.lat)
    #     print(mapview.lon)
    #
    #     try:
    #         url = f"http://api.openweathermap.org/data/2.5/weather?lat={mapview.lat}&lon={mapview.lon}&appid={self.api_key}"
    #
    #         response = requests.get(url)
    #         x = response.json()
    #         print(response)
    #
    #
    #         popup_window = CustomPopup()
    #         popup_window.update_label(x["name"])
    #
    #
    #     except requests.ConnectionError:
    #         print("Нет соединения с интернетом")


    def get_coordinates(self, mapview):

        self.get_city(mapview.lat,mapview.lon)
        mapview._layers.clear()




    def get_weather(self, city_name):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}"

            response = requests.get(url)
            x = response.json()
            print(x)

            if x["cod"] != "404":
                temperature = round(x["main"]["temp"] - 273.15)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = str(x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"] * 18 / 5)
                temp_min = int(math.floor(x["main"]["temp_min"] - 273.15))
                temp_max = int(math.ceil(x["main"]["temp_max"] - 273.15))
                location = x["name"] + ", " + x["sys"]["country"]
                self.root.ids.temperature.text = f"[b]{temperature}[/b]°"
                self.root.ids.weather.text = str(weather)
                self.root.ids.humidity.text = f"{humidity}%"
                self.root.ids.wind_speed.text = f"{wind_speed} km/h"
                self.root.ids.temp_min.text = f"{temp_min}°"
                self.root.ids.temp_max.text = f"{temp_max}°"
                self.root.ids.location.text = location
                if id == "800":
                    self.root.ids.weather_image.source = "assets/sun.png"
                elif "200" <= id <= "232":
                    self.root.ids.weather_image.source = "assets/storm.png"
                elif "300" <= id <= "321" or "500" <= id <= "531":
                    self.root.ids.weather_image.source = "assets/rain.png"
                elif "600" <= id <= "622":
                    self.root.ids.weather_image.source = "assets/snow.png"
                elif "701" <= id <= "781":
                    self.root.ids.weather_image.source = "assets/easyfog.png"
                elif "801" <= id <= "804":
                    self.root.ids.weather_image.source = "assets/clouds.png"
            else:
                print("Город не найден")
        except requests.ConnectionError:
            print("Нет соединения с интернетом")

    def get_city(self, lat, lon):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"

            response = requests.get(url)
            x = response.json()
            print(x)
            self.get_weather(x["name"])

            self.root.ids.city_name.text = x["name"]

        except requests.ConnectionError:
            print("Нет соединения с интернетом")

    def search_weather(self):
        city_name = self.root.ids.city_name.text
        if city_name != "":
            self.get_weather(city_name)




if __name__ == "__main__":
    Test_Погода().run()
