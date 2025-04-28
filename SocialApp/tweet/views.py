from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, userRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import login 


# Create your views here.
def index(request):
    return render(request,'index.html')

def tweetList(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request ,'tweet_list.html',{'tweets':tweets})

@login_required
def tweetCreate(request):
    # We are checking whether their is post request if yes then form is create by user or filled
    if request.method == "POST":
        # taking request and files
        form = TweetForm(request.POST,request.FILES)
        # std method for valid form
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save() 
            return redirect("tweetList")
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form': form})

@login_required
def tweetEdit(request,tweet_id):
        tweet = get_object_or_404(Tweet,pk=tweet_id, user= request.user)  
        if request.method=='POST':
            form = TweetForm(request.POST,request.FILES,instance=tweet)
            if form.is_valid():
                 tweet = form.save(commit=False)
                 tweet.user = request.user
                 tweet.save()
                 return redirect("tweetList")
        else:
             form = TweetForm(instance=tweet)
        return render(request,'tweet_form.html',{'form': form})

# login required is decorator
@login_required
def tweetDelete(request,tweet_id):
     tweet = get_object_or_404(Tweet,pk=tweet_id,user = request.user)
     if request.method == 'POST':
        tweet.delete()
        return redirect("tweetList")
     return render(request,'tweet_confirm_delete.html',{'tweet': tweet})
    
def Register(request):
    if request.method=='POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweetList')
    else:
        form = userRegistrationForm()
    return render(request,'registration/register.html',{'form':form})