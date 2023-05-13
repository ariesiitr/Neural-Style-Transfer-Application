from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
import os
from PIL import Image
import torchvision.transforms as transforms
import torch
from myapp.nst import generate_image


def home(request):
    return render(request, 'index.html')


# def result(request):
#     if request.method == 'POST' and 'content' in request.FILES and 'style' in request.FILES:
#         content_img = request.FILES['content']
#         style_img = request.FILES['style']
#
#         # Check if the uploaded files are valid images
#         try:
#             Image.open(content_img)
#             Image.open(style_img)
#         except:
#             return HttpResponseBadRequest('Invalid image(s)')
#
#         # Generate the output image using the NST model
#         out_img = generate_image(content_img, style_img)
#
#         print('ashishs')
#         # Save the output image to a temporary file
#         out_img_path = os.path.join('myapp', 'static', 'images', 'out.jpg')
#         out_img.save(out_img_path)
#
#         # Return the output image as a response
#         with open(out_img_path, 'rb') as f:
#             response = HttpResponse(f.read(), content_type='image/jpeg')
#         response['Content-Disposition'] = 'inline; filename="out.jpg"'
#         return response
#
#     else:
#         return HttpResponseBadRequest('Invalid request')

import time

def result(request):
    if request.method == 'POST' and 'content' in request.FILES and 'style' in request.FILES:
        content_img = request.FILES['content']
        style_img = request.FILES['style']

        print('okworks')

        #
        # # Check if the uploaded files are valid images
        try:
            Image.open(content_img)
            Image.open(style_img)
        except:
            return HttpResponseBadRequest('Invalid image(s)')

        # Generate the output image using the NST model
        out_img = generate_image(content_img, style_img)
        #
        # # Save the output image to a temporary file
        out_img_path = os.path.join('myapp', 'static', 'images', 'out.jpg')
        out_img.save(out_img_path)

        # Wait for the output image to be available
        while not os.path.isfile(out_img_path):
            time.sleep(1)

        # Return the output image as a response
        with open(out_img_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='image/jpeg')
        response['Content-Disposition'] = 'inline; filename="out.jpg"'
        return response
        return render(request, 'index.html')
    else:
        return HttpResponseBadRequest('Invalid request')