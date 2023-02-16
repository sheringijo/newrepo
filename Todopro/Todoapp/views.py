
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.utils.decorators import method_decorator
from Todoapp.decorators import login_required
from .models import Task

#create your views here.
@method_decorator(login_required,name="dispatch")
class Home(TemplateView):
     template_name="index.html"
     def get(self, request):
        name = Task.objects.filter(user=self.request.user)
        task_id=request.GET.get('id','')
        task_action=request.GET.get('action','')
        if task_id !="" or task_action!="":
            task_obj=Task.objects.get(id=task_id)
            if task_action=='delete':
                task_obj.delete()
            elif task_action=='done':
                task_obj.isCompleted=True
                task_obj.save() 
            elif task_action=='undo':
                task_obj.isCompleted=False
                task_obj.save()   
            return redirect('home')    

        return render(request, self.template_name, {'name': name})
     def post(self,request):
          title=request.POST.get('title')
          id=request.POST.get('task-id')
          if Task.objects.filter(user=request.user,title=title).exists():
              messages.info(request,"task already exists")
              return redirect('home')
          if id:
            data=Task.objects.get(id=id)
            data.title=title
            data.save()
          else:
            Task.objects.create(title=title,user=request.user)
          return redirect('home')
     
class Signup(TemplateView):
    template_name="signup.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    def post(self,request):
        username1=request.POST['username']
        email1=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'enterd username is already use')
                return render(request,'signup.html')
            if User.objects.filter(email=email1).exists():
                messages.info(request,'enterd email is already use')
                return render(request,'signup.html')
            else:       
             user=User.objects.create_user(username=username1,email=email1,password=password1)
             user.save()
            print('user created')
            return redirect('login')
        else:
          return render(request,'signup.html')
    

class Loginuser(TemplateView):
    template_name="login.html"
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated:
           return redirect('home')
        return super().dispatch( request,*args,**kwargs)  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self,request):
        username1=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=username1,password=pwd)
        if user is not None:
            auth.login(request,user) 
            return redirect('home')
        else:
             messages.info(request, 'username or password is incorrect')
             return redirect('login')  

@login_required  
def logout(request):
    auth.logout(request)
    return redirect('login')   
  

  

   