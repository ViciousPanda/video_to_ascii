# select, resize and add the image to the linked list
from node import LinkedImage
from PIL import Image, ImageDraw, ImageFont
from char_density import char_density_sort
from file_handling import make_temp_dir, combine_path
import os


class FrameConvert:

    def __init__(self, subfolder, frame_file):
        self.filename = os.path.join(subfolder, frame_file)
        self.max_width = 0
        self.max_height = 0
        self.current_width = 0
        self.current_height = 0
        self.pixel_matrix = None

    # convert filename frame to pixel matrix
    def get_frame(self):
        img = Image.open(self.filename)
        self.current_width, self.current_height = img.size
        self.max_width = self.current_width
        self.max_height = self.current_height
        self.pixel_matrix = img.getdata()

    # resizes frame to the provided character column width
    def frame_resize(self, character_columns):
        # will double the characters to keep dimentions intact
        character_columns = int(character_columns)
        if self.max_width > character_columns:
            self.current_width = character_columns
            self.current_height = round(
                self.max_height * character_columns / self.max_width
            )
        else:
            self.current_width = self.max_width
            self.current_height = self.max_height
        new_size = (self.current_width, self.current_height)
        self.pixel_matrix = self.pixel_matrix.resize(new_size)

    # add pixel matrix to a linked list
    def frame_to_ll(self):
        frame_list = LinkedImage(self.current_width, self.current_height)
        for y in range(self.current_height):
            for x in range(self.current_width):
                # insert last pixel first, so it lands at the back of the linked list
                frame_list.insert_beginning(
                    self.pixel_matrix[
                        (self.current_width * self.current_height)
                        - (y * self.current_width)
                        - (x + 1)
                    ]
                )
        return frame_list


class FrameManipulation:
    def __init__(self, frame):
        # linked list with the (r,g,b) data
        self.frame = frame
        # linked list with the (average values), (r,g,b) data
        self.frame_bnw = None
        # linked list with the (ascii characters), (average values), (r,g,b) data
        self.converted_frame = None
        self.width = frame.width
        self.height = frame.height

    # clear the console
    @staticmethod
    def cls():
        os.system("cls" if os.name == "nt" else "clear")

    # conversts (averages) the RGB frame Linked List into a monochrome frame Linked List
    def make_bnw(self):
        frame_list = LinkedImage(self.width, self.height)
        for n in self.frame:
            r, g, b = n.value
            sum_rgb = r + g + b
            average_rgb = round(sum_rgb / 3)
            frame_list.insert_beginning(((average_rgb), (r, g, b)))
        self.frame_bnw = frame_list

    # replaces pixel light values with ascii characters from strings
    def make_ascii(self, string=" .:-=+*#%@"):
        frame_list = LinkedImage(self.width, self.height)
        self.string = string
        ascii_string = char_density_sort(self.string)
        ascii_length = len(ascii_string)
        for n in self.frame_bnw:
            i = round(ascii_length * n.value[0] / 256)
            # insert the char in ascii_string in index value (* character spacing)
            frame_list.insert_beginning(
                ((ascii_string[i - 1]), (n.value[0]), (n.value[1]))
            )
        self.converted_frame = frame_list

    def ascii_to_frame(
        self, frames_dir, count, size=(1920, 1080), font_size=12, bgcolor="black"
    ):
        font = ImageFont.truetype("assets/fonts/CascadiaMono.ttf", font_size)
        w, h = size
        x, y = 0, 0
        image = Image.new("RGBA", size, bgcolor)
        draw = ImageDraw.Draw(image)
        width_count = 1

        for n in self.converted_frame.get_all_nodes():
            r, g, b = n.value[2]
            draw.text((x, y), n.value[0], font=font, fill=(r, g, b, 255))
            x += font.getlength(n.value[0])
            if width_count == self.width:
                width_count = 0
                x = 0
                y += font.getlength(n.value[0])
            width_count += 1
        name = "test_image{}.png".format(count)
        filename = combine_path(frames_dir, name)
        image.save(filename, "PNG")


"""



textsize was deprecated, the correct attribute is textlength which gives you the width of the text. for the height use the fontsize * how many rows of text you wrote.


# get an image
base = Image.open('images/boy.jpg').convert('RGBA')
# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('E:/PythonPillow/Fonts/Pacifico.ttf', 40)

# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((14,14), "Tutorials", font=fnt, fill=(255,255,255,128))

# draw text, full opacity
d.text((14,60), "Point", font=fnt, fill=(255,255,255,255))
out = Image.alpha_composite(base, txt)

#Show image
out.show()


def create_image(size, bgColor, message, font, fontColor):
    W, H = size
    image = Image.new("RGB", size, bgColor)
    draw = ImageDraw.Draw(image)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W - w) / 2, (H - h) / 2), message, font=font, fill=fontColor)
    return image


# create a class to fill the menu with names and operations
def main():
    video_instance = VideoToImage("assets", "sky.mov")
    video_instance.video_to_image()
    test_path = os.path.join(video_instance.temp_dir, "image0.jpg")
    print(test_path)
    test_frame = ImageConvert(test_path)
    test_frame.get_image()
    test_frame.image_resize(213)
    test_frame_ll = test_frame.image_to_ll()
    print(test_frame_ll.width)
    test_image = ImageManipulation(test_frame_ll)
    test_image.make_bnw()
    test_image.make_ascii()

    myMessage = test_image.print_ascii()
    myFont = ImageFont.truetype("assets/fonts/CascadiaMono.ttf", 16)
    myImage = create_image((1920, 1080), "black", myMessage, myFont, "white")
    myImage.save("test.png", "PNG")

    # print the ascii frame in the console
    def print_ascii(self):
        self.cls()
        print(
            "\n frame width = {}, frame height = {} \n".format(self.width, self.height)
        )

        ascii_string = ""

        width_count = 1
        for n in self.converted_frame.get_all_nodes():
            print(n.value, end="")
            ascii_string += n.value
            if width_count == self.width:
                print(" ")
                ascii_string += "\n"
                width_count = 0
            width_count += 1
        return ascii_string

"""
