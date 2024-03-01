from django.shortcuts import render,redirect

from .forms import CreateUserForm, LoginForm
# Create your views here.
def home(request):
 return render(request,'webapp/index.html')



# Register
def register(request):
    
    form = CreateUserForm()
    if request.method == "Post":
        form = CreateUserForm(request.post)
        if form.is_valid():
            form.save()
            # return redirect('')
            
    context = {'form':form}
    return render(request,'webapp/register.html',context=context)