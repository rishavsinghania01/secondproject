from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def setBook(request):
    if request.method=='POST':
        data=json.loads(request.body)
        bookid=data.get('bookid')
        title=data.get('title')
        price=data.get('price')

        # do something with the data, like storing in database
        print('Received: ',bookid,title,price)
        return JsonResponse({'message':'Data received successfully'},status=200)
    return JsonResponse({'error':'Invalid Request'},status=400)
def getBooks(request):
    #list of dict
    books=[
        {'bookid':1,'title':'Python','price':456.0},
        {'bookid':2,'title':'CSS','price':250.0},
        {'bookid':3,'title':'HTML','price':375.0},
        {'bookid':4,'title':'JavaScript','price':680.0},
        {'bookid':5,'title':'Django','price':900.0},
    ]
    return JsonResponse(books,safe=False)

