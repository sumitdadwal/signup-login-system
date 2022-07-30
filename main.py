import imp
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
import pandas as pd
import requests
import json
import http.client as httplib



class HomeScreen(Screen):
    pass
class SignUpScreen(Screen):
    def __init__(self, **kwargs):
      super(SignUpScreen, self).__init__(**kwargs)


    def createUserAccount(self):
        _username = ObjectProperty(None)
        _password = ObjectProperty(None)

        try:
            connection = httplib.HTTPSConnection('api.parse.com', 443)
            connection.connect()
            connection.request('POST', '/1/users', json.dumps({
                "username": self._username,
                "password": self._password,
            }), {
                "X-Parse-Application-Id": "nfgytgRuqQwkOqHxEhOEHKisT4sAxFIbCoOvbR5q",
                "X-Parse-REST-API-Key": "j9Qm7b6TuKZFiIAbONytGSWDLAAvWaie0dokk5nE",
                "Content-Type": "application/json"
            })
            result = json.loads(connection.getresponse().read())
            print(result)
        except:
            print("Error: Unable to connect!")
class LogInScreen(Screen):
    email = ObjectProperty(None)
    pwd = ObjectProperty(None)
    # def validate(self):


GUI = Builder.load_file("main.kv")
class MainApp(App):
    url = "http://localhost:8000/"
    def build(self):
        return GUI
    
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


    



MainApp().run()


