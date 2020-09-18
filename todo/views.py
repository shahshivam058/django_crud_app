from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from .forms import Todo_form

# Create your views here.
# views are used for handing the request it handle request and execute business logic as well as retuen response
def todo_list(request):
    todos = todo.objects.all()
    context = {
        "todos" : todos
    }
    return render(request,"index.html",context)

def todo_detail(request,id):
    todo_item = todo.objects.get(id=id)
    context = {
        "todo_item" : todo_item
    }
    return render(request,"todo_detail.html",context)

def todo_create(request):
    form  = Todo_form(request.POST or None)
    if form.is_valid():
        # name = form.cleaned_data['name']
        # due_date = form.cleaned_data['due_date']
        # todo_form = todo.objects.create(name = name,due_date = due_date)
        # todo_form.save()
        form.save()
        return redirect("/")
    context = {
        "form" : form
    }
    return render(request,"todo_create.html",context)

def todo_update(request,id):
    todo_item = todo.objects.get(id=id)
    form = Todo_form(request.POST or None,instance=todo_item)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {
        "form" : form
    }
    return render(request,"todo_update.html",context)

def todo_delete(request,id):
    todo_item = todo.objects.get(id=id)
    todo_item.delete()
    return redirect("/")

    

