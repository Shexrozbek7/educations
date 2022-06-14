from django.urls import path, include, re_path
# import routers
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from .views import (
    AllDataAPIView,
    ResearchAPIView,
    ProductionAPIView,
    ProtectAPIView,
    PHenologyAPIView,
    PhotoUpdateAPIView,
    PhotoAllAPIViews,
    NoteUpdateAPIView
)

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used

app_name = 'research'

urlpatterns = [
    path('', include(router.urls)),
    re_path(r"^alldata/$",AllDataAPIView.as_view()),
    path("research/<int:pk>/",ResearchAPIView.as_view()),
    path("product/<int:pk>/",ProductionAPIView.as_view()),
    path("protect/<int:pk>/",ProtectAPIView.as_view()),
    path("phenology/<int:pk>/",PHenologyAPIView.as_view()),
    re_path(r"^photo/$",PhotoAllAPIViews.as_view()),
    path("photo/<int:pk>/",PhotoUpdateAPIView.as_view()),

    path("note/<int:pk>/",NoteUpdateAPIView.as_view())
   
   
]
