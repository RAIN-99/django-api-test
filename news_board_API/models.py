from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    link = models.URLField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.PositiveIntegerField(default=0, editable=False)
    author_name = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author_name}"
