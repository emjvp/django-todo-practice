from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import View

from todo.models import Todo

from django.http import *

# from .forms import TodoForm

# Create your views here.
# def home(request):
#     todos = Todo.objects.all()
#     context = {
#         "todos": todos
#     }
#     return render(request, 'todo_list.html', context)

# def agregar(request):
#     if request.method == "POST":


class TodoListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'todo_list': Todo.objects.all()
        }
        return TemplateResponse(request, 'todo_list.html', context)


class TodoAddView(View):
    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, 'todo_add.html', {})
    
    def post(self, request, *args, **kwargs):
        description = request.POST['description']
        Todo.objects.create(description=description)
        return HttpResponseRedirect('/')


class TodoDoneView(View):
    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['todo_id'])
        todo.is_done = True
        todo.save()
        return HttpResponseRedirect('/')


class TodoEditView(View):
    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['todo_id'])        

        context = {
            'todo': todo
        }        
        
        return TemplateResponse(request, 'todo_edit.html', context)


    def post(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['todo_id'])        
        todo.description = request.POST['description']
        
        if 'is_done' in request.POST:
            todo.is_done = True
        else:
            todo.is_done = False
        todo.save()    
        import pdb; pdb.set_trace()  
        return HttpResponseRedirect('/')


class TodoDeleteView(View):
    def get(self, request, *args, **kwargs):
        todo = Todo.objects.get(id=kwargs['todo_id'])        
        todo.delete()
        return HttpResponseRedirect('/')




