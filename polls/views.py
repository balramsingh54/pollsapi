'''
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Poll
# Create your views here.
def polls_list(request):
	MAX_OBJECTS=20
	polls=Poll.objects.all()[:MAX_OBJECTS]
	data={"results": list(polls.values("question", "created_by__username", "pub_date"))}

	return JsonResponse(data)


def polls_detail(request):
	poll = get_object_or_404(Poll, pk=pk)
	data=data = {"results": { 
	"question": poll.question, 
	"created_by": poll.created_by.username, 
	"pub_date": poll.pub_date 
	}}
	return JsonResponse(data)
	'''

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer

class PollList(APIView):
	def get(self, request):
		polls = Poll.objects.all()[:20]
		data = PollSerializer(polls, many=True).data
		return Response(data)



class PollDetail(APIView):
	def get(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		data = PollSerializer(poll).data
		return Response(data)