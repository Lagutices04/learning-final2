from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='task_completed'),
    path('create/', views.create_task, name='create_task'),
    #path('create/<int:course_id>/', TaskCreationView.as_view(), name='create_task_with_course'),
    path('calificar_tarea/', views.calificar_tarea, name='calificar_tarea'),
    path('create_nota/', views.create_nota, name='create_nota'),
    path('lista/notas/', views.lista_notas, name='lista_notas'),
    path('<int:task_id>/nota_detail/', views.nota_detail, name='nota_detail'),
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('notas/<int:nota_id>/', views.nota_detail, name='nota_detail'),
    path('notas/<int:nota_id>/complete/', views.complete_nota, name='complete_nota'),
    path('notas/<int:nota_id>/delete/', views.delete_nota, name='delete_nota'),
    path('complete/', views.tasks_completed2, name='task_completed_2'),
    path('nota/', views.nota, name='notas'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Django pueda servir los archivos estáticos 

     
   


