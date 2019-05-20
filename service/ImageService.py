from urllib.request import urlopen, Request

import numpy
from skimage.measure import compare_ssim as ssim
from cv2 import imread, resize, cvtColor, COLOR_BGR2GRAY, imshow, imdecode


# import cv2

class ImageService:

    def compare_images(self, url1, url2):
        try:
            req = urlopen(Request(url1))
            arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
            image_a = imdecode(arr, -1)  # 'Load it as it is'

            req = urlopen(Request(url2))
            arr = numpy.asarray(bytearray(req.read()), dtype=numpy.uint8)
            image_b = imdecode(arr, -1)  # 'Load it as it is'

            height = 560
            width = 650

            image_a_resize = resize(image_a, (width, height))
            image_b_resize = resize(image_b, (width, height))

            image_a_resize_gray = cvtColor(image_a_resize, COLOR_BGR2GRAY)
            image_b_resize_gray = cvtColor(image_b_resize, COLOR_BGR2GRAY)

            similarity = ssim(image_a_resize_gray, image_b_resize_gray)

            print(similarity)
            if similarity > 0.75:
                return True
            else:
                return False

        except:
            return False
