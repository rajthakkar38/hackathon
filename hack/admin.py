from django.contrib import admin
from .models import problem
from .models import Reg
from .models import ideas
from .models import contactus

# Register your models here.

admin.site.register(problem)
admin.site.register(Reg)
admin.site.register(ideas)
admin.site.register(contactus)
