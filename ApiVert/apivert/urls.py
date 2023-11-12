from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from textrovertapp.views import *
from textrovertapp import views


router = routers.SimpleRouter()
router.register('all', ApiVertViewSet)
router.register('anger', AngerTemplateView)
router.register('birthday', BirthdayTemplateView)
router.register('happy', HappyTemplateView)
router.register('sad', SadTemplateView)
router.register('fear', FearTemplateView)
router.register('love', LoveTemplateView)
router.register('help', HelpTemplateView)
router.register('surprise', SurpriseTemplateView)



urlpatterns = [
    path('superdo', admin.site.urls),
    path('', include(router.urls)),
    path('', views.home, name='home')


]
