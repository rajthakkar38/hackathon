from django.db import models
from django.contrib.auth.models import User
Gender_CHOICES = (
    ('Male','Male'),
    ('Female', 'Female'),
    ('Other','Other'),
)
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    #team_name = models.ForeignKey(Reg , null = True, on_delete=models.SET_NULL)
    return 'user_name_{0}/{1}'.format(instance.user.username , filename)

class problem(models.Model):

    problem_id = models.TextField(default="")
    title = models.TextField()
    desc = models.TextField()
    #problem_upload = models.FileField( blank=True ,default="", upload_to=user_directory_path)

    def __str__(self):
        return self.problem_id

class Reg(models.Model):

    user = models.ForeignKey(User , on_delete = models.CASCADE)

    Team_name = models.CharField(max_length = 50)
    M1_Name = models.CharField(max_length = 100 )
    M1_email = models.EmailField(null = True)
    M1_Mobile_no = models.CharField(null = True, max_length = 10)
    M1_gender = models.CharField(max_length=10, choices=Gender_CHOICES ,null=True)

    M2_Name = models.CharField(max_length = 100 )
    M2_email = models.EmailField(null = True)
    M2_Mobile_no = models.CharField(null = True, max_length = 10)
    M2_gender = models.CharField(max_length=10, choices=Gender_CHOICES ,null=True)

    M3_Name = models.CharField(max_length = 100)
    M3_email = models.EmailField(null = True)
    M3_Mobile_no = models.CharField(null = True, max_length = 10)
    M3_gender = models.CharField(max_length=10, choices=Gender_CHOICES ,null=True)

    M4_Name = models.CharField(max_length = 100 , blank=True)
    M4_email = models.EmailField(blank=True )
    M4_Mobile_no = models.CharField(max_length = 10 , blank=True )
    M4_gender = models.CharField(max_length=10, choices=Gender_CHOICES  , blank=True )

    M5_Name = models.CharField(max_length = 100 , blank=True )
    M5_email = models.EmailField( blank=True )
    M5_Mobile_no = models.CharField( max_length = 10, blank=True )
    M5_gender = models.CharField(max_length=10, choices=Gender_CHOICES , blank=True )

    Mentor_Name = models.CharField(max_length = 100 ,default =" ")
    Mentor_email = models.EmailField(null = True ,default =" ")
    Mentor_Mobile_no = models.CharField(null = True, max_length = 10 , default =" ")
    Mentor_gender = models.CharField(max_length=10, choices=Gender_CHOICES ,null=True,default =" ")

    def __str__(self):
        return self.Team_name



class ideas(models.Model):

    user = models.ForeignKey(User ,default="", on_delete = models.CASCADE)
    problem_id = models.ForeignKey(problem ,default="" , null = True, on_delete=models.SET_NULL)
    idea = models.FileField( blank=True ,default="", upload_to=user_directory_path)

    def __str__(self):
        return str(self.user)


class contactus(models.Model):

    name = models.CharField( max_length=200)
    user = models.ForeignKey(User ,default="", on_delete = models.CASCADE)
    email = models.EmailField()
    subject = models.TextField()

    def __str__(self):
        return str(self.user)
