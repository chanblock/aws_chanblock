from corporate import views
from django.urls import include, path


urlpatterns = [
     path('', views.home),
     path('services', views.services, name="services"),
     path('regulation', views.regulation, name="regulation"),
     path('education', views.education, name="education"),
     path('monitoring', views.monitoring, name="monitoring"),
     path('monitorMtGox', views.monitorMtGox, name="monitorMtGox"),
     path('register_email', views.register_email, name='register_email'),
]