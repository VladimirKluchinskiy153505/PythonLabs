from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

from gym.forms import RegistrationForm, LoginForm
from gym.models import Master, Lesson, ClubCard


def index(request):
    masters = Master.objects.all()
    context = {
        'masters': masters
    }
    return render(request=request, template_name='gym/index.html',context=context)
def cards_view(request):
    cards = ClubCard.objects.all()
    context = {
        'cards': cards
    }
    return render(request=request, template_name='gym/clubcard_list.html', context=context)
def pageNotFound(request ,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            subject_name = form.cleaned_data['subject_name']
            email = form.cleaned_data['email']
            photo = form.cleaned_data['photo']
            password = form.cleaned_data['password']
            # Check if the user already exists
            if Master.objects.filter(username=username).exists():
                messages.error(request, 'User already exists.')
                return redirect('registration')
            # Create and save the user to the database
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            master = Master(username=username, subject_name= subject_name, email=email, photo=photo, password=password, user=user)
            master.save()
            # Redirect the user to a success page or login page
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'gym/registration.html', {'form': form})
def login(request):
    return HttpResponse('Login')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username =username, password=password)
            if user is not None:
                if user.is_superuser:
                    admin_url = reverse('admin:index')  # Replace 'admin:index' with the actual URL pattern for the admin panel
                    return redirect(admin_url)
                else:
                    masters = Master.objects.all()
                    context={'mastername': username,
                             'masters':masters}
                    return render(request,template_name='gym/index.html',context=context) #Replace home
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'gym/login.html', {'form': form})
def lesson_list(request):
    # Get filter parameters from the request GET parameters
    subject_name = request.GET.get('subject_name')
    lesson_price_higher = request.GET.get('lesson_price_higher')
    lesson_price_lower = request.GET.get('lesson_price_lower')

    # Apply filters based on the provided parameters
    lessons = Lesson.objects.all()
    subject_name_choices = Lesson.objects.values_list('subject_name', flat=True).distinct()
    if subject_name:
        lessons = lessons.filter(subject_name=subject_name)
    if lesson_price_higher:
        lessons = lessons.filter(lesson_price__gte=lesson_price_higher)
    if lesson_price_lower:
        lessons = lessons.filter(lesson_price__lte=lesson_price_lower)

    context = {
        'lessons': lessons,
        'subject_name_choices': subject_name_choices,
    }
    return render(request, 'gym/lesson_list.html', context)
def master_list(request):
    masters = Master.objects.all()
    context = {
        'masters': masters
    }
    return render(request, 'gym/master_list.html', context)
def lessons_for_current_master(request, username):
    master = Master.objects.get(username=username)
    related_lessons = master.lesson_set.all()
    context = {
        'lesson_list': related_lessons,
    }
    return render(request,'gym/lessons_for_current_user.html',context=context)

