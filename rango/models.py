from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):  # print object =toString()
        return self.name


'''
ForeignKey, one-to-many;
OneToOneField, one-to-one;
ManyToManyField, many-to-many.
'''


class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    # models.CASCADE -> 表示当被引用的对象（外键所指向的对象）被删除时，与之关联的对象（包含这个外键的对象）也会被级联删除
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # one-to-many relationship
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)  # 储存位置：MEDIA_ROOT/upload_to(dir)

    def __str__(self):
        return self.user.username
