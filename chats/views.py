from django.shortcuts import render
def chats_list(request):
    return render(request, "chats/chats_list.html", {})

# Create your views here.
