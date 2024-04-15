from django.db import models
from django.contrib.auth.models import User


class Types(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class News(models.Model):
    class StatusChoices(models.TextChoices):
        Publish = "PB", "Publish"
        Draft = "DR", "Draft"

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=StatusChoices.choices, default=StatusChoices.Draft)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'New'
        verbose_name_plural = 'News'


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    body = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='comments')
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
