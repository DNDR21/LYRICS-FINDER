from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
)

import requests
from bs4 import BeautifulSoup as bs
import os












class MyScreenManager(ScreenManager):
	pass
		







	



class MenuScreen(Screen):
	
		
	
	
	
	
	def __init__(self,**kwargs):
		super(MenuScreen,self).__init__(**kwargs)
		
		self.pressed_open=0
		
		
	
	
	
	def click_go_settings_button(self):
		
		if self.pressed_open>=1:
			self.manager.current = "settings"
			self.manager.transition.direction = "right"			
	
	
	
	
	
	
	def click_downloaded_lyrics_button(self):
		if self.pressed_open>=1:
			self.manager.current="downloaded_lyrics"
			self.manager.transition.direction="up"
			try:
				files=os.listdir("/sdcard/.Lyrics/")
				list=sorted(files)
				for file in list[1:]:
					self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text+="\n"+file[:-4]+"\n"
			except:
				pass
				

				
			
	
	
	def click_open_button(self):
		
		if self.pressed_open<=0:
			self.ids.open_button.text="OPEN"
			try:
				open("/sdcard/.Lyrics/.set_color.txt","r+")
			
				dosya=open("/sdcard/.Lyrics/.set_color.txt","r+")
				for color in dosya.readlines():
					if color=="RED":
						self.manager.get_screen("settings").ids.switch_red.active=True
					elif color=="BLUE":
						self.manager.get_screen("settings").ids.switch_blue.active=True
					elif color=="BLACK":
						self.manager.get_screen("settings").ids.switch_black.active=True
					elif color=="CYAN":
						self.manager.get_screen("settings").ids.switch_cyan.active=True
					else:
						pass
			
					
			except:
				try:
					os.mkdir("/sdcard/.Lyrics/")
					open("/sdcard/.Lyrics/.set_color.txt","a+")
				except:
					pass
			
		
		
		
		self.pressed_open +=1
		
		
		
		
		
		
		
		if self.pressed_open>1:
			try:
				self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
				
				dosya=open("/sdcard/.Lyrics/"+self.ids.song_box.text+".txt","r")
				self.manager.get_screen("lyrics").ids.song_label.text=dosya.read()
				
				self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
				
				self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
				
				
				self.manager.current="lyrics"
				self.manager.transition.direction="left"
			except:
				if self.ids.song_box.text !="":
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
			
			
						self.manager.current="lyrics"
						self.manager.transition.direction = "left"
						
						
			
						self.manager.get_screen("lyrics").ids.song_label.text="\n"*5+(self.x1)+"\n"*5
						
						self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
						
						self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box.text
						
						self.manager.get_screen("menu").ids.label_info.text="Thank You For Using This Application\nLYRICS FINDER\nDeveloper:DNDR\n\nv1.1.2"
				
					except:
						self.ids.label_info.text="SONG NOT FOUND\n"
					
					
					






					

					
					

class LyricsScreen(Screen):
	
	def click_plus_button(self):
		self.ids.song_label.font_size +=1
	def click_minus_button(self):
		self.ids.song_label.font_size -=1
		









		
		
		
		
		
class SettingsScreen(Screen):
	
	
	def GRAY_COLOR(self):
		
		self.ids.back_menu_settings.background_color=self.GRAY
		
		self.manager.get_screen("menu").ids.open_button.background_color=self.GRAY
		self.manager.get_screen("menu").ids.go_settings_button.background_color=self.GRAY
		self.manager.get_screen("menu").ids.song_box.foreground_color=self.GRAY
		self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.GRAY
			
		self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.plus_button.background_color=self.GRAY
		self.manager.get_screen("lyrics").ids.minus_button.background_color=self.GRAY
		
		self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.GRAY
		self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.GRAY
		
		self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.GRAY
		self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.GRAY
		self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.GRAY
		
		##set_color##
		try:
			open("/sdcard/.Lyrics/.set_color.txt","w+").write("GRAY")
		except:
			try:
				os.mkdir("/sdcard/.Lyrics/")
			except:
				pass
		#########
		
		
		
		
	def __init__(self,**kwargs):
		super(SettingsScreen,self).__init__(**kwargs)
		
		self.RED=(255,0,0,1)
		self.BLACK=(0,0,0,1)
		self.CYAN=(0,139,139,1)
		self.BLUE=(0,0,255,1)
		self.WHITE=(255,255,255,1)
		self.GRAY=(1,1,1,1)
		
		self.COLOR=None
		
		


				






	def click_switch_red(self,instance,value):
		if value==True:
			
			self.ids.switch_blue.active=False
			self.ids.switch_black.active=False
			self.ids.switch_cyan.active=False
			
			self.COLOR=self.RED
			
			
			self.ids.back_menu_settings.background_color=self.COLOR
			
			self.manager.get_screen("menu").ids.open_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.song_box.foreground_color=self.COLOR
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.COLOR
			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.COLOR
			
			##set_color##
			try:
				open("/sdcard/.Lyrics/.set_color.txt","w+").write("RED")
			except:
				try:
					os.mkdir("/sdcard/.Lyrics/")
				except:
					pass
				
			#########
			
		else:
			if (self.ids.switch_blue.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_cyan.active==False):
				self.GRAY_COLOR()
			
			
			
			
			
	def click_switch_blue(self,instance,value):
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_black.active=False
			self.ids.switch_cyan.active=False
			
			self.COLOR=self.BLUE
			
			
			self.ids.back_menu_settings.background_color=self.COLOR
			
			self.manager.get_screen("menu").ids.open_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.song_box.foreground_color=self.COLOR
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.COLOR
			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.COLOR
			
			##set_color##
			try:
				open("/sdcard/.Lyrics/.set_color.txt","w+").write("BLUE")
			except:
				try:
					os.mkdir("/sdcard/.Lyrics")
				except:
					pass
			#########
			
		
		else:
			if (self.ids.switch_red.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_cyan.active==False):
				self.GRAY_COLOR()						
	
	
	
	
	def click_switch_black(self,instance,value):
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_blue.active=False
			self.ids.switch_cyan.active=False
			
			self.COLOR=self.BLACK
			
			
			self.ids.back_menu_settings.background_color=self.COLOR

			
			self.manager.get_screen("menu").ids.open_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.song_box.foreground_color=self.GRAY
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.COLOR
			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.GRAY
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.COLOR
			
			
			##set_color##
			try:
				open("/sdcard/.Lyrics/.set_color.txt","w+").write("BLACK")
			except:
				try:
					os.mkdir("/sdcard/.Lyrics/")
				except:
					pass
			#########
			

			
		else:
			if (self.ids.switch_blue.active==False) and (self.ids.switch_red.active==False) and (self.ids.switch_cyan.active==False):
				self.GRAY_COLOR()						
												


	def click_switch_cyan(self,instance,value):
		if value==True:
			
			self.ids.switch_red.active=False
			self.ids.switch_blue.active=False
			self.ids.switch_black.active=False
			
			self.COLOR=self.CYAN
			
			
			self.ids.back_menu_settings.background_color=self.COLOR

			
			self.manager.get_screen("menu").ids.open_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.go_settings_button.background_color=self.COLOR
			self.manager.get_screen("menu").ids.song_box.foreground_color=self.COLOR
			self.manager.get_screen("menu").ids.downloaded_lyrics_button.background_color=self.COLOR
			
			self.manager.get_screen("lyrics").ids.back_menu_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.save_lyrics_in_lyrics.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("add_lyrics").ids.save_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.back_lyrics_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.plus_button.background_color=self.COLOR
			self.manager.get_screen("add_lyrics").ids.minus_button.background_color=self.COLOR
			
			self.manager.get_screen("downloaded_lyrics").ids.song_box_downloaded_lyrics.foreground_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.open_downloaded_lyrics.background_color=self.COLOR
			self.manager.get_screen("downloaded_lyrics").ids.return_menu_downloaded.background_color=self.COLOR
			
			
			##set_color##
			try:
				open("/sdcard/.Lyrics/.set_color.txt","w+").write("CYAN")
			except:
				try:
					os.mkdir("/sdcard/.Lyrics/")
				except:
					pass
			#########
			
			

			

		else:
			if (self.ids.switch_blue.active==False) and (self.ids.switch_black.active==False) and (self.ids.switch_red.active==False):
				self.GRAY_COLOR()
			
	
				
	




	

	
	
	
	
	
class AddLyricsScreen(Screen):
			
	def click_plus(self):
		self.ids.lyrics_ti.font_size +=1
	def click_minus(self):
		self.ids.lyrics_ti.font_size -=1
	
	
	def click_back_lyrics_button(self):
		self.ids.save_lyrics_button.text="SAVE"
	
	def click_save(self):
		
		if (self.ids.path_ti.text !="") and (self.ids.lyrics_ti.text !=""):
			
			try:
				os.mkdir("/sdcard/.Lyrics")
			except:
				pass
				
			try:
				dosya=open("/sdcard/.Lyrics/"+(self.ids.path_ti.text)+".txt","w+")
				dosya.write(self.ids.lyrics_ti.text)
				
				self.ids.save_lyrics_button.text="SAVED"
			except:
				
				try:
					os.mkdir("/sdcard/.Lyrics")
				except:
					pass
				



















class DownloadedLyricsScreen(Screen):
	
		
	
	def click_return_menu_downloaded(self):
		self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
		
	def click_open_downloaded_lyrics(self):
		if (self.ids.downloaded_lyrics_label.text !=""):
			self.manager.get_screen("downloaded_lyrics").ids.downloaded_lyrics_label.text=""
			
			
			try:
				dosya=open("/sdcard/.Lyrics/"+self.ids.song_box_downloaded_lyrics.text+".txt","r")
				
				self.manager.get_screen("lyrics").ids.song_label.text=dosya.read()
				
				self.manager.get_screen("add_lyrics").ids.path_ti.text=self.ids.song_box_downloaded_lyrics.text
				self.manager.get_screen("add_lyrics").ids.lyrics_ti.text=self.manager.get_screen("lyrics").ids.song_label.text
				
				self.manager.current="lyrics"
				self.manager.transition.direction="up"
			except:
				self.ids.downloaded_lyrics_label.text="SONG NOT FOUND!!!"
		
		
	



	



	
	
	
	
	
class APP(App):
	def build(self):
		return Builder.load_file("LYRICS.kv")
		
APP().run()
