from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import ProjectDetail, ContactDetail, IndexDetail, Project, ProjectImage, CarrerDetail
from .telegramBot import TelegramBot
from django.http import HttpResponse

# Create your views here.

contact_chat_id = '-4146585983'  # for testing channel
access_token = '7459531611:AAHwEHH-vfatCOgCpdPYSeuzAKc1PB2_EQI'  # for testing channel


class IndexListView(ListView):
    template_name = 'index.html'
    model = IndexDetail
    context_object_name = 'index_data'


class ProjectListView(ListView):
    model = Project
    template_name = 'project.html'
    context_object_name = 'projects'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        queryset = Project.objects.filter(category=slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for project in context['projects']:
            project.project_details = project.projectdetail_set.all()  # Fetch related ProjectDetail instances

            # Fetch the first image for each project
            project.image_url = None
            for detail in project.project_details:
                images = detail.images.all()
                if images:
                    project.image_url = images[0].image.url
                    break

            # Additional context for title and location
            project.title = project.title
            project.location = project.location

        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.get_object()
        project_details = project.projectdetail_set.all()
        context['project_details'] = project_details
        return context


class AboutView(ListView):
    template_name = 'about.html'

    def get_queryset(self):
        # Since there's no specific model, return an empty list or None
        return []


class ThankyouView(TemplateView):
    template_name = 'thank_you.html'

    
class ContactView(TemplateView):
    template_name = 'contact.html'
    model = ContactDetail

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")
        if name and email and subject and message:  # Check if all fields are filled
            data = ContactDetail(name=name, email=email, subject=subject, message=message)
            data.save()
            message = (
                f"name: {name}\n"
                f"email: {email}\n"
                f"subject: {subject}\n"
                f"message: {message}"
            )

            TelegramBot(contact_chat_id, access_token).sendMessage(message)
            return redirect('/thank_you')
            # return redirect('/')  # Redirect to a success page or any other page
        return render(request, self.template_name, {'error': 'All fields are required.'})


class CarrerView(TemplateView):
    template_name = 'contact.html'
    model = CarrerDetail

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        mobile = request.POST.get("mobile", "")
        subject = request.POST.get("subject", "")
        resume = request.FILES.get('resume')
        photo = request.FILES.get('photo')
        if name and email and subject and mobile:  # Check if all fields are filled
            data = CarrerDetail(name=name, email=email, subject=subject, mobile=mobile, resume=resume, photo=photo)
            data.save()
            message = (
                f"name: {name}\n"
                f"email: {email}\n"
                f"subject: {subject}\n"
                f"message: {mobile}"
            )

            TelegramBot(contact_chat_id, access_token).sendMessage(message)
            return redirect('/thank_you')
            # return redirect('/')  # Redirect to a success page or any other page
        return render(request, self.template_name, {'error': 'All fields are required.'})
