from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View 
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from .models import Family, Task, Transaction, Assignment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import SignUpForm




# Create your views here.

def login_view(request):
    # if POST, then authenticate the user (submitting the username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: # it was a get request so send the emtpy login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




class Landing_Page(TemplateView): 
    template_name = 'landing_page.html'

class Dashboard(TemplateView): 
    template_name = 'dashboard.html'



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


class Task_Create(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'amount', 'duedate', 'description', 'task_status', 'task_approval', 'user']
    template_name = "task_create.html"
    success_url = '/'
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
    fields = ['name', 'amount', 'duedate', 'description', 'task_status', 'task_approval', 'transactions']
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



class Transaction_Create(CreateView):
    model = Transaction
    fields = '__all__'
    template_name = "transaction_create.html"
    success_url = '/transactions'



class Transaction_Update(UpdateView):
    model = Transaction
    fields = ['amount', 'date']
    template_name = "transaction_update.html"
    success_url = '/transactions'



class Transaction_Delete(DeleteView):
    model = Transaction
    template_name = "transaction_confirm_delete.html"
    success_url = '/transactions'



class Family_List(TemplateView):
    template_name = 'familylist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context['families'] = Family.objects.filter(name_icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['families'] = Family.objects.all()
            context['header'] = "My Family Members" # this is where we add the key into our context object for the view to use
        return context 


class Family_Create(LoginRequiredMixin, CreateView):
    model = Family
    fields = ['name', 'description']
    template_name = "family_create.html"
    success_url = '/families'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/families')

   

class Family_Detail(DetailView): 
    model = Family
    template_name="family_detail.html"

class Family_Update(UpdateView):
    model = Family
    fields = ['name', 'description']
    template_name = "family_update.html"
    def get_success_url(self):
        return reverse('family_detail', kwargs={'pk': self.object.pk})

class Family_Delete(DeleteView):
    model = Task
    template_name = "family_delete_confirmation.html"
    success_url = "/families/"

