from django.db import models

# Create your models here.
class Blogpost(models.Model):
    blog_header = models.CharField( max_length=300)
    blog_body = models.TextField()
    author = models.CharField( max_length=150)
    post_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return f"{self.blog_header} {self.author}"