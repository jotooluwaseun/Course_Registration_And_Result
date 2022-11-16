from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Student


def createUserProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Student.objects.create(
            user=user,                       
            first_name=user.first_name,
            last_name=user.last_name,             
            email=user.email,            
            profile_completion=50                       
        )
       

def updateUserProfile(sender, instance, created, **kwargs):
    Student = instance
    user = Student.user

    if created == False:
        user.first_name = Student.first_name
        user.last_name = Student.last_name               
        user.email = Student.email      
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(createUserProfile, sender=User)
post_save.connect(updateUserProfile, sender=Student)
post_delete.connect(deleteUser, sender=Student)
