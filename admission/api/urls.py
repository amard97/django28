from django.urls import path,include
from admission.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('curd',views.UserViewSet)

urlpatterns = [
    path('',include(router.urls)),

]