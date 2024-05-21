from video_to_image import VideoToImage
from image_processing import ImageConvert
import sys
from menu import Menu


# use function menu_builder to make a menu
def menu_builder(class_name):
    menu_instance = Menu(class_name)
    menu_instance.draw()
    getattr(globals()[menu_instance.class_name_str](), menu_instance.option)()


class MainMenu:
    def video_select(self):
        video_instance = VideoToImage("assets", "sky.mov")
        video_instance.video_to_image()

    def resize(self):
        menu_builder(SizeMenu)

    def ascii_code(self):
        pass

    def build_ascii(self):
        pass

    def quit(self):
        print("Quit program" + "\n")
        sys.exit(0)


class SizeMenu:
    def hd(self):
        pass

    def full_hd(self):
        pass

    def quad_hd(self):
        pass

    def ultra_hd(self):
        pass

    def back(self):
        menu_builder(MainMenu)

    def quit(self):
        print("Quit program" + "\n")
        sys.exit(0)


# create a class to fill the menu with names and operations
def main():
    menu_builder(MainMenu)


if __name__ == "__main__":
    main()


"""
import file
make images

import images

    resize / pixelate
        720p
        1080p
        2k
        4k
        
    black and white
    
    ascii conversion
    
    color
    
    
    

"""
