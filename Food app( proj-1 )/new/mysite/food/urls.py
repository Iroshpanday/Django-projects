from.import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # path('', views.null,name='null'),
    #/food/hello
    path('', views.IndexClassView.as_view(),name='index'),
    #/food/id(1/2/else)
    path('<int:pk>/',views.FoodDetail.as_view(),name='details'),
    path('item/', views.item,name='item'),
    #add item
    path('add', views.create_item,name='create_item'),
    #edit
    path('update/<int:id>/', views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/', views.delete_item,name='delete_item'),
    
    
]