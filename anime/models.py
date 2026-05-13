from django.db import models
from django.contrib.auth.models import User




class Anime_List(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE , default=None)
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField()


#this function will show the actual title but not the objects
    def __str__(self):
        return f'{self.title}'
    


























# # class Anime(models.Model):
# #     STATUS_CHOICES = [
# #         ('watching', 'Watching'),
# #         ('completed', 'Completed'),
# #         ('dropped', 'Dropped'),
# #         ('plan_to_watch', 'Plan to Watch'),
# #     ]
# #     title = models.CharField(max_length=200)
# #     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
# #     current_episode = models.IntegerField(default=0)
# #     total_episodes = models.IntegerField(default=0)
# #     rating = models.FloatField(null=True, blank=True)
# #     created_at = models.DateTimeField(auto_now_add=True)


# class anime(models.Model):
#     title = models.CharField(max_length=255)

#     def __str__(self):
#         return self.title
# # Create your models here.
