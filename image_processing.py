# select, resize and add the image to the linked list
from node import LinkedImage
from PIL import Image, ImageDraw, ImageFont
from char_density import char_density_sort
from file_handling import combine_path
import os


class FrameConvert:

    def __init__(self, subfolder, frame_file):
        self.filename = os.path.join(subfolder, frame_file)
        img = Image.open(self.filename)
        self.video_width, self.video_height = img.size
        self.ascii_width = 0
        self.ascii_height = 0
        self.size = 0
        self.pixel_matrix = img.getdata()
        self.font_size = 0
        self.font = None
        self.char_len = 0
        self.frame = None  # linked list with the (r,g,b) data
        self.converted_frame = (
            None  # linked list with the (ascii characters), (r,g,b) data
        )

    # resizes frame to the provided font size and add pixel matrix to a linked list
    def frame_resize(self, font_size=16):
        self.font_size = font_size
        # calculate character spacing relative to font size
        self.font = ImageFont.truetype("assets/fonts/CascadiaMono.ttf", int(font_size))
        self.char_len = self.font.getlength("*")
        # pixelate image by resizing character to the size of a pixel
        self.ascii_width = round(self.video_width / self.char_len)
        self.ascii_height = round(
            self.video_height * self.ascii_width / self.video_width
        )
        new_size = (self.ascii_width, self.ascii_height)
        self.pixel_matrix = self.pixel_matrix.resize(new_size)
        # add the resized matrix to a linked list
        self.frame = LinkedImage(self.ascii_width, self.ascii_height)
        for y in range(self.ascii_height):
            for x in range(self.ascii_width):
                # insert last pixel first, so it lands at the back of the linked list
                self.frame.insert_beginning(
                    self.pixel_matrix[
                        (self.ascii_width * self.ascii_height)
                        - (y * self.ascii_width)
                        - (x + 1)
                    ]
                )

    def make_ascii(self, string=" .:-=+*#%@"):
        self.converted_frame = LinkedImage(self.ascii_width, self.ascii_height)
        ascii_string = char_density_sort(string)
        ascii_length = len(ascii_string)
        for n in self.frame:
            r, g, b = n.value
            sum_rgb = r + g + b
            average_rgb = round(sum_rgb / 3)

            # use greyscale to find a corresponding dense character in the provided string
            i = round(ascii_length * average_rgb / 256)

            # insert the char and rgb value in a tuple
            self.converted_frame.insert_beginning(((ascii_string[i - 1]), (r, g, b)))

    # write asci characters to jgp file in output dir
    def ascii_to_frame(self, output_dir, file_count, bgcolor="black"):
        x, y = 0, 0
        self.size = (self.video_width, self.video_height)
        image = Image.new("RGB", self.size, bgcolor)
        draw = ImageDraw.Draw(image)
        width_count = 1

        for n in self.converted_frame.get_all_nodes():
            r, g, b = n.value[1]
            draw.text((x, y), n.value[0], font=self.font, fill=(r, g, b))
            x += self.char_len
            if width_count == self.ascii_width:
                width_count = 0
                x = 0
                y += self.char_len
            width_count += 1
        name = "image{}.jpg".format(file_count)
        filename = combine_path(output_dir, name)
        image.save(filename, "JPEG", subsampling=0, quality=100)
