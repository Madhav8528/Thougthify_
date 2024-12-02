from django.shortcuts import render,redirect
from .models import createthought
from .forms import ThoughtForm, RegisterationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def thought(request):
    return render(request, 'index.html')


def thought_list(request):
   thoughts = createthought.objects.all().order_by("-uploaded_at")
   return render(request,"thought_list.html",{'thoughts':thoughts})

@login_required
def create_thought(request):
    if request.method=='POST':
      form = ThoughtForm(request.POST,request.FILES)
      if form.is_valid():
         thought = form.save(commit=False)
         thought.user = request.user
         thought.save()
         return redirect('thought_list')
    else:
       form = ThoughtForm()
    return render(request,"thought_form.html",{'form':form}) 
@login_required
def edit_thought(request, thought_id):
   thought = get_object_or_404(createthought,pk=thought_id,user=request.user)

   if request.method == "POST":
      form = ThoughtForm(request.POST,request.FILES,instance=thought)
      if form.is_valid():
         thought = form.save(commit=False)
         thought.user = request.user
         thought.save()
         return redirect('thought_list')
   else:
      form = ThoughtForm(instance=thought)
   return render(request,"thought_form.html",{'form':form})

@login_required
def thought_delete(request,thought_id):
   thought = get_object_or_404(createthought,pk=thought_id,user=request.user)

   if request.method == "POST":
      thought.delete()
      return redirect('thought_list')
   return render(request,"thought_delete.html",{'thought':thought})

def register(request):
   if request.method=='POST':
     form = RegisterationForm(request.POST)
     if form.is_valid():
       user = form.save(commit=False)
       user.set_password(form.cleaned_data['password1'])
       user.save()
       login(request,user)
       return redirect('thought_list')
   else:
      form = RegisterationForm()
   return render(request,"registration/register.html",{'form' : form})