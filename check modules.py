import os#import os lib

install_modules=["setuptools","--upgrade pip wheel setuptools virtualenv","docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*","kivy_deps.gstreamer==0.1.*","kivy_deps.angle==0.1.*","kivy","requests","bs4"]#modules to be added

uninstall_modules=["-y kivy.deps.glew kivy.deps.gstreamer kivy.deps.sdl2 kivy.deps.angle"]


os.system("python -m pip install --upgrade pip ")
for i in uninstall_modules:
        os.system("python -m pip uninstall "+i)#uninstall modules
for i in install_modules:
	os.system("python -m pip install "+i)#install modules
