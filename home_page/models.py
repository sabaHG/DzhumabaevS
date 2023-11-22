from django.db import models

class CarModel(models.Model):
    GENRE = (
        ('Sedan', 'Sedan'),
        ('Universal', 'Universal'),
        ('SUV' , 'SUV'),
    )
    title = models.CharField(max_length=100, verbose_name="Enter your car name")
    description = models.TextField()
    image = models.ImageField(upload_to='cars/')
    cost = models.PositiveIntegerField()
    type = models.CharField(max_length=100, choices=GENRE)


    def __str__(self):
        return self.title

class Afisha(models.Model):
    title_car = models.CharField(max_length=100)
    created_ad = models.DateField(null= True)

    def __str__(self):
        return self.title_car
class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo

