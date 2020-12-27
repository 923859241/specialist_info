from django.contrib import admin
from Specialist.models import SpecialistCategory
from Specialist.models import Specialist
from Specialist.models import UserInfo
from Specialist.models import Project
from Specialist.models import ProjectSpecialist
from Specialist.models import SchoolList
from Specialist.models import Studentlist

# Register your models here.
admin.site.register(SpecialistCategory)
admin.site.register(Specialist)
admin.site.register(UserInfo)
admin.site.register(Project)
admin.site.register(ProjectSpecialist)
admin.site.register(SchoolList)
admin.site.register(Studentlist)
