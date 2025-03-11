from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from students.models import Classroom
from .models import Message

def chat_room(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    return render(request, "chat/chat_room.html", {"classroom": classroom})

def delete_message(request, message_id):
    if request.method == "POST":
        message = get_object_or_404(Message, id=message_id)
        if request.user == message.user:  # Only allow the sender to delete
            message.delete()
            return JsonResponse({"success": True, "message_id": message_id})
        else:
            return JsonResponse({"error": "You can only delete your own messages"}, status=403)
    return JsonResponse({"error": "Invalid request"}, status=400)
