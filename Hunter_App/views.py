from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Personal
from .forms import PersonalForm
from django.contrib import messages

#Se esta utilizando el paquete django-widget-tweaks para poder modificar los widgets de los formularios
# Create your views here.
def login_view(request):
    return render(request, 'login.html')
def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context['login_error'] = True

    return render(request, 'login.html', context)

def personal_view(request):
    query = request.GET.get('search')
    if query:
        personal = Personal.objects.filter(nombre__icontains=query)
        if not personal.exists():
            messages.error(request, 'No se encontraron resultados para tu búsqueda.')
    else:
        personal = Personal.objects.all()

    if request.user.is_authenticated:
        # Agregar
        if request.method == "POST" and 'add' in request.POST:
            form = PersonalForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('personal_view')

        # Modificar
        elif request.method == "POST" and 'modify' in request.POST:
            person = get_object_or_404(Personal, id=request.POST.get('id'))
            form = PersonalForm(request.POST, request.FILES, instance=person)
            if form.is_valid():
                form.save()
                return redirect('personal_view')

        # Eliminar
        elif request.method == "POST" and 'delete' in request.POST:
            person = get_object_or_404(Personal, id=request.POST.get('id'))
            person.delete()
            return redirect('personal_view')

        else:
            form = PersonalForm()
    else:
        form = None

    return render(request, 'personal.html', {'personal': personal, 'form': form})