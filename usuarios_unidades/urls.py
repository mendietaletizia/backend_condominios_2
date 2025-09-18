from django.urls import path
from .views import (UserListCreateView, UserRetrieveUpdateDeleteView, UserRoleListView, UserRoleUpdateView,ResidenteListCreateView, ResidenteRetrieveUpdateDeleteView, UnidadListCreateView,
    UnidadRetrieveUpdateDeleteView)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDeleteView.as_view(), name='user-detail'),
    path('roles/', UserRoleListView.as_view(), name='role-list'),
    path('roles/<int:pk>/', UserRoleUpdateView.as_view(), name='role-update'),
    path('residentes/', ResidenteListCreateView.as_view(), name='residente-list-create'),
    path('residentes/<int:pk>/', ResidenteRetrieveUpdateDeleteView.as_view(), name='residente-detail'),
    path('unidades/', UnidadListCreateView.as_view(), name='unidad-list-create'),
    path('unidades/<int:pk>/', UnidadRetrieveUpdateDeleteView.as_view(), name='unidad-detail'),
]
