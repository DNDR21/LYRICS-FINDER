import kivy
from kivy.app import App
kivy.require('1.8.0')
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)

import requests
from bs4 import BeautifulSoup as bs
import os






















class MenuScreen(Screen):


        def __init__(self,**kwargs):
		super(MenuScreen,self).__init__(**kwargs)
		
		self.pressed_open=0
		

	def click_search_button(self):

		y=""
		x=self.ids.song_box.text

		for i in range(len(x)):
                        if i==0:
				y=x[0].upper()
			elif x[i]==" ":
				y+="-"
			else:
				y+=x[i].lower()



		link="https://search.azlyrics.com/search.php?q="+y+"&w=songs&p=1"
		r=requests.get(link)
		soup=bs(r.content,"html.parser")
		search_file=soup.find("div",{"class":"container main-page"})
		search_file=search_file.find_all("a")
		self.ids.searched_lyrics_label.text=""

		for i in search_file[:-1]:
			self.ids.searched_lyrics_label.text +="\n"+i.get_text()+"\n"*3


	def click_downloaded_lyrics_button(self):
                
		self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""	
		files=os.listdir("/sdcard/.Lyrics/")
		files=sorted(files)
			
		for file in files[1:]:
                        self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+file[:-4]+"\n"

                        
	def click_open_button(self):
		
		if self.pressed_open>=0:
                        
			if self.ids.song_box.text !="":
				
				try:
                                        
					dosya=open("/sdcard/.Lyrics/"+self.ids.song_box.text+".txt","r")
					self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(dosya.read())+"\n"*5
					self.manager.current="lyrics"
					self.manager.transition.direction = "left"
					self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
					self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
					
				except:
                                        
					y=""
					x=self.ids.song_box.text
					
					for i in range(len(x)):
						if i==0:
							y=x[0].upper()
						elif x[i]==" ":
							y+="-"
						else:
							y+=x[i].lower()
					try:
                                                
						self.r=requests.get("https://genius.com/"+y+"-lyrics")
						self.soup=bs(self.r.content,"html.parser")
						self.y1=self.soup.find("div",{"class":"lyrics"})
						self.x1=self.y1.get_text()
						self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(self.x1)+"\n"*5
						self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
						self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text

						self.manager.current="lyrics"
						self.manager.transition.direction = "left"
				
					except:
                                                
						self.ids.searched_lyrics_label.text="SONG NOT FOUND\n"




















class SettingsScreen(Screen):


	def GRAY_COLOR(self):
		
		self.ids.back_menu_settings.background_color=self.GRAY

		
		self.manager.get_screen("menu").ids.open_button.background_color=self.GRAY
		self.manager.get_screen("menu").ids.go_settings_button.background_color=self.GRAY
		self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.GRAY
		self.manager.get_screen("menu").ids.search_button.background_color=self.GRAY

			
		self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.plus_button.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.minus_button.background_color=self.GRAY

		
		self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.GRAY
		
		
		self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.GRAY
		self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.GRAY

		
	def __init__(self,**kwargs):
		super(SettingsScreen,self).__init__(**kwargs)
		
		self.RED=(255,0,0,1)
		self.BLACK=(0,0,0,1)
		self.CYAN=(0,139,139,1)
		self.BLUE=(0,0,255,1)
		self.WHITE=(255,255,255,1)
		self.GRAY=(1,1,1,1)
		self.DARK=[0,0,0,1]
		self.LIGHT=[1,1,1,1]

		
	def light(self,instance,value):
			
		if value==True:
			
			self.ids.switch_dark.active=False
			self.ids.switch_white.active=True
	
			
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
			self.ids.switch_white.active=False

			
	def dark(self,instance,value):
                
		if value==True:
                        
			self.ids.switch_light.active=False
			self.ids.switch_black.active=True
			
			
			self.background_color=self.DARK
			self.ids.settings_label.color=self.LIGHT
			self.ids.colors_label.color=self.LIGHT
			self.ids.back_menu_settings.background_color=self.DARK
			self.ids.back_menu_settings.color=self.LIGHT

			
			self.manager.get_screen("menu").background_color=self.DARK
			self.manager.get_screen("menu").ids.searched_lyrics_label.color=self.LIGHT		
			self.manager.get_screen("menu").ids.open_button.background_color=self.DARK
			self.manager.get_screen("menu").ids.open_button.color=self.LIGHT
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.DARK
			self.manager.get_screen("menu").ids.go_settings_button.color=self.LIGHT
			self.manager.get_screen("menu").ids.song_box.background_color=self.DARK
			self.manager.get_screen("menu").ids.song_box.foreground_color=self.LIGHT
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.DARK
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.color=self.LIGHT
			self.manager.get_screen("menu").ids.search_button.background_color=self.DARK
			self.manager.get_screen("menu").ids.search_button.color=self.LIGHT
			
			
			self.manager.get_screen("lyrics").background_color=self.DARK
			self.manager.get_screen("lyrics").ids.song_label.color=self.LIGHT
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.DARK
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.color=self.LIGHT
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.DARK
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.color=self.LIGHT
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.DARK
			self.manager.get_screen("lyrics").ids.plus_button.color=self.LIGHT
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.DARK
			self.manager.get_screen("lyrics").ids.minus_button.color=self.LIGHT
			
			
			self.manager.get_screen("downloaded_lyrics").background_color=self.DARK
			self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.color=self.LIGHT
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.background_color=self.DARK
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.LIGHT
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.DARK
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.color=self.LIGHT
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.DARK
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.color=self.LIGHT
		
			
			self.manager.get_screen("add_lyrics").background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.color=self.LIGHT
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.color=self.LIGHT
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.plus_button.color=self.LIGHT
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.minus_button.color=self.LIGHT
			self.manager.get_screen("add_lyrics").ids.path_ti.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.path_ti.foreground_color=self.LIGHT
			self.manager.get_screen("add_lyrics").ids.lyrics_ti.background_color=self.DARK
			self.manager.get_screen("add_lyrics").ids.lyrics_ti.foreground_color=self.LIGHT

			
		if value==False:
                        
			self.ids.switch_light.active=True
			self.ids.switch_black.active=False
			
	
	def click_switch_red(self,instance,value):
                
		if value==True:
			
			self.ids.switch_blue.active=False
			self.ids.switch_black.active=False
			self.ids.switch_white.active=False
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
                        
			if (self.ids.switch_blue.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_cyan.active==False):
                                
				self.GRAY_COLOR()

				
	def click_switch_blue(self,instance,value):
                
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_black.active=False
			self.ids.switch_white.active=False
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
                        
			if (self.ids.switch_red.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_cyan.active==False):
                                
				self.GRAY_COLOR()

				
	def click_switch_white(self,instance,value):
		
		if value==True:
                        
			self.ids.switch_red.active=False
			self.ids.switch_blue.active=False
			self.ids.switch_black.active=False
			self.ids.switch_cyan.active=False

			
			self.ids.back_menu_settings.background_color=self.WHITE

			
			self.manager.get_screen("menu").ids.open_button.background_color=self.WHITE
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.WHITE
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.WHITE
			self.manager.get_screen("menu").ids.search_button.background_color=self.WHITE

			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.WHITE
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.WHITE
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.WHITE
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.WHITE

			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.WHITE
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.WHITE
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.WHITE
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.WHITE

			
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.WHITE
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.WHITE
				
		else:
                        
			if (self.ids.switch_red.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_cyan.active==False) and (self.ids.switch_white.active==False):
                                
				self.GRAY_COLOR()

			
	def click_switch_black(self,instance,value):
                
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_blue.active=False
			self.ids.switch_white.active=False
			self.ids.switch_cyan.active=False
			
			
			self.ids.back_menu_settings.background_color=self.BLACK

			
			self.manager.get_screen("menu").ids.open_button.background_color=self.BLACK
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.BLACK
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.BLACK
			self.manager.get_screen("menu").ids.search_button.background_color=self.BLACK

			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.BLACK
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.BLACK
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.BLACK
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.BLACK

			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.BLACK
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.BLACK
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.BLACK
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.BLACK

			
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.BLACK
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.BLACK

		else:
                        
			if (self.ids.switch_blue.active==False) and (self.ids.switch_red.active==False) and (self.ids.switch_cyan.active==False):
                                
				self.GRAY_COLOR()

				
	def click_switch_cyan(self,instance,value):
                
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_blue.active=False
			self.ids.switch_black.active=False
			self.ids.switch_white.active=False

			
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
                        
			if (self.ids.switch_blue.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_red.active==False):
                                
				self.GRAY_COLOR()
				
	
	













class LyricsScreen(Screen):
	def click_plus_button(self):
		self.ids.song_label.font_size +=1
	def click_minus_button(self):
		self.ids.song_label.font_size -=1
		
		
		
		
	











class AddLyricsScreen(Screen):

	def click_back_lyrics_button(self):
		self.ids.save_lyrics_button.text="SAVE"
		
	def click_plus(self):
		self.ids.lyrics_ti.font_size +=1
		
	def click_minus(self):
		self.ids.lyrics_ti.font_size -=1
	
	def click_save(self):
                
		if (self.ids.path_ti.text !="") and (self.ids.lyrics_ti.text !=""):
                        
			try:
                                
				os.mkdir("/sdcard/.Lyrics")
			except:
                                
				pass
			
			dosya=open("/sdcard/.Lyrics/"+(self.ids.path_ti.text)+".txt","w+")
			dosya.write(self.ids.lyrics_ti.text)
			
			self.ids.save_lyrics_button.text="SAVED"









					
					
					






class DownloadedLyricsScreen(Screen):
        
	def __init__(self,**kwargs):
		super(DownloadedLyricsScreen,self).__init__(**kwargs)
		
		self.list_open=[]

		
	def on_text_song_box_downloaded_lyrics(self,instance):
                
		if instance.text !="":
			
			word=instance.text
			list=[]
			self.list_open=list
			files=os.listdir("/sdcard/.Lyrics/")
			files=sorted(files)
			
			for file in files[1:]:
                                
				if file[:-4].startswith(instance.text):
                                        
					list.append(file[:-4])
					self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
					
					for i in list:
                                                
						self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+i+"\n"

		
		if instance.text=="":
                        
			self.list_open=[]
			self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
			try:
                                
				files=os.listdir("/sdcard/.Lyrics/")
				files=sorted(files)
				
				for file in files[1:]:
                                        
					self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+file[:-4]+"\n"
			except:
                                
				os.mkdir("/sdcard/.Lyrics/")

				
	def click_return_menu_downloaded(self):
                
		self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""

		
	def click_open_downloaded_lyrics(self):
                
		if (self.ids.song_box_downloaded_lyrics.text !=""):
                        
			if len(self.list_open)==1:
                                
				self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
				try:
                                        
					dosya=open("/sdcard/.Lyrics/"+self.list_open[0]+".txt","r")
					self.manager.get_screen("lyrics").ids.song_label.text=dosya.read()
					self.manager.get_screen("add_lyrics").ids.path_ti.text=self.list_open[0]
					self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
					
					self.manager.current="lyrics"
					self.manager.transition.direction="up"
				except:
                                        
					self.ids.downloaded_lyrics_label.text="SONG NOT FOUND!!!"
		
		
	



	















class MyScreenManager(ScreenManager):
	pass









class APP(App):
	App.background_color=(1, 1, 1, 1)
	App.color=(0,0,0,1)
	def build(self):
		return Builder.load_file("LYRICS.kv")
APP().run()