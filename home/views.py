from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from .models import Questions, Answere
from django.core.paginator import Paginator
from django.contrib import messages
from . import form


# question = Questions.objects.order_by('-q_number')[:10]

# Create your views here.

def index(request):

    if request.user.is_anonymous:
        return redirect('/login')
    question = Questions.objects.order_by('-q_number')
    paginator = Paginator(question, 10)
    page_number = request.GET.get('page')
    question1 = paginator.get_page(page_number)
    context = {"question": question1}
    
    return render(request, 'index.html', context)

def post_question(request):


    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        user = request.user
        question = request.POST.get("question")
        ques = Questions(user=user, question=question, date = datetime.today())
        print(ques.q_number)
        ques.save()
        return redirect("/")

def postnew(request):
    if request.user.is_anonymous:
        return redirect('/login')
    context = {'name': request.user}
    return render(request, 'askdoubt.html', context)


def log_in(request):
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')




def log_out(request):
    logout(request)
    return redirect('/login')

def reply(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        q_id = request.POST.get('q_id')
        context = {"q_id": q_id}
        return render(request, "reply.html", context)

def postanswere(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        q_id = request.POST.get('q_id')
        answere = request.POST.get('answere')
        user = request.user
        ans = Answere(q_number = q_id, user=user, answere=answere, date=datetime.today())
        ans.save()
        return redirect("/")

def view_reply(request):
    if request.user.is_anonymous:
        return redirect('/login')
    if request.method == "POST":
        q_id = request.POST.get('q_id')
        answere = Answere.objects.filter(q_number = q_id)
        context = {'q_id': q_id,
                   'answere': answere}
        return render(request, "view_reply.html", context)




def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        if pass1 != pass2:
            return HttpResponse("password not same")
        if (email.find("@nitkkr.ac.in") == -1):
            return HttpResponse("Not a nit kurukshetra mail")
        email_exist = User.objects.filter(email=email).exists()
        user_exist = User.objects.filter(username=name).exists()
        if email_exist:
            return HttpResponse("Email already exists")
        if user_exist:
            return HttpResponse("user already exists")
        if not user_exist:
            myuser = User.objects.create_user(username=name, email=email, password=pass1)
            myuser.save()
            messages.success(request, "Your account has been created")
            return redirect("/login")

    return render(request, 'registration.html')


