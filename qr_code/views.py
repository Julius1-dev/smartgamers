import qrcode
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from .forms import GamerForm
from django.contrib import messages
from django.http import HttpResponse
import qrcode
from qrcode.image.pure import PymagingImage

def generate_qr_code(request):
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
        user=request.user
        form = GamerForm(request.POST)
        if form.is_valid():
            game_hours = form.cleaned_data['game_hours']*200
            form.save()
            messages.success(request, f'{user.username}, Your request has been submitted!')
            return redirect("generate_qr_code", game_hours=game_hours)
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





    
