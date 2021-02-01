from django.shortcuts import render


def test_cors(request):
    return render(request,'test_cors.html')