"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contenido import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursos/crear/', views.crear_curso, name='crear_curso'), 
    path('cursos/editar/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),


]


if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)