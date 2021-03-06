from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars_index, name='index'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='detail'),
    path('guitars/<int:guitar_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('guitars/<int:guitar_id>/add_photo/', views.add_photo, name='add_photo'),
    path('guitars/<int:guitar_id>/assoc_strap/<int:strap_id>/', views.assoc_strap, name='assoc_strap'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('straps/', views.StrapList.as_view(), name='straps_index'),
    path('straps/<int:pk>/', views.StrapDetail.as_view(), name='straps_detail'),
    path('straps/create/', views.StrapCreate.as_view(), name='straps_create'),
    path('straps/<int:pk>/update/', views.StrapUpdate.as_view(), name='straps_update'),
    path('straps/<int:pk>/delete/', views.StrapDelete.as_view(), name='straps_delete'),
]