import os
import cv2
from file_handling import combine_path


class ImageConversion:
    def __init__(self, res, fps):
        self.res = res
        self.fps = fps

    def image_conversion(self, input_path, total_frames):

        video = cv2.VideoWriter(
            "final_video.mp4",
            cv2.VideoWriter_fourcc("m", "p", "4", "v"),
            int(self.fps),
            self.res,
        )
        for i in range(0, total_frames):
            image_name = "image{}.jpg".format(str(i))
            image_path = combine_path(input_path, image_name)
            video.write(cv2.imread(image_path))
        video.release()
