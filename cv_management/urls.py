from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('setQuestion/<int:test_id>', setQuestions),
    path('getQuestion/<int:test_id>', getMultipleChoice),
    path('getAttempts/<int:user_id>', getAttempts),
    # path('addRequirement', addRequirement),
    # path('getRequirements/<int:vac_id>', getRequirements),
    path('setAnswer/<int:seeker_id>', setAnswer),
    path('insertTest', InsertTest),
    path('getTests', GetTests),
    # path('vacancyInfo/<int:vac_id>', VacancyInfo),
    # path('addDefaultQuestion', DefaultQuestion),
]
