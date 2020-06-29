from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class Beauty(models.Model):
    name = models.TextField()
    address = models.TextField(blank=True, default='')
    telephone = models.TextField(blank=True, default='')
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sephoraweb:beauty_goods', args=[str(self.id)])


class Good(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="sephoraweb", blank=True, null=True)
    beauty = models.ForeignKey(Beauty, null=True, related_name='goods', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sephoraweb:good_detail', args=[str(self.beauty.id), str(self.id)])


# This Abstract Review can be used to create RestaurantReview and DishReview
class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class BeautyReview(Review):
    beauty = models.ForeignKey(Beauty, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return "{} review".format(self.beauty.name)
