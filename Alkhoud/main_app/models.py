from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''class Profile(models.Model):
     
     #user = models.OneToOneField(User, on_delete=models.CASCADE)
     avatar = models.ImageField(upload_to="images/", default="images/default.jpg")
     level = models.IntegerField()
     age = models.IntegerField()
     city = models.CharField(max_length=200)'''
     
'''class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    decription = models.TextField()'''

class Club (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    type_choices = models.TextChoices("Club Type", ["Gym", "Self_defense ","Equestrian"])
    city_choices = models.TextChoices("Club Type", ["Riyadh", "Jeddah ","Hail", 'Dammam'])
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200 , default=None) # نغيرها إلى تشويس
    decription = models.TextField()
    city = models.CharField(max_length=200, default="Riyadh")
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

class Say (models.Model):
    name = models.CharField(max_length=200)
    decription = models.TextField()

class Offers (models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()

class Package (models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE, default=1)
    package_type = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    duration = models.CharField(max_length=200)



class Comment(models.Model):
    club = models.ForeignKey(Club,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)







'''

class Subscriber(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(max_length=200)
    package = models.ForeignKey(Package, on_delete=models.CASCADE) '''

class Coach (models.Model):
    #user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    coach_name = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    experience = models.CharField(max_length=200) #عدد  سنوات الخبرة للمدرب

class Tournament(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    tournament_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")


'''
class Enroll(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    is_enrolled = models.BooleanField(default=False)


class Payment(models.Model):
    #club = models.ForeignKey(Club, on_delete=models.CASCADE)
    #subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=200)
    card_holder_name = models.CharField(max_length=400)
    expired_date = models.DateField()
    cvv = models.IntegerField()
    # is_paid = models.BooleanField(default=False)

class Review(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.FloatField()

'''

class Contact (models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()