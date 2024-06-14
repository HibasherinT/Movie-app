from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    release_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, default=None)
    rating = models.IntegerField()
    comment = models.CharField(max_length=50)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.comment

