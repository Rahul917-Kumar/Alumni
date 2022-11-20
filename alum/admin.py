from django.contrib import admin
from .models import PersonDetails, PastCompanies_AndPosition, Current_WorkProfile, CollegeProfile, ConnectHandles
# Register your models here.

admin.site.register(PersonDetails)
admin.site.register(ConnectHandles)
admin.site.register(PastCompanies_AndPosition)
admin.site.register(Current_WorkProfile)
admin.site.register(CollegeProfile)
