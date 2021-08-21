from typing import ItemsView
from django.http import request
from django.shortcuts import render,get_object_or_404,redirect
from .models import Contactclass
from django.contrib.auth.decorators import login_required
from .forms import contactform
from django.views.generic.edit import CreateView



# Create your views here.
@login_required
def messages(request):
    all_objects = Contactclass.objects.all()[::-1]
    return render(request, 'contact/allmessage.html',{'objects':all_objects})

@login_required
def messagedetail(request, message_id):
    message = get_object_or_404(Contactclass, pk=message_id)
    return render(request, 'contact/detailmessage.html',{'object':message})

@login_required
def delete_message(request,id):
    message = Contactclass.objects.get(id=id)
    if request.method == 'POST' :
        message.delete()
        return redirect('contact:messages')
    return render(request,'contact/message-delete.html',{'item':message})

# old conctact me code
@login_required
def contactme(request):

    if request.method == 'POST':

        form = contactform(request.POST)

        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
         form = contactform()
    return render(request,'contact/contactme.html',{'form':form})

# class Contactme(CreateView):
#     model = Contactclass
#     fields = ['subject','message']
#     template_name = 'contact/contactme.html'
    
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)