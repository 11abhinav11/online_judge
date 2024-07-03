from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import problem
from django.forms import formset_factory
from .forms import add_problem as adding_problem, add_test as adding_test, question_form


def problems(request):
    Probs = problem.objects.all().values()
    user = request.user
    group = False
    if user.groups.filter(name='Admin').exists():
        group = True
    if request.user.is_authenticated:
        return render(request, 'problems_list.html', {'problems': Probs, 'group': group})
    else:
        return render(request, 'problems_list.html', {'problems': Probs, 'group': group})


def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='Admin').exists():
            Probs = problem.objects.all().values()
            return render(request, 'dashboard.html', {'problems': Probs})
    else:
        redirect("index")


def add_problem(request):
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                prob = adding_problem(request.POST)
                if prob.is_valid():
                    obj = prob.save()
                    return redirect("test/"+str(obj.Problem_ID))
            else:
                prob = adding_problem()
            return render(request, 'add_problem.html', {'form': prob})
        else:
            return redirect("index")
    else:
        return redirect("index")


def add_test(request, id):
    if (problem.objects.filter(Problem_ID=id).count() == 0):
        return HttpResponseRedirect('/error')
    if request.user.is_authenticated:
        user = request.user
        if user.groups.filter(name='Admin').exists():
            if request.method == 'POST':
                test_case = adding_test(request.POST)
                if test_case.is_valid():
                    obj = test_case.save(commit=False)
                    obj.Problem_ID = problem.objects.get(Problem_ID=id)
                    obj.save()
                    return HttpResponseRedirect(request.path_info)
            else:
                test_case = adding_test()
            return render(request, 'add_test.html', {'form': test_case})
        else:
            return redirect("index")
    else:
        return redirect("index")


def solve(request, id):
    question = problem.objects.get(Problem_ID=id)
    if request.user.is_authenticated:
        form = question_form(request.POST)
        return render(request, 'question.html', {'form': form, 'question': question})
    else:
        form = question_form()
        return render(request, 'question.html', {'form': form, 'question': question})
