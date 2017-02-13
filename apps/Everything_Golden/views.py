from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import User, Event, Product
from django.db.models import Q
import datetime
import json
import bcrypt

#CONTROLLER
# Create your views here.

def index(request):
    return render(request, 'Everything_Golden/index.html')
def about(request):
    return render(request, 'Everything_Golden/about.html')
def members(request):
    return render(request, 'Everything_Golden/login.html')
@csrf_exempt
def register(request):
    if request.method == "POST":
        print "Register Method"
        data = json.loads(request.POST.get('form_data'))
        print data
        password = data['member']['password']
        pw_confirmation = data['member']['password_confirmation']
        if password != pw_confirmation:
            print "Passwords Dont Match"
            return redirect('members')
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        if bcrypt.hashpw(password.encode(),pw_hash) == pw_hash:
            user = User.objects.create(first_name = data['member']['first_name'], 
                                last_name = data['member']['last_name'],
                                email = data['member']['email'],
                                age = int(data['member']['age']),
                                password = pw_hash,
                                gender = data['member']['gender'],
                                phone = int(data['member']['phone']),
                                membership_type = data['membershipType']['tier'])
        else:
            print "Failed Authentication"
            return redirect('/')
        if user:
            request.session['id'] = user.id
            print User.objects.filter(first_name=str(user.first_name))
            try:
                return JsonResponse({ 'redirect_to' : 'profile' })
            except:
                print "SMH"
        else:
            print "get" 
            return redirect("/")
def login(request):
    print "Login Method"
    if request.method == 'POST':
        data = request.POST
        user = User.objects.filter(email = data['email'])
        if user:
            print user
            password = data['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            if bcrypt.hashpw(password.encode(),pw_hash) == pw_hash: 
                request.session['id'] = user[0].id
                return redirect('profile')
            else:
                return redirect('/')
    else:
        return redirect('members')
def profile(request):
    try:
        print "Profile Method " + str(request.session['id'])
        user = User.objects.filter(id=request.session['id'])
        user_events = Event.objects.filter(attendee=request.session['id'])
        upcoming_events = Event.objects.filter(~Q(attendee=request.session['id']))
        print user
        return render(request, 'Everything_Golden/profile.html', { 'users' : user, 
                                                                  'events' : user_events, 
                                                                  'upcoming_events' : upcoming_events })
    except:
        return redirect('members')
def merchandise(request):
    return render(request, 'Everything_Golden/merchandise.html')
def schedule(request):
    events = Event.objects.all()
    return render(request, 'Everything_Golden/schedule.html', {'events' : events})
def join_event(request, id):
    if request.method == 'GET':
        return redirect('/')
    else:
        user = User.objects.filter(id=request.session['id'])
        event = Event.objects.filter(id=id)
        if user:
            try:
                print user
                print event
                event[0].attendee.add(user[0])
                return redirect('profile')
            except:
                print "Fail"
                return redirect('/')
        else:
            pass
def logout(request):
    if request.session['id']:
        request.session.clear()
        return redirect('/')
    else:
      return redirect('/')  
def stories(request):
    return render(request, 'Everything_Golden/stories.html')
def contact(request):
    return render(request, 'Everything_Golden/contact.html')


