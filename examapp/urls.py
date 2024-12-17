from django.urls import path
from . import views

urlpatterns=[
    path('startTest/',views.startTest),
    path('nextQuetion/',views.nextQuetion),
    path('previousQuetion/',views.previousQuetion),
    path('endexam/',views.endexam),
    path('addQuetion/',views.addQuetion),
    path('viewQuetion/',views.viewQuetion),
    path('updateQuetion/',views.updateQuetion),
    path('deleteQuetion/',views.deleteQuetion),
    path('giveMePage1/',views.giveMePage1),
    path('giveMePage2/',views.giveMePage2),
    path('giveMePage3/',views.giveMePage3),
    path('search/<pageno>',views.search),
    path('search1/',views.search1),
    path('showRemainingTime/',views.showRemainingTime)

]