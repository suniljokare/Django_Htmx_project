from .forms import RegisterForm, ExpenseForm
from .models import Expense

from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy,reverse

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from django.views.generic import FormView, RedirectView,TemplateView
import datetime



class SignupView(FormView):
    template_name = 'signup2.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)

# class CustomerLoginView(LoginView):
#     template_name = 'login.html'
#     fields = '__all__'
#     redirect_authenticated_user = True

#     def get_success_url(self):
#         return reverse_lazy('homepage')

class CustomerLoginView(View):
    
    def get(self,*args,**kwargs):
        form = AuthenticationForm()
        return render(self.request, 'login2.html',{'form':form})

    def post(self,request,*args,**kwargs):
        fm = AuthenticationForm(request, data=request.POST)
        
        if fm.is_valid():
            umail = fm.cleaned_data.get('username')
            upass = fm.cleaned_data.get('password')
            user = authenticate(username=umail,password=upass)

            if user is not None or user.is_superuser==True:
                login(self.request, user)
                messages.success(request,f'welcome  {user.first_name} !!!!!!')
                return redirect('homepage')

            else:
                messages.error(request,"Invalid username or password.")
        return render(request, 'login2.html',{'form':fm})


class LogoutView(RedirectView):
    url = '/'
    def get(self, request):
        logout(request)
        return super(LogoutView, self).get(request)


class AddExpenseView(LoginRequiredMixin,FormView):
    template_name = 'add2.html'
    form_class = ExpenseForm
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        fm = form.save(commit=False)
        fm.user =self.request.user
        fm.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class DisplayExepsneView(ListView):
    template_name = 'display.html'
    context_object_name = 'expenses'
    paginate_by = 3

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user.id)    


class SearchView(View):

    def get(self, request):
        search_term = request.GET.get('search', None)
        if search_term:
            expenses =Expense.objects.filter(ename__icontains=search_term,user=request.user.id).all()
            template = 'search_results.html'
        else:
            expenses = Expense.objects.all()
            template = 'display.html'

        return render(request, template_name=template,context={'expenses': expenses})


class UpdateExepenseView(View):
    def get(self,id):
        instance = Expense.objects.get(id=id)
        form = ExpenseForm(instance=instance)
        context = {'form':form,'instance':instance }
        return render(self.request, 'edit2.html', context)


    def post(self,id):
        instance = Expense.objects.get(id=id)
        form = ExpenseForm(self.request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('display')


class DeleteExpenseView(DeleteView):
    model = Expense
    template_name = 'delete.html'
    success_url = 'display'




def today(request):
    expenses = Expense.objects.filter(date=datetime.date.today())

    total = 0
    for expense in expenses:
        total+=expense.eamount

    return render(request, 'today.html',{'expenses':expenses,'total':total})


def month(request):
    expenses = Expense.objects.filter(date=datetime.now().month)

    total = 0
    for expense in expenses:
        total+=expense.eamount

    return render(request, 'today.html',{'expenses':expenses,'total':total})


def year(request):
    expenses = Expense.objects.filter(date=datetime.now())

    total = 0
    for expense in expenses:
        total+=expense.eamount

    return render(request, 'today.html',{'expenses':expenses,'total':total})


def home(request):
    fm = RegisterForm()
    return render(request, 'home.html', {'form':fm})

def limit(request):
    return render(request, 'limit.html')


def update(request,id):
    instance = Expense.objects.get(id=id)
    form = ExpenseForm(request.POST or None,request.FILES or None,instance=instance)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
        return redirect('display')
    
    return render(request, 'edit2.html',{'form':form,'instance':instance })


  




