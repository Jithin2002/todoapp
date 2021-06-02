from django.shortcuts import render,redirect
from todoapp.forms import TodoCreateForm
from todoapp.models import Todos


# Create your views here.

def create_todo(request):
    if request.method=="GET":
        form=TodoCreateForm()
        context={}
        context["form"]=form
        return render(request,"createtodo.html",context)
    elif request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todo=Todos(task_name=taskname,status=status,user=user)
            todo.save()
            print(taskname,user,status)
            return render(request,"index.html")
def list_all_todos(request):
    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listalltodos.html",context)
def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("list")
def index(request):
    return render(request,"index.html")
def update_todo(request,id):
    todo=Todos.objects.get(id=id)
    dict={
        "task_name":todo.task_name,
        "user":todo.user,
        "status":todo.status
    }
    form=TodoCreateForm(initial=dict)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            task_name=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todo.task_name=task_name
            todo.user=user
            todo.status=status
            todo.save()
            return redirect("list")
    return render(request,"updatetodo.html",context)


