from django.contrib import admin
from .models import Milestone , Goal ,Domain , Group ,Project
# Register your models here.
admin.site.register(Goal)
admin.site.register(Milestone)
admin.site.register(Domain)

admin.site.register(Group)
admin.site.register(Project)

