from django.shortcuts import render, HttpResponse
from .models import CustomUser, BlogPost, Comment
from .signals import comment_added

# Create your views here.
def add_comment(request):
    blogpost = BlogPost.objects.get(id=5)
    comment_author = CustomUser.objects.get(id=8)
    # print(blogpost, comment_author)
    comment = Comment.objects.create(comment="comment 2", blogpost=blogpost, comment_user=comment_author)
    comment_added.send(sender=None, comment=comment)
    return HttpResponse("ok")