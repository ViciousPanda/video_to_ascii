from video_to_image import VideoToImage
from image_processing import FrameConvert
from file_handling import make_temp_dir
from image_to_video import ImageConversion


# create a class to fill the menu with names and operations
def main():
    video_instance = VideoToImage("assets", "sky.mov")
    video_settings = video_instance.video_to_image()

    print(video_instance.counter)
    print(video_instance.temp_dir)

    ascii_frames_dir = make_temp_dir("assets", "ascii_frames")

    for i in range(0, video_instance.counter):
        file = "image{}.jpg".format(i)
        ascii_instance = FrameConvert(video_instance.temp_dir, file)
        ascii_instance.frame_resize(16)
        ascii_instance.make_ascii()
        ascii_instance.ascii_to_frame(ascii_frames_dir, i)

    print(video_instance.fps)
    print(ascii_instance.size)

    output_instance = ImageConversion(ascii_instance.size, video_instance.fps)
    output_instance.image_conversion(ascii_frames_dir, video_instance.counter)
    # print("{} frames have been converted").format(count)

    """    
    ascii_frames_dir = make_temp_dir("assets", "ascii_frames")
    count = 0

    for subdir, dirs, files in os.walk(video_settings):
        for file in files:
            ascii_instance = FrameConvert(subdir, file)
            ascii_instance.frame_resize(16)
            ascii_instance.make_ascii()
            ascii_instance.ascii_to_frame(ascii_frames_dir, count)
            count += 1
    print("{} frames have been converted").format(count)
    """


if __name__ == "__main__":
    main()


"""

TODO:
- reverse input string and make background white
- instead of iterate through a directory, store the filenames

"""
