#! /usr/bin/python3
import os
import random
from gi.repository import Gio

class wallpaperChanger(object):
    settings = {"background": "org.gnome.desktop.background",
                "locksreen" : "org.gnome.desktop.screensaver"}
    def __init__(self, folder=None, user=None, setting="background"):
        self.folder = folder
        self.chosen_one = None
        self.setting = Gio.Settings.new(self.settings[setting])
        self.user = user
        if user:
            self.change = self.su_change
        else:
            self.change = self.std_change

    def select_folder(self, folder):
        self.folder = folder

    def select_default_folder(self):
        home_folder = os.path.expanduser("~")
        self.folder =  "{home}/Images/Wallpapers".format(home=home_folder)

    def pick(self):
        files = os.listdir(self.folder)
        self.chosen_one = random.choice(files)

    def std_change(self, user=None):
        if not self.chosen_one or not self.folder:
            return
        full_path = os.path.join(self.folder, self.chosen_one)
        wallpaper = "file://{path}".format(path=full_path)
        self.setting.set_string("picture-uri", wallpaper)

    def su_change(self, user):
        pass


if __name__ == "__main__":
    wpc_w = wallpaperChanger(setting="background")
    wpc_w.select_default_folder()
    wpc_w.pick()
    wpc_w.change()

    wpc_w = wallpaperChanger(setting="locksreen")
    wpc_w.select_default_folder()
    wpc_w.pick()
    wpc_w.change()
