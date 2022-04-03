from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View 
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from .models import Task, Transaction



# Create your views here.


class Landing_Page(TemplateView): 
    template_name = 'landing_page.html'



class Task_List(TemplateView):
    template_name = 'tasklist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context['tasks'] = Task.objects.filter(name_icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['tasks'] = Task.objects.all()
            context['header'] = "Daily Tasks" # this is where we add the key into our context object for the view to use
        return context


class Task_Create(CreateView):
    model = Task
    fields = ['name', 'amount', 'duedate', 'status', 'user']
    template_name = "task_create.html"
    # success_url = "/tasks/"
    # def get_success_url(self):
    #     return reverse('task_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/tasks')
   

class Task_Detail(DetailView): 
    model = Task
    template_name="task_detail.html"

class Task_Update(UpdateView):
    model = Task
    fields = ['name', 'amount', 'duedate', 'status', 'user']
    template_name = "task_update.html"
    # success_url = "/tasks/"
    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

class Task_Delete(DeleteView):
    model = Task
    template_name = "task_delete_confirmation.html"
    success_url = "/tasks/"


def profile(request, username):
    user = User.objects.get(username=username)
    tasks = Task.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'tasks': tasks})



# Transactions view function

def transactions_index(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_index.html', {'transactions': transactions})

def transactions_show(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    return render(request, 'transaction_show.html', {'transaction': transaction})


# django auth
def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
                    return HttpResponseRedirect('/login')
            else:
                print('The username and/or password is incorrect.')
                return HttpResponseRedirect('/login')
    else: # it was a get request so send the empty login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/landing_page')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/'+str(user.username))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})