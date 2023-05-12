from django.db import models

ROOM_TYPES = (
    ('AC single' , 'AC single'),
    ('AC double' , 'AC double'),
    ('AC semi suit' , 'AC semi suit'),
    ('AC suit' , 'AC suit'),
    ('Conference Room' , 'Conference Room'),
    ('Party/Dining Hall with catering' , 'Party/Dining Hall with catering'),
    ('Party/Dining Hall without catering' , 'Party/Dining Hall without catering'),
)

GUEST_TYPES = (
    ('Official guest' , 'Official guest'),
    ('Staff guest' , 'Staff guest'),
    ('Normal guest' , 'Normal guest'),
)

class Room(models.Model):
    room_description = models.CharField(max_length=500, default="A nice and comfortable room for you stay")
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES, default='AC single')
    room_count = models.IntegerField(default=0)
    room_booked_count = models.IntegerField(default=0)
    room_image = models.ImageField(upload_to="room_images/", null=True, blank=True)

    @property
    def room_available_count(self):
        return self.room_count - self.room_booked_count

    def __str__(self):
        return self.room_type 
    

class Guest(models.Model):
    guest_name = models.CharField(max_length=20)
    guest_phone = models.CharField(max_length=20)
    guest_email = models.CharField(max_length=20)
    guest_address = models.CharField(max_length=20)
    guest_gender = models.CharField(max_length=10)
    guest_age = models.IntegerField()
    guest_type = models.CharField(max_length=20, choices=GUEST_TYPES, default='Normal guest')

    def __str__(self):
        return self.guest_name
    
class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    room_count = models.IntegerField(default=1)
    check_in = models.DateField()
    check_out = models.DateField(null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.guest.guest_name + " " + self.room.room_type
    
class Img(models.Model):
    image=models.ImageField(upload_to='img/',null=True,default=None)