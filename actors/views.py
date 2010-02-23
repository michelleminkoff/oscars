from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from oscars.actors.models import Actor

def index(request):
    latest_actor_list = Actor.objects.all().order_by('actor_last')[:5]
    return render_to_response('actors/index.html', {'latest_actor_list': latest_actor_list})

def detail(request, id):
    try:
        p = Actor.objects.get(pk=id) 
    except Actor.DoesNotExist:
        raise Http404
    return render_to_response('actors/detail.html', {'actor': p})

def children(request):
    start_age = 10
    end_age = 19
    latest_10actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_10.html', {'latest_10actor_list': latest_10actor_list})

def twenties(request):
    start_age = 20
    end_age = 29
    latest_20actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_20.html', {'latest_20actor_list': latest_20actor_list})

def thirties(request):
    start_age = 30
    end_age = 39
    latest_30actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_30.html', {'latest_30actor_list': latest_30actor_list})

def fourties(request):
    start_age = 40
    end_age = 49
    latest_40actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_40.html', {'latest_40actor_list': latest_40actor_list})

def fifties(request):
    start_age = 50
    end_age = 59
    latest_50actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_50.html', {'latest_50actor_list': latest_50actor_list})

def sixties(request):
    start_age = 60
    end_age = 69
    latest_60actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
    return render_to_response('actors/decade_60.html', {'latest_60actor_list': latest_60actor_list})

def seventies(request):
   start_age = 70
   end_age = 79
   latest_70actor_list = Actor.objects.filter(award_age__range=(start_age,end_age)).order_by('-award_age')[:50]
   return render_to_response('actors/decade_70.html', {'latest_70actor_list': latest_70actor_list})

def browse_age(request):
	return render_to_response('actors/browse_age.html')

def browse_name(request):
    latest_actor_name_list = Actor.objects.all().order_by('actor_last')[:100]
    return render_to_response('actors/browse_name.html', {'latest_actor_name_list': latest_actor_name_list})