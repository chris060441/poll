from django.urls import path
from .views import * 

urlpatterns = [
    # path('poll/',views.poll_list),
    path('pollz/', views.PollList.as_views()),
    path('poll/<int:pk>/',PollDetail.as_view()),
    path('option/<int:oid>/', PollVote.as_view()),
]
