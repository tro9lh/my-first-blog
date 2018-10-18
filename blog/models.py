from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator


class Post(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    HAIR_CHOICES = (
        ('блонд', 'блонд'),
        ('брюнет','брюнет'),
        ('шатен','шатен'),
        ('рыжий','рыжий'),
        ('русый','русый'),
        ('седой','седой'),
    )

    FAVORITE_ANIMAL = (
        ('Собачка','Собачка'),
        ('Кошечка','Кошечка'),
        ('нечто среднее','нечто среднее'),
    )

    HAVE_ANIMAL = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    #img = models.CharField(validators=[URLValidator()], null=True, max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, null=True)
    patronymic = models.CharField(max_length=200, null=True)
    DateofBirth = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    img = models.ImageField(upload_to = 'blog/pic_folder/', default = 'blog/pic_folder/15709.jpg')
    hairСolor = models.CharField(max_length=6, choices=HAIR_CHOICES, null=True)
    weight = models.IntegerField(null=True)
    favoriteAnimal = models.CharField(max_length=100,choices=FAVORITE_ANIMAL, null=True)
    haveAnimal = models.CharField(max_length=1, choices=HAVE_ANIMAL, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
