from django.contrib import admin
from .models import *


admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)