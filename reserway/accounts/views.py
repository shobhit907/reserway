from django.shortcuts import render,redirect
from .forms import BookingAgentForm,ExtendedUserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=ExtendedUserCreationForm(request.POST)
        booking_agent_form=BookingAgentForm(request.POST)

        if form.is_valid() and booking_agent_form.is_valid():
            user=form.save()
            booking_agent=booking_agent_form.save(commit=False)
            booking_agent.user=user
            booking_agent.save()
            login(request,user)
            return redirect('bookings:home')
        return render(request,'accounts/signup.html',{'form':form,'booking_agent_form':booking_agent_form})
    else:
        form=ExtendedUserCreationForm()
        booking_agent_form=BookingAgentForm()
        return render(request,'accounts/signup.html',{'form':form,'booking_agent_form':booking_agent_form})