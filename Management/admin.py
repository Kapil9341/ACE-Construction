from django.contrib import admin
from .models import ProjectDetail, ContactDetail, Publication, Project, ProjectImage, IndexDetail, CarrerDetail


# Register your models here.


class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ['get_project_title', 'get_project_location', 'area']  # Adjusted list display fields

    def get_project_title(self, obj):
        return obj.project.title

    def get_project_location(self, obj):
        return obj.project.location

    get_project_title.short_description = 'Project Title'  # Custom column header for project title


class ContactDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']


class CarrerDetailAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'mobile']


admin.site.register(ProjectDetail, ProjectDetailAdmin)
admin.site.register(ContactDetail, ContactDetailAdmin)
admin.site.register(Publication)
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(IndexDetail)
admin.site.register(CarrerDetail, CarrerDetailAdmin)
