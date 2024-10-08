from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/<int:pk>/delete', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
                  path('subscription/', SubscriptionView.as_view(), name='subscription'),
              ] + router.urls
