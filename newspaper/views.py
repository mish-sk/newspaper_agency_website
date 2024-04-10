from django.shortcuts import render


def index(request):
    context = {

    }
    return render(
        request,
        "newspaper/index.html",
        context=context
    )
