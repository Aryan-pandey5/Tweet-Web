from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('all/',views.tweet_list,name='all_tweet'),
    path('form/',views.AddTweet,name='add_data'),
    path('delete/<int:id>/',views.deleteTweet,name='tweet_delete'),
    path('edit/<int:id>/',views.updateTweet,name='tweet_edit'),
    
    path('registration/',views.registration,name='register'),
    path('accounts/login/',views.loginView , name='login'),
    path('logout/',views.logoutView , name='LogOut')
]
