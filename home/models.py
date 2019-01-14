from django.db import models
from home.helper import PAGES
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class GeneralHeader(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, null=True, blank=True)
    bg_img = models.ImageField(upload_to='bg_images', blank=True, null=True)
    page_name = models.IntegerField(default=0, choices=PAGES)
    button_text = models.CharField(max_length=255, blank=True, null=True)
    content = RichTextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(self.title)


class Navbar(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=1)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.title)


class Author(models.Model):
    profile_photo = models.ImageField(upload_to='profile_pictures')
    bg_image = models.ImageField(upload_to='bg_images')
    occupation = models.CharField(max_length=255)
    author = models.OneToOneField(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "{}".format(self.author)


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_subtitle = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    bg_img = models.ImageField(upload_to='bg_images', blank=True, null=True)
    content_text = models.CharField(max_length=255)
    auth = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.post_title)


class Footer(models.Model):
    social_name = models.CharField(max_length=255)
    icon_link = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.social_name)


class FooterText(models.Model):
    footer_text = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.footer_text)
