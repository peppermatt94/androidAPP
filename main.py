# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:46:59 2021

@author: pepermatt94
"""
import certifi
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
import bs4
import datetime
from kivy.core.audio import SoundLoader
import random as rn
from pydub import AudioSegment
from kivymd.uix.dialog import MDDialog



KV = """
NavigationLayout:

    ScreenManager:
        Screen:
            
            
            BoxLayout:
                orientation: 'vertical'
        
                MDToolbar:
                    title: "Liturgia del giorno"
                    elevation: 10
                    left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
        
                GridLayout:
                    rows: 8
                    #row_force_default:True
                    #row_default_height:40
            
                            
                    MDRaisedButton:
                        text: "Lodi"
                        #size: 75,50
                        #height:40
                        size_hint_x: .1
                        size_hint_y: .1
                        on_press: app.answerLODI()
                        
                    MDRaisedButton:
                        text: "Ufficio delle letture"
                        #size: 75,50
                        size_hint_x: .1
                        size_hint_y: 0.1
                        on_press: app.answerUFFICIO()
                        
                    MDRaisedButton:
                        text: "Ora Media"
                        #size: 75,50
                        size_hint_x: .1
                        size_hint_y: .1
                        on_press: app.answerORAMEDIA()
                        
            
                        
                    MDRaisedButton:
                        text: "Vespri"
                        #size: 75,50
                        size_hint_x: .1
                        size_hint_y: .1
                        on_press: app.answerVESPRI()
                        
                    MDRaisedButton:
                        text: "Compieta"
                        #size: 75,50
                        size_hint_x: .1
                        size_hint_y: .1
                        on_press: app.answerCOMPIETA()
                   
                     
            
                    ScrollView:
                        
                        MDLabel:
                            id: mdlab
                            text: "Clicca sull'ora che vuoi pregare!"
                            size_hint_y: None
                            height: self.texture_size[1]
                            text_size: self.width, None
                            
                                 
                    MDRaisedButton:
                        text: "Canto del cammino a caso"
                        size_hint_x:1
                        size_hint_y:0.1
                        on_press: app.play()
                            
                    MDRaisedButton:
                        text: "stop"
                        size_hint_x:1
                        size_hint_y:0.1
                        on_press: app.stop()
                        
            MDNavigationDrawer:
                id: nav_drawer

                BoxLayout:
                    orientation: "vertical"
                    padding: "8dp"
                    spacing: "8dp"
        
                    AnchorLayout:
                        anchor_x: "left"
                        size_hint_y: None
                        height: avatar.height
        
                        Image:
                            id: avatar
                            size_hint: None, None
                            size: "56dp", "56dp"
                            source: "data/logo/kivy-icon-256.png"
        
                    MDLabel:
                        text: "Liturgia Delle Ore App 0.1"
                        font_style: "Button"
                        size_hint_y: None
                        height: self.texture_size[1]
        
                    MDLabel:
                        text: "developed_by_pepermatt94"
                        font_style: "Caption"
                        size_hint_y: None
                        height: self.texture_size[1]
        
                    ScrollView:
        
                        MDList:
        
                            OneLineAvatarListItem:
                                text: "Contattaci:"
                                
        
                                IconLeftWidget:
                                    icon: "information-outline"
        
                            OneLineAvatarListItem:
                                text: "matteo.peperoni@libero.it"
                                
        
                                
                    
"""

class MainApp(MDApp):
    
    def build(self):
        self.title = "Hello kivy"
        self.theme_cls.theme_style = "Light"
        
        
        return Builder.load_string(KV)
        #layout = RelativeLayout()

    def answerLODI(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data={today}&ora=lodi-mattutine"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
        
    def answerUFFICIO(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data={today}&ora=ufficio-delle-letture"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
    def answerVESPRI(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data={today}&ora=vespri"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
        
    def answerORAMEDIA(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data={today}&ora=ora-media"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
        
    def answerCOMPIETA(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/la-liturgia-delle-ore/?data={today}&ora=compieta"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_data,
                                     ca_file=certifi.where())
        
    def answerMessa(self):
        today = datetime.date.today()
        today = f"{today.year}{today.month}{today.day}"
        endpoint = f"https://www.chiesacattolica.it/liturgia-del-giorno/?data-liturgia=20210505"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint,
                                     on_success=self.get_dataMISSA,
                                     ca_file=certifi.where())
   
    def get_data(self, request, response):
        html_reader = bs4.BeautifulSoup(response, "html.parser")
        LaudesElem = ".seed-post" 
        Laudes = html_reader.select(LaudesElem)
        Laudes = Laudes[0].getText()
        
        self.root.ids["mdlab"].text = Laudes
        
    def get_dataMISSA(self, request, response):
        html_reader = bs4.BeautifulSoup(response, "html.parser")
        LaudesElem = ".container main_container" 
        Laudes = html_reader.select(LaudesElem)
        Laudes = Laudes[0].getText()
        self.root.ids["mdlab"].text = Laudes
        
    def play(self):
        Random = str(rn.randint(1,80))
        endpoint = f"http://www.sanciro.ischia.it/2/{Random}.mp3"
        song = requests.get(endpoint)
        with open("todaySong.mpeg", "wb") as f:
            f.write(song.content)
            f.close()
        
        AudioSegment.from_file("todaySong.mpeg").export("todaySong.mp3", format="mp3")
        
        
        self.sound = SoundLoader.load("todaySong.mp3")
        self.sound.play()
        
    def stop(self):
        self.sound.stop()
MainApp().run()
