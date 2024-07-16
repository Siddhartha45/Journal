from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import CustomUser, BlogPost, Comment
from django.dispatch import Signal


comment_added = Signal()


@receiver(post_save, sender=CustomUser)
def print_welcome_user(sender, instance, created, **kwargs):
    if created:
        print("sender:", sender)
        print("instance:", instance)
        print(f"Hello {instance.name}!, You are welcome")


@receiver(post_delete, sender=BlogPost)
def blogpost_postdelete_message(sender, instance, **kwargs):
    print(f"{instance.id} deleted from the database.")


# @receiver(post_save, sender=Comment)
# def notify_author_on_comment(sender, instance, created, **kwargs):
#     if created:
#         notification_message = f"{instance.comment_user} commented on your post {instance.blogpost}"
#         print(f"Sending notification to {instance.blogpost.author}: {notification_message}")


@receiver(comment_added, sender=None)
def notify_author_on_comment(sender, comment, **kwargs):
    blogpost_author = comment.blogpost.author
    notification_message = f"{comment.comment_user} commented on your post {comment.blogpost}"
    print(f"Sending notification to {blogpost_author}: {notification_message}")
