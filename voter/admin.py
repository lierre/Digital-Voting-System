from django.contrib import admin
from voter.models import Commissioner, Candidate, Category, Votes, Voter

admin.site.register(Commissioner)
admin.site.register(Candidate)
admin.site.register(Category)
admin.site.register(Votes)
admin.site.register(Voter)
