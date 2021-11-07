from django.urls import path
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view, registerPage, loginPage, logoutUser


app_name = 'tests'

urlpatterns = [
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),

    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]