# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,render_to_response, redirect
from django.views.generic import CreateView,View
from django.contrib.auth.models import User

from eventapp.forms import OnlineForm,OrderForm,DateInput
from eventapp.models import MyEvent,OrderDetail




class AdminView(View):
	template_name='adminhome.html'
	def get(self,request):
		if request.user.is_superuser:
			return render(request,self.template_name)

class EventView(View):
    template_name = 'eventcreate.html'
    form_class = OnlineForm
    def get(self,request):
        if request.user.is_superuser:
            form  = self.form_class()
            context={
                'form':form
            }
            return render(request,self.template_name,context)
        else:
            return redirect('/login/')

    def post(self,request):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            print('Valid !')
            form.save()
            context = {
                'form':form,
                'success':"saved successfully"
            }
            return redirect('/list/')

        else:
            print('Invalid !')
            context = {
                'form':form
            }
            return render(request,self.template_name,context)


class ListEvent(View):
	template_name = 'listevent.html'
	def get(self,request):
		if request.user.is_superuser:
			data = MyEvent.objects.all()
			context={
				'data' :data
			}
			return render(request,self.template_name,context)

class EditEvent(View):
	template_name = 'editevent.html'
	form_class = OnlineForm

	def get(self,request,pk):
		if request.user.is_superuser:
			event_id = pk
			event_obj = MyEvent.objects.get(id=event_id)
			form = OnlineForm(
				initial={
				'event_type':event_obj.event_type,
				'event_name':event_obj.event_name,
				'pic':event_obj.pic,
				'rate':event_obj.rate,
			
				}
			)
			context = {
				'form': form
			}
			return render(request,self.template_name,context)

	def post(self,request,pk):
		event_id = pk
		form = OnlineForm(request.POST,request.FILES)
		edit_event =MyEvent.objects.get(id=event_id)
		print(edit_event)
		if form.is_valid():

			print "valid"
			edit_event.event_type = str(request.POST.get('event_type'))
			edit_event.event_name =str(request.POST.get('event_name'))
			edit_event.pic =request.FILES.get('pic')
			edit_event.rate =str(request.POST.get('rate'))
			
			
			edit_event.save()
			
			context = {
			'form': form
			}
			return redirect('/list/')
		else:
			print "not valid",form.errors
			context = {
			'form':form
			}
			return render(request,self.template_name,context)

class BookEvent(View):
	template_name = 'book.html'
	def get(self,request):
		if request.user.is_staff:
			data = MyEvent.objects.all()
			context={
				'data' :data
			}
			return render(request,self.template_name,context)

class Order(View):
	template_name = 'ordr.html'
	form_class = OrderForm

	def get(self,request,pk):
		if request.user.is_staff:
			event_id = pk
			event_obj = MyEvent.objects.get(id=event_id)
			form = OrderForm()
			context = {
				'form': form,
				'event_type':event_obj.event_type,
				'event_name':event_obj.event_name,
				'pic':event_obj.pic,
				'rate':event_obj.rate,
			
			}
			return render(request,self.template_name,context)


	

	def post(self, request,pk):
		event_id=pk
		form = OrderForm(request.POST)
		model=MyEvent
		print(request)
		event_obj = MyEvent.objects.get(id=event_id)
		# if form.is_valid():
		print("eeee")
		log_user=request.user
		
		s_date = str(request.POST.get('event_date'))
		s_booked_by = User.objects.get(username=log_user)
		sobj = OrderDetail.objects.create(event_type=event_obj.event_type,event_name=event_obj.event_name,event_date=s_date,booked_by=s_booked_by)
		sobj.save()
		
		return redirect('/book/')

		