from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
import requests
from bs4 import BeautifulSoup as bs
import os
import sys

from search_lyrics import *
from local import *


Builder.load_file("LYRICS.kv")

local("D:/.Lyrics/").local_do()


class MenuScreen(Screen):
    
    def __init__(self,**kwargs):
        super(MenuScreen,self).__init__(**kwargs)
        self.pressed_open=0
        self.local=open("D:/.Lyrics/.local.txt","r").read()
        
    def click_search_button(self):
        
        search_lyrics=Search(self.ids.song_box.text)
        search_lyrics.search_lyrics()
        self.ids.searched_lyrics_label.text=""
        
        for i in search_lyrics.name[:-1]:
            self.ids.searched_lyrics_label.text +="\n"+i.get_text()+"\n"*3

    def click_downloaded_lyrics_button(self):
        self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
        files=os.listdir(self.local)#"/sdcard/.Lyrics/")
        files=sorted(files)
        files=files[3:]

        for file in files:
            self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+file[:-4]+"\n"

    def click_open_button(self):
        if self.pressed_open>=0:
            if self.ids.song_box.text !="":
                try:
                    file=open(self.local+self.ids.song_box.text+".txt","r", errors='ignore')#/sdcard/.Lyrics/
                    self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(file.read())+"\n"*5
                    self.manager.current="lyrics"
                    self.manager.transition.direction = "left"
                    self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
                    self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
                except :
                    try:
                        open_lyrics=Search(self.ids.song_box.text)
                        open_lyrics.open_lyrics()
                        
                        self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(open_lyrics.name)+"\n"*5
                        self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
                        self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
                        self.manager.current="lyrics"
                        self.manager.transition.direction = "left"
                    except AttributeError:
                        try:
                            open_lyrics=Search(self.ids.song_box.text)
                            open_lyrics.open_lyrics()
                            self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(open_lyrics.name)+"\n"*5
                            self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
                            self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
                            self.manager.current="lyrics"
                            self.manager.transition.direction = "left"
                        except:
                            try:
                                open_lyrics=Search(self.ids.song_box.text)
                                open_lyrics.open_lyrics()
                                self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(open_lyrics.name)+"\n"*5
                                self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
                                self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
                                self.manager.current="lyrics"
                                self.manager.transition.direction = "left"
                            except:
                                self.ids.searched_lyrics_label.text="SONG NOT FOUND\n"
                
                    
                    







class SettingsScreen(Screen):
    def __init__(self,**kwargs):
        super(SettingsScreen,self).__init__(**kwargs)
        self.local=open("D:/.Lyrics/.local.txt","r").read()
        
    def GRAY_COLOR(self):

        last_theme=open("D:/.Lyrics/"+".last_theme.txt","r+").read()
        if last_theme=="LIGHT":
            self.COLOR=self.LIGHT
            
        elif last_theme=="DARK":
            self.COLOR=self.DARK
            

        
        self.ids.back_menu_settings.background_color=self.COLOR
        
        self.manager.get_screen("menu").ids.open_button.background_color=self.COLOR
        self.manager.get_screen("menu").ids.go_settings_button.background_color=self.COLOR
        self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.COLOR
        self.manager.get_screen("menu").ids.search_button.background_color=self.COLOR

        self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.COLOR
        self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.COLOR
        self.manager.get_screen("lyrics").ids.plus_button.background_color=self.COLOR
        self.manager.get_screen("lyrics").ids.minus_button.background_color=self.COLOR

        self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.COLOR
        self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.COLOR
        self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.COLOR
        self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.COLOR

        self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.COLOR
        self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.COLOR

    def __init__(self,**kwargs):
        super(SettingsScreen,self).__init__(**kwargs)
        self.RED=(255,0,0,1)
        self.BLACK=(0,0,0,1)
        self.CYAN=(0,139,139,1)
        self.BLUE=(0,0,255,1)
        self.WHITE=(255,255,255,255)
        self.GRAY=(1,1,1,1)
        self.DARK=[0,0,0,1]
        self.LIGHT=[255,255,255,1]

    def light(self,instance,value):
        
        if value==True:

            open("D:/.Lyrics/"+".last_theme.txt","w+").write("LIGHT")
            
            self.ids.switch_dark.active=False
            self.ids.switch_red.active=False
            self.ids.switch_blue.active=False
            self.ids.switch_cyan.active=False

            self.background_color=self.LIGHT
            self.ids.settings_label.color=self.DARK
            self.ids.colors_label.color=self.DARK
            self.ids.back_menu_settings.background_color=self.LIGHT
            self.ids.back_menu_settings.color=self.DARK

            self.manager.get_screen("menu").background_color=self.LIGHT
            self.manager.get_screen("menu").ids.searched_lyrics_label.color=self.DARK
            self.manager.get_screen("menu").ids.open_button.background_color=self.LIGHT
            self.manager.get_screen("menu").ids.open_button.color=self.DARK
            self.manager.get_screen("menu").ids.go_settings_button.background_color=self.LIGHT
            self.manager.get_screen("menu").ids.go_settings_button.color=self.DARK
            self.manager.get_screen("menu").ids.song_box.background_color=self.LIGHT
            self.manager.get_screen("menu").ids.song_box.foreground_color=self.DARK
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.LIGHT
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.color=self.DARK
            self.manager.get_screen("menu").ids.search_button.background_color=self.LIGHT
            self.manager.get_screen("menu").ids.search_button.color=self.DARK

            self.manager.get_screen("lyrics").background_color=self.LIGHT
            self.manager.get_screen("lyrics").ids.song_label.color=self.DARK
            self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.LIGHT
            self.manager.get_screen("lyrics").ids.back_menu_lyrics.color=self.DARK
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.LIGHT
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.color=self.DARK
            self.manager.get_screen("lyrics").ids.plus_button.background_color=self.LIGHT
            self.manager.get_screen("lyrics").ids.plus_button.color=self.DARK
            self.manager.get_screen("lyrics").ids.minus_button.background_color=self.LIGHT
            self.manager.get_screen("lyrics").ids.minus_button.color=self.DARK

            self.manager.get_screen("downloaded_lyrics").background_color=self.LIGHT
            self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.background_color=self.LIGHT
            self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.LIGHT
            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.LIGHT
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.color=self.DARK

            self.manager.get_screen("add_lyrics").background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.color=self.DARK
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.color=self.DARK
            self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.plus_button.color=self.DARK
            self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.minus_button.color=self.DARK
            self.manager.get_screen("add_lyrics").ids.path_ti.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.path_ti.foreground_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.lyrics_ti.background_color=self.LIGHT
            self.manager.get_screen("add_lyrics").ids.lyrics_ti.foreground_color=self.DARK
            
        if value==False:
            
            self.ids.switch_dark.active=True


    def dark(self,instance,value):
        
        if value==True:

            open("D:/.Lyrics/"+".last_theme.txt","w+").write("DARK")
            
            self.ids.switch_light.active=False
            self.ids.switch_red.active=False
            self.ids.switch_blue.active=False
            self.ids.switch_cyan.active=False
            
            self.background_color=self.DARK
            self.ids.settings_label.color=self.GRAY
            self.ids.colors_label.color=self.GRAY
            self.ids.back_menu_settings.background_color=self.DARK
            self.ids.back_menu_settings.color=self.GRAY

            self.manager.get_screen("menu").background_color=self.DARK
            self.manager.get_screen("menu").ids.searched_lyrics_label.color=self.GRAY
            self.manager.get_screen("menu").ids.open_button.background_color=self.DARK
            self.manager.get_screen("menu").ids.open_button.color=self.GRAY
            self.manager.get_screen("menu").ids.go_settings_button.background_color=self.DARK
            self.manager.get_screen("menu").ids.go_settings_button.color=self.GRAY
            self.manager.get_screen("menu").ids.song_box.background_color=self.DARK
            self.manager.get_screen("menu").ids.song_box.foreground_color=self.GRAY
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.DARK
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.color=self.GRAY
            self.manager.get_screen("menu").ids.search_button.background_color=self.DARK
            self.manager.get_screen("menu").ids.search_button.color=self.GRAY

            self.manager.get_screen("lyrics").background_color=self.DARK
            self.manager.get_screen("lyrics").ids.song_label.color=self.GRAY
            self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.DARK
            self.manager.get_screen("lyrics").ids.back_menu_lyrics.color=self.GRAY
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.DARK
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.color=self.GRAY
            self.manager.get_screen("lyrics").ids.plus_button.background_color=self.DARK
            self.manager.get_screen("lyrics").ids.plus_button.color=self.GRAY
            self.manager.get_screen("lyrics").ids.minus_button.background_color=self.DARK
            self.manager.get_screen("lyrics").ids.minus_button.color=self.GRAY

            self.manager.get_screen("downloaded_lyrics").background_color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.color=self.GRAY
            self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.background_color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.GRAY
            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.color=self.GRAY
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.DARK
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.color=self.GRAY

            self.manager.get_screen("add_lyrics").background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.color=self.GRAY
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.color=self.GRAY
            self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.plus_button.color=self.GRAY
            self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.minus_button.color=self.GRAY
            self.manager.get_screen("add_lyrics").ids.path_ti.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.path_ti.foreground_color=self.GRAY
            self.manager.get_screen("add_lyrics").ids.lyrics_ti.background_color=self.DARK
            self.manager.get_screen("add_lyrics").ids.lyrics_ti.foreground_color=self.GRAY
            
        if value==False:
            
            self.ids.switch_light.active=True
            
    def click_switch_red(self,instance,value):

        if value==True:

            self.ids.switch_blue.active=False
            self.ids.switch_cyan.active=False

            self.ids.back_menu_settings.background_color=self.RED

            self.manager.get_screen("menu").ids.open_button.background_color=self.RED
            self.manager.get_screen("menu").ids.go_settings_button.background_color=self.RED
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.RED
            self.manager.get_screen("menu").ids.search_button.background_color=self.RED

            self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.RED
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.RED
            self.manager.get_screen("lyrics").ids.plus_button.background_color=self.RED
            self.manager.get_screen("lyrics").ids.minus_button.background_color=self.RED

            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.RED
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.RED
            self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.RED
            self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.RED

            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.RED
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.RED

        else:
            if (self.ids.switch_blue.active==False) and (self.ids.switch_cyan.active==False):
                self.GRAY_COLOR()

    def click_switch_blue(self,instance,value):

        if value==True:
            self.ids.switch_red.active=False
            self.ids.switch_cyan.active=False

            self.ids.back_menu_settings.background_color=self.BLUE

            self.manager.get_screen("menu").ids.open_button.background_color=self.BLUE
            self.manager.get_screen("menu").ids.go_settings_button.background_color=self.BLUE
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.BLUE
            self.manager.get_screen("menu").ids.search_button.background_color=self.BLUE

            self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.BLUE
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.BLUE
            self.manager.get_screen("lyrics").ids.plus_button.background_color=self.BLUE
            self.manager.get_screen("lyrics").ids.minus_button.background_color=self.BLUE

            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.BLUE
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.BLUE
            self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.BLUE
            self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.BLUE

            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.BLUE
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.BLUE

        else:
            if (self.ids.switch_red.active==False) and  (self.ids.switch_cyan.active==False):
                self.GRAY_COLOR()

    def click_switch_cyan(self,instance,value):

        if value==True:
            self.ids.switch_red.active=False
            self.ids.switch_blue.active=False

            self.ids.back_menu_settings.background_color=self.CYAN

            self.manager.get_screen("menu").ids.open_button.background_color=self.CYAN
            self.manager.get_screen("menu").ids.go_settings_button.background_color=self.CYAN
            self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.CYAN
            self.manager.get_screen("menu").ids.search_button.background_color=self.CYAN

            self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.CYAN
            self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.CYAN
            self.manager.get_screen("lyrics").ids.plus_button.background_color=self.CYAN
            self.manager.get_screen("lyrics").ids.minus_button.background_color=self.CYAN

            self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.CYAN
            self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.CYAN
            self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.CYAN
            self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.CYAN

            self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.CYAN
            self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.CYAN

        else:
            if (self.ids.switch_blue.active==False) and (self.ids.switch_red.active==False):
                self.GRAY_COLOR()






class LyricsScreen(Screen):
    def click_plus_button(self):
        self.ids.song_label.font_size +=1
    def click_minus_button(self):
        self.ids.song_label.font_size -=1






class AddLyricsScreen(Screen):
    def __init__(self,**kwargs):
        super(AddLyricsScreen,self).__init__(**kwargs)
        self.local=open("D:/.Lyrics/.local.txt","r").read()

    def click_back_lyrics_button(self):
        self.ids.save_lyrics_button.text="SAVE"

    def click_plus(self):
        self.ids.lyrics_ti.font_size +=1

    def click_minus(self):
        self.ids.lyrics_ti.font_size -=1

    def click_save(self):

        if (self.ids.path_ti.text !="") and (self.ids.lyrics_ti.text !=""):
            try:
                os.mkdir(self.local)#/sdcard/.Lyrics
            except:
                pass
            
            file=open(self.local+(self.ids.path_ti.text)+".txt","w+", errors='ignore')#/sdcard/.Lyrics
            file.write(self.ids.lyrics_ti.text)

            self.ids.save_lyrics_button.text="SAVED"

class DownloadedLyricsScreen(Screen):
    def __init__(self,**kwargs):
        super(DownloadedLyricsScreen,self).__init__(**kwargs)
        self.list_open=[]
        self.local=open("D:/.Lyrics/.local.txt","r").read()
        
    def on_text_song_box_downloaded_lyrics(self,instance):

        if instance.text !="":
            
            word=instance.text
            list=[]
            self.list_open=list 
            files=os.listdir(self.local)#/sdcard/.Lyrics
            files=sorted(files)
            files=files[3:]
            
            for file in files:
                if file[:-4].startswith(word) == True:
                    list.append(file[:-4])
                    self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""

                    for i in list:
                        self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+i+"\n"

        if instance.text=="":
            
            self.list_open=[]

            self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""

            try:
                files=os.listdir(self.local)#/sdcard/.Lyrics
                files=sorted(files)
                files=files[3:]
                
                for file in files:
                    self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+file[:-4]+"\n"
                    
            except:
                os.mkdir(self.local)#/sdcard/.Lyrics


    def click_return_menu_downloaded(self):

        self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""

    def click_open_downloaded_lyrics(self):

        if (self.ids.song_box_downloaded_lyrics.text !=""):

            if len(self.list_open)==1:

                self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""

                try:
                    file=open(self.local+self.list_open[0]+".txt","r", errors='ignore')#/sdcard/.Lyrics
                    self.manager.get_screen("lyrics").ids.song_label.text=file.read()
                    
                    self.manager.get_screen("add_lyrics").ids.path_ti.text=self.list_open[0]
                    self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text

                    self.manager.current="lyrics"
                    self.manager.transition.direction="up"
                except:
                    self.ids.downloaded_lyrics_label.text="SONG NOT FOUND!!!"

















sm = ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(SettingsScreen(name="settings"))
sm.add_widget(LyricsScreen(name="lyrics"))
sm.add_widget(AddLyricsScreen(name="add_lyrics"))
sm.add_widget(DownloadedLyricsScreen(name="downloaded_lyrics"))

class APP(App):
    def build(self):
        return sm


APP().run()
