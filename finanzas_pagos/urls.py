from django.urls import path
from .views import GastoListCreateView, GastoRetrieveUpdateDeleteView

urlpatterns = [
    path("gastos/", GastoListCreateView.as_view(), name="gasto-list-create"),
    path("gastos/<int:pk>/", GastoRetrieveUpdateDeleteView.as_view(), name="gasto-detail"),
]
