from django.urls import path
from myApi import views

urlpatterns = [
    path('contact/', views.contact_list),
    path('contactdetails/<int:pk>/', views.contact_detail),
    path('product/', views.product_list),
    path('order/', views.OrderList.as_view()),
    path('snippet/', views.SnippetList.as_view()),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view()),
]