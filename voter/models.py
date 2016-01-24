from django.db import models
from django.contrib.auth.models import User


class Commissioner(models.Model):
    # A model for the commissioners table

    # This line is required to link commissioner to an instance of User model
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    # A model for the categories table

    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class Voter(models.Model):
    # A model for the voters table

    # This line is required to link voter to an instance of User model
    user = models.OneToOneField(User)
    commissioner = models.ForeignKey(Commissioner)      # A commissioner has many voters hence the category fk
    faculty = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    program = models.CharField(max_length=50)
    image_url = models.CharField(max_length=250)
    sex = models.CharField(max_length=25)

    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)


class Candidate(models.Model):
    # A model for the candidates table

    picture = models.ImageField(upload_to='profile_images', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    commissioner = models.ForeignKey(Commissioner)      # A commissioner has many candidates hence the category fk
    category = models.ForeignKey(Category)              # A category has many candidates hence the category fk
    faculty = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    program = models.CharField(max_length=50)
    sex = models.CharField(max_length=25)

    voters = models.ManyToManyField(Voter, through='Votes')      # Relationship between  a candidate and voter is a vote

    def __str__(self):
        return self.user_name


class Votes(models.Model):
    # A model for listing a candidate and their voters
    candidate = models.ForeignKey(Candidate)
    voter = models.ForeignKey(Voter)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{0} {1}".format(self.voter.first_name, self.voter.last_name)






