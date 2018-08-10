from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as Superuser
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from skywalker.models import User
from skywalker.models import Turma
from skywalker.models import Matricula

from skywalker.forms import UserRegistrationForm
from skywalker.forms import EditUserForm
from skywalker.forms import EditTeamForm
from skywalker.forms import TeamRegistrationForm
"""""""""""""""
    LOGIN
"""""""""""""""

def login_view(request):
    if request.method == 'GET':
        return render(request, 'skywalker/login_form.html', {})
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)

        if user is not None:
            #request.session['user'] = user
            request.session['user_name'] = user.username
            request.session['user_id'] = user.id
            login(request, user)
            lista = User.objects.all()
            return redirect(index_users)
        else:
            return HttpResponse("Seu nome de usuário e senha não conferem!")


"""""""""""""""
 CRUD PESSOAS
"""""""""""""""

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            siap = userObj['siap']
            nivel = userObj['nivel']
            categoria = userObj['categoria']
            
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = User.objects.create(username=username, email=email, siap=siap, nivel=nivel, categoria=categoria)
                user.save()
                return redirect(index_users)
            else:
                return HttpResponse('Parece que um usuário com este email ou username já existe')
    else:
        return render(request, 'skywalker/register001.html', {})


def index_users(request):
    if request.method == 'GET':
        query = request.GET.get('search_by', None)
        
        if query is None:
            #user_id = request.session['user_id']
            lista = User.objects.all()
            #user = User.objects.get(id=user_id)
            return render(request, 'skywalker/my_services.html', {'lista': lista})
        else:
            lista = User.objects.filter(username__icontains=query)
            return render(request, "skywalker/my_services.html", {'lista': lista})


def edit_user(request, pk):
    instance = User.objects.get(id=pk)
    if request.method == 'GET':
        return render(request, "skywalker/edit_service.html", {'instance': instance})
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(index_users)
        else:
            return HttpResponse('Algo deu errado')

def delete_user(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect(index_users)

"""""""""""""""
 CRUD TURMAS
"""""""""""""""

def register_team(request):
    #user = request.session.get('user_id', '')
    user_id = request.session['user_id']
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            teamObj = form.cleaned_data
            nome = teamObj['nome']
            idioma = teamObj['idioma']
            responsavel = Superuser.objects.get(id=user_id)
            team = Turma.objects.create(nome=nome, responsavel=responsavel, idioma=idioma)
            team.save()
            return redirect(index_people, pk=team.codigo)
        else:
            return HttpResponse('Algo deu errado')
    else:
        return render(request, 'skywalker/register_team.html', {'lista': User.objects.all()})


def index_teams(request):
    if request.method == 'GET':
        query = request.GET.get('search_by', None)
        
        if query is None:
            #user_id = request.session['user_id']
            lista = Turma.objects.all()
            return render(request, 'skywalker/my_teams.html', {'lista': lista})
        else:
            lista = Turma.objects.filter(nome__icontains=query)
            return render(request, "skywalker/my_teams.html", {'lista': lista})


def index_people(request, pk):
    turma = Turma.objects.get(codigo=pk)

    if request.method == 'GET':
        query = request.GET.get('search_by', None)
        if query is None:
            users = User.objects.all()
            lista = User.objects.filter(matriculado=False)
            #user = User.objects.get(id=user_id)
            return render(request, 'skywalker/people_list.html', {'lista': lista, 'turma': turma})
        else:
            lista = User.objects.filter(username__icontains=query)
            return render(request, "skywalker/people_list.html", {'lista': lista, 'turma': turma})

def add_person(request, id, codigo):
    user = User.objects.get(id=id)
    turma = Turma.objects.get(codigo= codigo)
    matricula = Matricula.objects.create(aluno=user, turma=turma)
    matricula.save()
    user.matriculado = True;
    user.save()
    return redirect(index_people, pk=codigo)

def edit_team(request, pk):
    instance = Turma.objects.get(codigo=pk)
    lista = Matricula.objects.filter(turma=instance)
    if request.method == 'GET':
        return render(request, "skywalker/edit_team.html", {'instance': instance, 'lista': lista})
    if request.method == 'POST':
        form = EditTeamForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(index_teams)
        else:
            return HttpResponse('Algo deu errado')

def delete_team(request, pk):
    turma = Turma.objects.get(codigo=pk)
    matriculados = Matricula.objects.filter(turma=turma)
    for user in matriculados:
        user.matriculado = False
    turma.delete()
    return redirect(index_teams)

def delete_subscriber(request, id, codigo):
    user = User.objects.get(id=id)
    turma = Turma.objects.get(codigo=codigo)
    matricula = Matricula.objects.get(aluno=user, turma=turma)
    matricula.delete()
    user.matriculado = False
    user.save()
    return redirect(edit_team, pk=codigo)
    

"""""""""""""""
 CRUD IDIOMAS
"""""""""""""""

"""""""""""""""
   ERROR 404
"""""""""""""""
def error404(request):
    return render(request, "skywalker/404Error.html", {})

"""""""""""""""
   LOGOUT
"""""""""""""""

def logout_view(request):
    logout(request)
    return redirect(login_view)

