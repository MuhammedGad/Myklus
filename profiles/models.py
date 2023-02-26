from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model as user_model
User = user_model()

class Categories(models.Model):
    category = models.CharField(max_length=32)
    def __str__(self):
        return self.category

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    profile_pic = models.ImageField(default='')
    phone = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')
    category = models.ForeignKey(Categories, blank=True, on_delete=models.CASCADE)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(usta=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(usta=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.first_name


class Rating(models.Model):
    usta = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'usta'),)
        index_together = (('user', 'usta'),)