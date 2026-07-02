from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    title = models.CharField(max_length=250)

    slug = models.SlugField(blank=True, unique=True)

    image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    excerpt = models.TextField(max_length=250)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    featured = models.BooleanField(default=False)

    published = models.BooleanField(default=True)

    def save(self,*args,**kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args,**kwargs)

    def __str__(self):
        return self.title