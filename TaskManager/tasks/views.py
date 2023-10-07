from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list-task')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list-task')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


@login_required(login_url='/login/') 
def Edit_Info(request, pk): 
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list-task')
    else:
        form = TaskForm(instance=task)

    context = {'task': task, 'form': form}
    return render(request, 'edit_task.html', context)

@login_required(login_url='/login/') 
def Delete_Info(request, pk):
    student = Task.objects.get(pk=pk)
    student.delete()

    return redirect('list-task')



def add_task_form(request):
    context = request.user.id
    print(context)
    return render(request, 'task_form.html', {'user': context})
