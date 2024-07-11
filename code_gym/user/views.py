from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import signup_form, login_form
from .models import user as user_model, User
from problems.models import submission, problem


def error(request, exception):
    return render(request, 'error.html')


def index(request):
    if request.user.is_authenticated:
        user_obj = User.objects.get(id=request.user.id)
        user = user_model.objects.get(user=user_obj)
        lang_dict = {'cpp': 0, 'c': 0, 'py': 0, 'js': 0}
        submission_list = submission.objects.filter(
            User_ID=user_obj, verdict="Accepted").order_by('-time_stamp')
        solved_list = user.problems_solved.all()
        diff = {'Hard': 0, 'Easy': 0, 'Medium': 0}
        tag_context = {'Array': 0, 'Linked_List': 0, 'Hash_Table': 2, 'Stack': 2, 'Dynamic_Programming': 0,
                       'Backtracking': 0, 'Binary_Search': 0,
                       'String': 0, 'Sorting': 0, 'Greedy': 4, 'Matrix': 3}
        for prob in submission_list:
            lang_dict[prob.language] += 1
            diff[prob.Problem_Id.difficulty] += 1
        for prob in solved_list:
            for tag in prob.problem_tags.split():
                tag_context[tag] += 1
        return render(request, 'index.html', {'profile': user, 'langs': lang_dict, 'problems': submission_list, 'diff': diff, 'tag': tag_context})
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            user_obj = form.save()
            user_model.objects.create(user=user_obj, rating=100).save()
            return redirect('login')
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = signup_form()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('index')
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = login_form()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')
