from django.shortcuts import render

# Import models
from .models import Comment

# Create your views here.
def index(request):
  comments = Comment.objects.order_by('-date_added')
  context = {'comments' : comments}
  return render(request, 'guestbook/index.html', context)

def sign(request):
  return render(request, 'guestbook/sign.html')