# views.py
import qrcode
import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from users.models import CustomUsers
from .forms import GamerForm
from django.contrib import messages

import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import qrcode
from qrcode.image.pure import PymagingImage
from .models import CustomUsers  # Make sure to import your model

def generate_qr_code(request, username):
    user_profile = get_object_or_404(CustomUsers, user__username=username)

    # Add user details to the QR code
    data = f"User: {user_profile.gamers.username}\nEmail: {user_profile.gamers.email}"

    # Calculate the time countdown
    game_hours = timezone.now() + timezone.timedelta(minutes=30)
    data += f"\nExpires: {game_hours.strftime('%Y-%m-%d %H:%M:%S')}"

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white", image_factory=PymagingImage)

    # Return the image directly as an HTTP response
    response = HttpResponse(img, content_type="image/png")
    return response
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import qrcode
from qrcode.image.pure import PymagingImage
from .models import CustomUsers  # Make sure to import your model

def generate_qr_code(request):


    # Calculate the time countdown
    game_hours = timezone.now() + timezone.timedelta(minutes=30)

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white", image_factory=PymagingImage)

    # Return the image directly as an HTTP response
    response = HttpResponse(img, content_type="image/png")
    return response


def gaming(request):
    if request.method == 'POST':
        form = GamerForm(request.POST)
        if form.is_valid():
            user = request.user
            game_hours = form.cleaned_data['game_hours']*200
            form.save()
            messages.success(request, f'{user.username}, Your request has been submitted!')
            return redirect("generate_qr_code", username=user.username, game_hours=game_hours)
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = GamerForm()

    return render(
        request=request,
        template_name="qr_code/gamer.html",
        context={"form": form}
    )





    
