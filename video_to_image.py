import cv2
import os
import shutil


class VideoToImage:
    def __init__(self, subfolder, video_file):
        self.root_dir = os.path.dirname(__file__)
        self.asset_dir = os.path.join(self.root_dir, subfolder)
        self.filename = os.path.join(self.asset_dir, video_file)
        self.temp_dir = None
        self.fps = None
        self.counter = 0

    def create_temp_folder(self, temp_folder_name="video_frames"):
        self.temp_dir = os.path.join(self.asset_dir, temp_folder_name)
        if os.path.isdir(self.temp_dir):
            print("removing folder")
            shutil.rmtree(self.temp_dir)
            print("making folder at {}".format(self.temp_dir))
            os.mkdir(self.temp_dir)
        else:
            os.mkdir(self.temp_dir)
            print("making folder at {}".format(self.temp_dir))

    def video_to_image(self):
        video = cv2.VideoCapture(self.filename)

        # empty temperary folder for images
        if video.isOpened():
            self.create_temp_folder()
            print("\n Processing video file...")

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


'''


def video_to_image(path, filename):

    # read video content
    video = cv2.VideoCapture(local_filename)

    # empty temperary folder for images
    if video.isOpened():
        print("Making temperary folder")
        create_temp_folder(local_dir)
        print("Processing video file")
    success, image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    counter = 0
    # print(cv2.getBuildInformation())

    while success:
        # write frame to image
        cv2.imwrite(
            os.path.join(local_dir, "/images/image{}.jpg".format(str(counter))),
            image,
        )
        # cv2.imwrite("assets/images/image{}.jpg".format(str(counter)), image)
        success, image = video.read()
        counter += 1
    # When everything done, release the capture
    video.release()
    cv2.destroyAllWindows()
    return fps, counter


def create_temp_folder(local_dir):
    folder = os.path.join(local_dir, "/temp_frames")
    if os.path.isdir(folder):
        print("removing folder")
        shutil.rmtree(folder)
        print("making folder at {}".format(folder))
        os.mkdir(folder)
    else:
        os.mkdir(folder)
        print("making folder at {}".format(folder))
    return None

    if not os.listdir("/your/path"):
        print("Directory is empty")
    else:
        print("Directory is not empty")

    shutil.rmtree("/home/me/test")
    os.mkdir("/home/me/test")

    dirName = "/home/varun/temp"

    if os.path.exists(dirName) and os.path.isdir(dirName):
        if not os.listdir(dirName):
            print("Directory is empty")
        else:
            print("Directory is not empty")
    else:
        print("Given Directory don't exists")


"""

print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(video.get(cv2.CAP_PROP_FPS))
print(video.get(cv2.CAP_PROP_FRAME_COUNT))

"""
'''
