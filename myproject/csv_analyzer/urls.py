from django.urls import path
from . import views

app_name = 'csv_analyzer'


urlpatterns = [
    path('upload/', views.upload_file, name='upload'),
    path('analyze/<int:file_id>',views.analyze, name = 'analyze'),
]