from django.db import models

# Create your models here.
class Commissioner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    def _get_full_name(self):
        '''
        :return: voters fullname
        '''
        return '%s %s' %(self.first_name, self.last_name)
    full_name = property(_get_full_name())

class Voter(Commissioner):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # user_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=250)
    faculty = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    program = models.CharField(max_length=50)
    image_url = models.CharField(max_length=250)


class Candidate(Commissioner):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=250)
    faculty = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    program = models.CharField(max_length=50)
    sex = models.CharField(max_length=25)



class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=250)


class Votes(models.Model):
