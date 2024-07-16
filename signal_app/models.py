from django.db import models


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=150)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment