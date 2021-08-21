from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
 path('',views.messages,name="messages"),
 path('<int:message_id>/', views.messagedetail, name='messagedetail'),
 path('delete/<int:id>',views.delete_message,name="delete_message"),
 path('contactme/',views.contactme,name='contactme'),
]
