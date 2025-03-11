from django.urls import path
from .views import chat_room, delete_message

urlpatterns = [
    path("<int:class_id>/", chat_room, name="chat_room"),
    path("delete/<int:message_id>/", delete_message, name="delete_message"),  # New delete URL
]