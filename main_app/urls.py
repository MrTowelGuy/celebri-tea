from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('tea/', views.tea_index, name='index'),
  path('tea/<int:tea_id>/', views.tea_detail, name='detail'),
  path('tea/create/', views.TeaCreate.as_view(), name='tea_create'),
  path('tea/<int:pk>/update/', views.TeaUpdate.as_view(), name='tea_update'),
  path('tea/<int:pk>/delete/', views.TeaDelete.as_view(), name='tea_delete'),
]
