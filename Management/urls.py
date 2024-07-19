from django.contrib import admin
from django.urls import path
from .views import IndexListView, ContactView, ProjectListView, AboutView, ProjectDetailView, CarrerView, ThankyouView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('carrer/', CarrerView.as_view(), name='carrer'),
    path('project/<str:slug>/', ProjectListView.as_view(), name='project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('thank_you/', ThankyouView.as_view(), name='thankyou'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)