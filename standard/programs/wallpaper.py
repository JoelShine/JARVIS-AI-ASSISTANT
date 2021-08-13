import ctypes
import os
import random

images = os.listdir("C:\\Users\\joels\\Desktop\\Wallpapers")

imagePath = f"C:\\Users\\joels\\Desktop\\Wallpapers\\{random.choice(images)}"

def changeBG(imagePath):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
    return;

changeBG(imagePath)