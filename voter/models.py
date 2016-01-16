from django.db import models


class Commissioner(models.Model):
    # A model for the commissioners table

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Category(models.Model):
    # A model for the categories table

    category_name = models.CharField(max_length=50)
    category_description = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class Voter(models.Model):
    # A model for the voters table

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    commissioner = models.ForeignKey(Commissioner)      # A commissioner has many voters hence the category fk
    faculty = models.CharField(max_length=150)
    department = models.CharField(max_length=50)
    course = models.CharField(max_length=250)
    program = models.CharField(max_length=50)
    image_url = models.CharField(max_length=250)
    sex = models.CharField(max_length=25)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Candidate(models.Model):
    # A model for the candidates table

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
        return self.voter






