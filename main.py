from video_to_image import VideoToImage
from image_processing import FrameConvert, FrameManipulation
from file_handling import make_temp_dir
import os


# create a class to fill the menu with names and operations
def main():
    video_instance = VideoToImage("assets", "sky.mov")
    video_settings = video_instance.video_to_image()
    ascii_frames_dir = make_temp_dir("assets", "ascii_frames")
    count = 0
    for subdir, dirs, files in os.walk(video_settings):
        for file in files:
            ascii_instance = FrameConvert(subdir, file)
            ascii_instance.get_frame()
            ascii_instance.frame_resize(280)
            ascii_ll = ascii_instance.frame_to_ll()
            ascii_instance = FrameManipulation(ascii_ll)
            ascii_instance.make_bnw()
            ascii_instance.make_ascii()
            ascii_instance.ascii_to_frame(ascii_frames_dir, count)
            count += 1
    print("{} frames have been converted").format(count)
    """
    ascii_instance = FrameConvert(video_settings[0])
    ascii_instance.get_frame()
    ascii_instance.frame_resize(280)
    ascii_instance_ll = ascii_instance.frame_to_ll()
    ascii_instance = FrameManipulation(test_frame_ll)
    ascii_instance.make_bnw()
    ascii_instance.make_ascii()
    ascii_instance.ascii_to_frame()
    """


if __name__ == "__main__":
    main()


"""



FONTS and WIDTH
CascadiaMono at 16px is 8px wide and 1px space



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
