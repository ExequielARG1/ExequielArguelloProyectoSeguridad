from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Personal
from .forms import PersonalForm
from django.contrib import messages

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

def index_view(request):
    return render(request, 'index.html')

def personal_view(request):
    query = request.GET.get('search')
    if query:
        personal = Personal.objects.filter(nombre__icontains=query)
        if not personal.exists():
            messages.error(request, 'No se encontraron resultados para tu búsqueda.')
    else:
        personal = Personal.objects.all()

    form = None
    person_id = None

    try:  # Manejo básico de errores
        if request.user.is_authenticated:
            person_id = request.POST.get('id')

            if request.method == "POST":
                if 'add' in request.POST:
                    form = PersonalForm(request.POST, request.FILES)
                    if form.is_valid():
                        form.save()
                        return redirect('personal_view')

                elif 'modify' in request.POST and person_id:
                 person = get_object_or_404(Personal, id=person_id)
                 form = PersonalForm(request.POST, request.FILES, instance=person)
                 if form.is_valid():
                    form.save()
                    return redirect('personal_view')
                 
                elif 'delete' in request.POST:
                    person = get_object_or_404(Personal, id=person_id)
                    person.delete()
                    return redirect('personal_view')

                else:
                    form = PersonalForm()
            else:
                form = PersonalForm()

        else:
            form = None

    except Exception as e:
        messages.error(request, f"Ocurrió un error: {e}")

    return render(request, 'personal.html', {'personal': personal, 'form': form, 'person_id': person_id})
