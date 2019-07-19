from django.urls import path
from . import views

# urlpatterns的成员不与demo文件夹下的html页面对应，而是与view.py的函数对应
urlpatterns = [
    path('index/', views.index), # 记录子路径
    # path('index2/', views.index2), # 记录子路径
    # path('edit/', views.edit),
    # path('edit/edit_action', views.edit_action), # 这里的edit_action对应edit.html页面中form表单的name值，二者必须相同
]