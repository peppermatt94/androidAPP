# -*- coding: utf-8 -*-
"""
Created on Sat May  1 23:46:59 2021

@author: pepermatt94
"""
import certifi
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivy.core.audio import SoundLoader
from kivymd.uix.dialog import MDDialog
import random as rn
import webbrowser
from time import sleep
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
                            source: "Volto.png"
        
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
        

    def answerLODI(self):
        endpoint = "http://pepermatt94.pythonanywhere.com/"
        self.root.ids["mdlab"].text = "Caricamento in corso"
        self.rs_request = UrlRequest(endpoint+"lodi",
                                      on_success=self.get_data,
                                      ca_file=certifi.where(),on_failure=self.error, verify = True)
        self.root.ids["mdlab"].text = "Sono almeno uscito dall'answer"
        sleep(5)
        
    def error(self):
        self.root.ids["mdlab"].text = "errore nel caricamento pagina"
        
    def answerUFFICIO(self):
        endpoint = f"https://it.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&rnnamespace=0&format=json"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint+"ufficio",
                                      on_success=self.get_data,
                                      ca_file=certifi.where())
    def answerVESPRI(self):
        endpoint = f"http://pepermatt94.pythonanywhere.com/"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint+"vespri",
                                      on_success=self.get_data,
                                      ca_file=certifi.where())
        
    def answerORAMEDIA(self):
        endpoint = f"http://pepermatt94.pythonanywhere.com/"
        #following function select in the root (the app if we want) the "mdlab" widget
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint+"ora-media",
                                      on_success=self.get_data,
                                      ca_file=certifi.where(), on_failure=self.error)
        
    def answerCOMPIETA(self):
        endpoint = f"http://pepermatt94.pythonanywhere.com/"
        self.root.ids["mdlab"].text = "Caricamento in corso..."
        self.rs_request = UrlRequest(endpoint +"compieta",
                                      on_success=self.get_data,
                                      ca_file=certifi.where(), on_failure=self.error)
        

    def get_data(self, request, response):
        self.root.ids["mdlab"].text = "ora sono dentro il get_data"
        content = response
        try:
            response != ""
        except KeyError:
            content = f"Ci spiace, ma la ricerca delle lodi non ha prodotto risultati!\n\nRiprova! "
        self.root.ids["mdlab"].text = content
        
    def play(self):
        Random = str(rn.randint(1,100))
        endpoint = f"http://www.sanciro.ischia.it/2/{Random}.mp3"
        webbrowser.open(endpoint)
        
        
    def stop(self):
        #self.sound.stop()
        pass
           
MainApp().run()
