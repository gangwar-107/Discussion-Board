from django.contrib import admin

# Register your models here.
from .models import Board,Topic,Post

mod = [Board,Topic,Post]
admin.site.register(mod)