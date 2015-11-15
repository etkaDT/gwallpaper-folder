#! /usr/bin/python3
import os
import random
from gi.repository import Gio

class wallpaperChanger(object):
    def __init__(self, folder=None):
        self.folder = folder
        self.chosen_one = None
        self.setting = Gio.Settings.new("org.gnome.desktop.background")

    def select_folder(self, folder):
        self.folder = folder

    def select_default_folder(self):
        home_folder = os.path.expanduser("~")
        self.folder =  "{home}/Images/Wallpapers".format(home=home_folder)

    def pick(self):
        files = os.listdir(self.folder)
        self.chosen_one = random.choice(files)

    def change(self):
        if not self.chosen_one or not self.folder:
            return
        full_path = os.path.join(self.folder, self.chosen_one)
        wallpaper = "file://{path}".format(path=full_path)
        self.setting.set_string("picture-uri", wallpaper)


if __name__ == "__main__":
    wpc = wallpaperChanger()
    wpc.select_default_folder()
    wpc.pick()
    wpc.change()
