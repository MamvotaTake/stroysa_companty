from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
from contacts.models import Contact


def inquiry(request):
    if request.method == 'POST':
        house_id = request.POST['car_id']
        user_id = request.POST['user_id']
        house_title = request.POST['house_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(house_id=house_id, user_id=user_id, first_name=first_name, last_name=last_name,
                          house_title=house_title,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone,
                          message=message)

        send_mail(
            'New Car Inquiry',
            f'Here is the message. {house_title} ',
            'EMAIL_HOST_USER',
            ['tooyoungmamvota@gmail.com'],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your message has been submitted, we will get back to you shortly.')
        return redirect('/houses/' + house_id)
