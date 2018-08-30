from django import forms

from eventapp.models import MyEvent,OrderDetail



class DateInput(forms.DateInput):
    input_type = 'date' 

class OnlineForm(forms.ModelForm):
	class Meta:
		model=MyEvent
		exclude = ('created_date','booking_date','event_date',)
		widgets = {
            
            'event_date': DateInput(),
        }

class OrderForm(forms.ModelForm):
	class Meta:
		model=MyEvent
		exclude = ('created_date',)
		widgets = {
	           
	        'event_date': DateInput(),
	  
	    }

