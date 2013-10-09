import ctypes
import urllib
import time
import os, sys
import _winreg 
from bs4 import BeautifulSoup
def registerCentered():
    #changes the registry to center wallpaper
    try:
        wallpaperStyle = '0'
        tileWallpaper = '0'
        desktopKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                                         r'Control Panel\\Desktop',
                                         0,
                                         _winreg.KEY_SET_VALUE)
        _winreg.SetValueEx(desktopKey,
                               'WallpaperStyle',
                               0,
                               _winreg.REG_SZ,
                               wallpaperStyle)
        _winreg.SetValueEx(desktopKey,
                               'TileWallpaper',
                               0,
                               _winreg.REG_SZ,
                               tileWallpaper)
    except:
        continue
    return
registerCentered()
while True:
    try:
        url = "http://apod.nasa.gov/apod/astropix.html"
        page = BeautifulSoup(urllib.urlopen(url))
        for image in page.findAll("img"):
                print "Image: %(src)s" % image
        parsed = "http://apod.nasa.gov/apod/"+"%(src)s" % image
        x = urllib.urlretrieve(parsed)
        ctypes.windll.user32.SystemParametersInfoA(20, 0,x[0], 0)
        os.remove(x[0])
        time.sleep(86400)
    except:
        continue
