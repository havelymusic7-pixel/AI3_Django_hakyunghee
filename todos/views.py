from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.all()
    progress_todos = todos.filter(is_in_progress=True)
    waiting_todos = todos.filter(is_in_progress=False, is_completed=False)
    return render(
        request,
        "todos/todo_list.html",
        {
            "progress_todos": progress_todos,
            "waiting_todos": waiting_todos,
        },
    )


def todo_create(request):
    form = TodoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todos:list")
    return render(
        request,
        "todos/todo_form.html",
        {"form": form, "page_title": "할 일 등록"},
    )


def todo_update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("todos:list")
    return render(
        request,
        "todos/todo_form.html",
        {"form": form, "page_title": "할 일 수정"},
    )


@require_POST
def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed
    todo.save(update_fields=["is_completed"])
    return redirect("todos:list")


@require_POST
def todo_start(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_in_progress = True
    todo.save(update_fields=["is_in_progress"])
    return redirect("todos:list")


@require_POST
def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("todos:list")
