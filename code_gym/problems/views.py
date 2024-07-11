from django.shortcuts import render, redirect
from pathlib import Path
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import problem, save_code as code_save, User, test_cases, submission
from user.models import user as user_model
from django.forms import formset_factory
from .forms import add_problem as adding_problem, add_test as adding_test, question_form
import uuid
import sys
import os
import subprocess


def problems(request):
    Probs = problem.objects.all().order_by('-date')
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
            Probs = problem.objects.all().values().order_by('-time_stamp')
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


def parsed_string(str1):
    string = ""
    for line in str1.split('\n'):
        string = string + line + "\\n"
    string = string[0:-2]
    return string


def solve(request, id):
    problem_obj = problem.objects.get(Problem_ID=id)
    project_path = Path(settings.BASE_DIR)
    if request.user.is_authenticated:
        user = request.user
        user_obj = User.objects.get(id=request.user.id)
        sub = submission.objects.filter(
            User_ID=user_obj, Problem_Id=problem_obj).order_by('-time_stamp')
        if (code_save.objects.filter(Problem_Id=problem_obj, User=user_obj).exists()):
            obj = code_save.objects.get(Problem_Id=problem_obj, User=user_obj)
            obj = obj.code
            obj = obj.replace("\\", "&#$%;")
            string = parsed_string(obj)
        else:
            string = ""
        if request.method == 'POST':
            uni = str(uuid.uuid4())
            form = question_form()
            # test code
            if request.POST.get('run'):
                language = request.POST['language']
                code = request.POST['code']
                test = request.POST['test']
                code_runner = executable_file(language, code, uni)
                if code_runner == "Error":
                    output = "Error while compiling code"
                else:
                    output = run_code(language, code_runner, test, uni)
                os.remove(project_path/"codes"/code_runner)
                return render(request, 'question.html', {'form': form, 'question': problem_obj, 'submissions': sub,
                                                         'output': output, 'saved_code': string, 'input': test})
            # submit code
            else:
                language = request.POST['language']
                code = request.POST['code']
                tests = test_cases.objects.filter(Problem_ID=id)
                sub_obj = submission.objects.create(code=code, language=language, Problem_Id=problem_obj,
                                                    User_ID=user_obj)

                code_runner = executable_file(language, code, uni)
                if code_runner == "Error":
                    output = "Error while compiling code"
                else:
                    sub_obj.verdict = "Accepted"
                    for i, test in enumerate(tests):
                        output = run_code(
                            language, code_runner, test.Input, uni)
                        if (output[0:-1] != test.output and output != test.output):

                            sub_obj.verdict = "Wrong answer on Test Case " + \
                                str(i)
                            break
                    if sub_obj.verdict == "Accepted":
                        solved_problems_list = user_model.objects.get(
                            user=user_obj).problems_solved.all()
                        if (problem_obj not in solved_problems_list):
                            user_model.objects.get(
                                user=user_obj).problems_solved.add(problem_obj)
                            problem_obj.solved = int(problem_obj.solved)+1
                            user_model.save()
                            problem_obj.save()
                os.remove(project_path/"codes"/code_runner)
                sub_obj.save()
                return render(request, 'question.html', {'form': form, 'question': problem_obj, 'saved_code': string, 'submissions': sub})
        else:
            form = question_form()
            return render(request, 'question.html', {'form': form, 'question': problem_obj, 'saved_code': string, 'submissions': sub})
    else:
        form = question_form()
        return render(request, 'question.html', {'form': form, 'question': problem_obj})


def save_code(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_obj = User.objects.get(id=request.POST.get('Username', False))
            problem_obj = problem.objects.get(
                Problem_ID=request.POST.get('PID', False))
            obj, created = code_save.objects.get_or_create(
                Problem_Id=problem_obj, User=user_obj)
            obj.code = request.POST.get('code', False)
            obj.save()
            return HttpResponse('')
        return render(request, 'error.html')
    return render(request, 'error.html')


def executable_file(language, code, uni):
    project_path = Path(settings.BASE_DIR)
    dir_path = project_path/"codes"
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
    codes_dir = project_path/"codes"
    code_file_name = f"{uni}.{language}"
    code_file_path = codes_dir/code_file_name
    with open(code_file_path, "w") as code_file:
        code_file.write(code)

    if language == "cpp":
        executable_path = codes_dir/f"{uni}.exe"
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        if compile_result.returncode == 0:
            return executable_path
        else:
            return "Error"
    elif language == "py":
        return code_file_name

    elif language == 'c':
        executable_path = codes_dir/f"{uni}.exe"
        compile_result = subprocess.run(
            ["g++", str(code_file_path), "-o", str(executable_path)]
        )
        os.remove(code_file_path)
        if compile_result.returncode == 0:
            return
        else:
            return "Error"

    elif language == 'js':
        return code_file_name

    return "Error"


def run_code(language, code, input_data, uni):
    project_path = Path(settings.BASE_DIR)
    directories = {"inputs", "outputs"}

    for directory in directories:
        dir_path = project_path/directory
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
    inputs_dir = project_path/"inputs"
    outputs_dir = project_path/"outputs"
    code_dir = project_path/"codes"

    input_file_name = f"{uni}.txt"
    output_file_name = f"{uni}.txt"

    input_file_path = inputs_dir/input_file_name
    output_file_path = outputs_dir/output_file_name
    code_file_path = code_dir/code

    with open(input_file_path, "w") as input_file:
        input_file.write(input_data)

    with open(output_file_path, "w") as output_file:
        pass

    if language == "cpp":
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    [str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    elif language == "py":
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["python3", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )

    elif language == 'c':
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    [str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )
    elif language == 'js':
        with open(input_file_path, "r") as input_file:
            with open(output_file_path, "w") as output_file:
                subprocess.run(
                    ["node", str(code_file_path)],
                    stdin=input_file,
                    stdout=output_file,
                )
    with open(output_file_path, "r") as output_file:
        output_data = output_file.read()
    if output_data == "":
        return "Error"
    os.remove(output_file_path)
    os.remove(input_file_path)
    return output_data
