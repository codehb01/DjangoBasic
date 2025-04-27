from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')

def tweetList(request):
    tweets = Tweet.object.all().order_by('-created_at')
    return render(request ,'tweet_list.html',{'tweets':tweets})

def tweetCreate(request):
    # We are checking whether their is post request if yes then form is create by user or filled
    if request.method == "POST":
        # taking request and files
        TweetForm(request.POST,request.FILES)
        # std method for valid form
        if form.is_valid():
            tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save() 
        return redirect("tweetList")
    else:
        form=TweetForm()
    return render(request,'tweet_form.html',{'form': form})


def tweetEdit(request,tweet_id):
        tweet = get_object_or_404(Tweet,pk=tweet_id, user= request.user)  
        if request.method=='POST':
            form = TweetForm(request.POST,request.FILES,instance=tweet)
        else:
             form = TweetForm(instance=True)
        return render(request,'tweet_form.html',{'form': form})