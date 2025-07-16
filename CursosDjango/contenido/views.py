from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso
from .forms import CursoForm

# Create your views here.

def principal(request):
    cursos = Curso.objects.all()
    return render(request, "contenido/principal.html", {"cursos": cursos})

def contacto(request):
    return render(request,"contenido/contacto.html")

def cursos(request):
    return render(request, "contenido/cursos.html")


def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('Principal')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'contenido/editar_curso.html', {'form': form, 'curso': curso})

def eliminar_curso(request, curso_id):
    curso = get_object_or_404(Curso, pk=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('Principal')
    return render(request, 'contenido/eliminar_curso.html', {'curso': curso})
