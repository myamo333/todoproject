# kanban/views.py

from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # ここを修正
    return render(request, 'kanban/index.html', {'tasks': tasks, 'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 追加されたタスクを表示するページにリダイレクト
    # POSTリクエスト以外の場合や、フォームが無効な場合は何もしない

@csrf_exempt
def update_task(request, task_id):
    if request.method == 'PUT':
        task = Task.objects.get(pk=task_id)
        new_status = request.body.decode('utf-8')
        task.status = new_status
        task.save()
        return JsonResponse({'message': 'Task status updated successfully.'})