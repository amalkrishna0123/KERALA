from django.shortcuts import render

def Index(request):
    return render(request, "index.html")  # Changed from "myapp/index.html" to "index.html"

def About(request):
    return render(request, "about-us.html")

def Projects(request):
    return render(request, "projects.html")

def Services(request):
    return render(request, "services.html")

def Packages(request):
    return render(request, "packages.html")

def Blog(request):
    return render(request, "blog.html")

def Contact(request):
    return render(request, "contact-us.html")

    