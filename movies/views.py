from django.shortcuts import render

def index(request):
    return render(request, "movies/index.html", {})

def about(request):
    return render(request, "movies/about.html", {
        "movies": [
            "fight club",
            "The dark knight",
            "The amazing spider man"
        ]
    })
