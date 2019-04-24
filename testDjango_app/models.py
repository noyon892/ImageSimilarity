import os

from django.core.exceptions import ValidationError
from django.db import models
# from skimage.measure import compare_ssim
# import imutils
# import cv2

# from PIL import Image
# import pytesseract
# from difflib import SequenceMatcher


def update_filename(instance, filename):
    path = "images/"
    format = instance.name + '.jpg'
    return os.path.join(path, format)


def update_filename1(instance, filename):
    path = "images/"
    format = instance.name + '1.jpg'
    return os.path.join(path, format)


class Person(models.Model):
    name = models.CharField(max_length=32, default='')
    # email = models.EmailField(null=False, unique=True, blank=True)
    # phone_no = models.CharField(max_length=16, default='')
    # dob = models.DateField(default='')
    # sex = models.CharField(max_length=6, default='')
    # profession = models.CharField(max_length=32, default='')
    # address = models.TextField(null=True, default='')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, default="")
    image = models.ImageField(null=True, upload_to=update_filename)
    image2 = models.ImageField(null=True, upload_to=update_filename1)

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     image1 = cv2.imread("C:/Users/User/Desktop/download (2).jpg")
    #     image2 = cv2.imread("C:/Users/User/Desktop/download (2).jpg")
    #     image1 = cv2.resize(image1, (1200, 700))
    #     image2 = cv2.resize(image2, (1200, 700))
    #     # convert the images to grayscale
    #     gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    #     gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    #     (score, diff) = compare_ssim(gray1, gray2, full=True)
    #     if score != 1:
    #         super(Person, self).save(*args, **kwargs)
    #     else:
    #         raise ValidationError(u"You haven't set a valid department. Do you want to continue?")

    # def save(self, *args, **kwargs):
    #     img = self.image
    #     img2 = self.image2
    #     text = pytesseract.image_to_string(Image.open(img)).lower()
    #     text2 = pytesseract.image_to_string(Image.open(img2)).lower()
    #     ratio = SequenceMatcher(a=text, b=text2).ratio() * 100
    #     if ratio >= 100:
    #         print("Same Image %: " + str(ratio) + "% similarity")
    #         print(text)
    #         print("===========================================")
    #         print(text2)
    #         raise ValidationError(u"You haven't set a valid department. Do you want to continue?")
    #     else:
    #         print("Different Image:" + str(ratio)+ "% similarity")
    #         print(text)
    #         print("===========================================")
    #         print(text2)
    #         super(Person, self).save(*args, **kwargs)


class Department(models.Model):
    class Meta:
        verbose_name_plural = 'Departments'

    department_name = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.department_name
