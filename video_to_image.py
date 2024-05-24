import cv2
import os
from file_handling import make_temp_dir, combine_path


class VideoToImage:
    def __init__(self, subfolder, video_file):
        self.filename = combine_path(subfolder, video_file)
        print(self.filename)
        self.temp_dir = None
        self.fps = None
        self.counter = 0

    def video_to_image(self):
        video = cv2.VideoCapture(self.filename)

        # empty temperary folder for images
        if video.isOpened():
            self.temp_dir = make_temp_dir("assets", "video_frames")
            print("\nProcessing video file... \n")

        success, image = video.read()
        self.fps = video.get(cv2.CAP_PROP_FPS)

        while success:
            # write frame to image
            cv2.imwrite(
                os.path.join(self.temp_dir, "image{}.jpg".format(str(self.counter))),
                image,
            )
            # cv2.imwrite("assets/images/image{}.jpg".format(str(counter)), image)
            success, image = video.read()
            self.counter += 1
        # When everything done, release the capture
        video.release()
        cv2.destroyAllWindows()
        print("{} frames have been rendered".format(self.counter))
        return self.temp_dir


'''


"""

print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(video.get(cv2.CAP_PROP_FPS))
print(video.get(cv2.CAP_PROP_FRAME_COUNT))

"""
'''
