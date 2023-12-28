from django.shortcuts import render
from Service.models import TicketIpek, TicketOnur
from random import randint
# Create your views here.

def IndexDion_Contact (request) : 
    return render(request,'contact.html')
    
def IndexDion_Photography (request) : 
    return render(request,'photography.html')

def IndexDion (request) : 
    return render(request,"dion_index.html")

def HomeIndex (request) : 
    return render(request,"index.html")
def IndexIpek (request) : 
    return render(request,"ipek_index.html")

def Ticket (request) : 
    ticket_name = request.POST.get('name')
    ticket_email = request.POST.get('email')
    ticket_subject =  request.POST.get('subject')
    ticket_message = request.POST.get('message')
    ticket_order = randint(0,99999)
    create_new_ticket = TicketIpek(name=ticket_name,order=ticket_order,email=ticket_email,subject=ticket_subject,message=ticket_message)
    create_new_ticket.save()
    context = {'bilet_numarasi' : ticket_order}
    return render(request,'ticket.html',context=context)

def Ticket_Onur (request) : 
    ticket_name = request.POST.get('name')
    ticket_email = request.POST.get('email')
    layer1 = request.POST.get('layer1')
    layer2 = request.POST.get('layer2')
    layer3 = request.POST.get('layer3')
    ticket_order = randint(0,99999)
    create_new_ticket = TicketOnur(name=ticket_name,order=ticket_order,email=ticket_email,kutu=f"{layer1} \n {layer2} \n {layer3}"
    )
    create_new_ticket.save()
    context = {'bilet_numarasi' : ticket_order}
    return render(request,'ticket.html',context=context)