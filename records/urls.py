from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentRecordViewSet, login_view

router = DefaultRouter()
router.register(r'student-records', StudentRecordViewSet)

urlpatterns = [
    path('login/', login_view),
]

urlpatterns += router.urls