from django.shortcuts import render , redirect , get_object_or_404

# Create your views here.
from .models import TweetModel
from .forms import TweetForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from django.contrib.auth import login , logout

def index(request):
    return render(request,'base.html')

def tweet_list(request):
    tweets = TweetModel.objects.all().order_by('-created_at')
    context ={'tweets':tweets}
    return render(request , 'all_tweet.html',context)


@login_required
def AddTweet(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES)  #request.FILES : for img
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweet')
    context =  {'form':form} 
    return render(request,'add_tweet.html',context)


@login_required
def updateTweet(request,id):
    tweet = get_object_or_404(TweetModel , pk = id , user = request.user)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        form =TweetForm(request.POST, request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('all_tweet')
    return render(request,'add_tweet.html',{'form':form})
 
 
@login_required   
def deleteTweet(request , id ):
    tweet = get_object_or_404(TweetModel , pk = id , user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('all_tweet')
    return render(request,'del_conf.html')


def registration(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('all_tweet')       
    context = {'form':form}
    return render(request,'registration/register.html',context)


from django.contrib.auth.forms import AuthenticationForm
def loginView(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('all_tweet')
    context = {'form':form}
    return render(request,'registration/login.html',context)


def logoutView(request):
    if request.method == "POST":
        logout(request)
        return redirect('all_tweet')
    return render(request,'registration/logged_out.html')