from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField('first name',max_length=30)
    last_name=models.CharField('last name',max_length=30)
    date_of_birth=models.DateField('date of birth')
    def get_relative_url(self):
        return "/api/author/%i/" % self.id

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    publish_date=models.DateTimeField("publish date",editable=True,auto_now_add=True)
    author=models.ForeignKey(Author)
    def get_relative_url(self):
        return "/api/post/%i/" % self.id


