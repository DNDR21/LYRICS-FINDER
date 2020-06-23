import os
import sys


class local():

    def __init__(self,local):
        self.local=local

    def local_do(self):
        
        try:
            os.mkdir(self.local)
        except:
            pass

        open(self.local+".set_color.txt","w+")
        open(self.local+".last_theme.txt","w+").write("LIGHT")
        open(self.local+".local.txt","w+").write("D:/.Lyrics/")
