from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django.contrib import messages

cred = credentials.Certificate(r"C:\Users\dhruv\PycharmProjects\TheDeigningSphere\thedesigningsphere\designing_sphere\cred.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
def home(request):
    return render(request, "home.html")
def contact(request):
    return render(request, "contact.html")
def graphic(request):
    return render(request, "graphic.html")
def dhruv(request):
    return render(request, "dhruv.html")
def project(request):
    return render(request, "project.html")
def gautam(request):
    return render(request, "gautam.html")
def team(request):
    return render(request, "team.html")
def teaser(request):
    return render(request, "teaser.html")
def surabhi(request):
    return render(request, "surabhi.html")
def samyak(request):
    return render(request, "samyak.html")
def dandiya(request):
    return render(request, "dandiya.html")
def carnival(request):
    return render(request, "carnival.html")
def ram(request):
    return render(request, "ram.html")
def reel(request):
    return render(request, "reel.html")
def dm(request):
    return render(request, "dm.html")
def gm(request):
    return render(request, "gm.html")
def cgi(request):
    return render(request, "CGI.html")
def submit_query(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        # Add data to Firestore
        doc_ref = db.collection('queries').add({
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone,
            'query': query
        })

        # Add success message
        messages.success(request, 'Data inserted successfully!')

        # Redirect to home page or any other page
        return redirect('home')

    return render(request, 'contact_us.html')