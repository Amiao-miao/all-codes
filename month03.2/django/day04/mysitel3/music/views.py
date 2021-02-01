from django.shortcuts import render

# Create your views here.
def music_view(request):
    return render(request,'music/index.html')