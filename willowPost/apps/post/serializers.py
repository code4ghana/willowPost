from rest_framework import serializers,fields,reverse
from willowPost.apps.post import models


class AuthorSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField('get_url')
    class Meta:
        model=models.Author
        fields=('id','url','first_name','last_name','date_of_birth')

    def get_url(self,author):
       request = self.context['request']
       return reverse.reverse('author_details', args=[author.id],request=request)


class PostSerializer(serializers.ModelSerializer):
    url=serializers.SerializerMethodField('get_url')
    class Meta:
        model=models.Post
        fields=('id','url','title','content','author')

    def get_url(self,post):
       request = self.context['request']
       return reverse.reverse('post_details', args=[post.id],request=request)


