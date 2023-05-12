from django.shortcuts import render
from .models import Room, Guest, Booking, Img, GUEST_TYPES

def index_base(request):
    return render(request,'index_base.html',{})
def index_office(request):
    return render(request,'index_office.html',{})
def index_rules(request):
    return render(request,'index_rules.html')
def index_about(request):
    return render(request,'index_about.html')
def index_gallery(request):
    images=Img.objects.all()
    context={'gallery':images}
    return render(request,'index_gallery.html',context)

def booking(request):
    if request.method == "GET":
        room_type = request.GET.get('room_type')
        room = Room.objects.get(room_type=room_type)
        return render(request, 'booking.html', {
            'booked' : False,
            'room': room,
            'guest_types' : [x[0] for x in GUEST_TYPES]
        })
    else:
        guest_type = request.POST.get('guest_type')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        room_type = request.POST.get('room_type')
        room_count = request.POST.get('room_count')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')

        guest = Guest.objects.create(
            guest_name=name,
            guest_email=email,
            guest_phone=phone,
            guest_address=address,
            guest_gender = gender,
            guest_age = age,
            guest_type = guest_type
        )
        guest.save()

        room = Room.objects.get(room_type=room_type)
        room.room_booked_count += int(room_count)
        room.save()

        price = get_room_price(room_type, guest_type) * int(room_count)

        booking = Booking.objects.create(
            guest=guest,
            room=room,
            room_count=room_count,
            check_in=check_in,
            check_out=check_out,
            price = price
        )
        booking.save()

        return render(request, 'booking.html', {
            'room_count': room.room_count,
            'booked' : True,
        })

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {
        'rooms' : rooms
    })


def get_room_price(room_type, guest_type):
    price = 0
    if room_type == 'AC single':
        if guest_type == 'Official guest':
            price = 700
        elif guest_type == 'Staff guest':
            price = 700
        elif guest_type == 'Normal guest':
            price = 1000
    elif room_type == 'AC double':
        if guest_type == 'Official guest':
            price = 700
        elif guest_type == 'Staff guest':
            price = 1000
        elif guest_type == 'Normal guest':
            price = 1200
    elif room_type == 'AC semi-suit':
        if guest_type == 'Official guest':
            price = 800
        elif guest_type == 'Staff guest':
            price = 1000
        elif guest_type == 'Normal guest':
            price = 1500
    elif room_type == 'AC suit':
        if guest_type == 'Official guest':
            price = 1500
        elif guest_type == 'Staff guest':
            price = 2000
        elif guest_type == 'Normal guest':
            price = 2500
    elif room_type == 'Conference Room':
        if guest_type == 'Official guest':
            price = 2000
        elif guest_type == 'Staff guest':
            price = 2000
        elif guest_type == 'Normal guest':
            price = 3000
    elif room_type == 'Party/Dining Hall with catering':
        if guest_type == 'Official guest':
            price = 3000
        elif guest_type == 'Staff guest':
            price = 3000
        elif guest_type == 'Normal guest':
            price = 3000
    elif room_type == 'Party/Dining Hall without catering':
        if guest_type == 'Official guest':
            price = 5000
        elif guest_type == 'Staff guest':
            price = 5000
        elif guest_type == 'Normal guest':
            price = 5000
    
    
    return price