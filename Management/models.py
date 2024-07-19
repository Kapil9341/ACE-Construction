from django.db import models


# Create your models here.

class IndexDetail(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='homeImage/')

    def __str__(self):
        return self.title


from django.db import models


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('architecture', 'Architecture'),
        ('interior', 'Interior'),
        ('design', 'Design'),
        ('planning', 'Planning'),
        ('renovation', 'Renovation'),
    ]
    client_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.client_name}-{self.title}-{self.category}-{self.location}"


class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    date = models.DateField()
    project_detail = models.TextField()

    def __str__(self):
        return f"{self.project.client_name}-{self.project.title}-{self.project.category}-{self.project.location}-{self.area}"


class ProjectImage(models.Model):
    project_detail = models.ForeignKey(ProjectDetail, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProjectImage/')

    def __str__(self):
        return f"{self.project_detail.project.client_name}-{self.project_detail.project.title}-{self.project_detail.project.category}-{self.project_detail.project.location}-{self.project_detail.area}"

    # class Meta:
    #     db_table = 'ProjectDetail'

    # def __str__(self):
    #     return f"{self.title}' - '{self.location}"


class ContactDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}'-'{self.subject}"


class CarrerDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    mobile = models.IntegerField()
    resume = models.FileField(upload_to='resumes/')
    photo = models.ImageField(upload_to='resume/photo/')

    def __str__(self):
        return f"{self.name}'-'{self.subject}-{self.mobile}"


class Publication(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='publication/')
    media_link = models.URLField()
    video_link = models.URLField()

    def __str__(self):
        return self.title
