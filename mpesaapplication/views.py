from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
# Create your views here.
def index(request):
    cl= MpesaClient()
    phone_number = '0115007958'
    amount= 1
    account_reference= 'reference'
    transaction_desc ='description'
    callback_url = 'http://darajambili.herokuapp.com/express-payment'
    response = cl.stk_push(phone_number,amount,account_reference,transaction_desc)
    return HttpResponse(response)
def stk_push_callback(request):
    data = request.body
    return HttpResponse('STK Push in Django')