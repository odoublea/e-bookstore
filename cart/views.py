from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Book

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html', {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        book = get_object_or_404(Book, id=book_id)
        cart.add(book=book, qty=book_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        cart.delete(book=book_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_id = int(request.POST.get('bookid'))
        book_qty = int(request.POST.get('bookqty'))
        cart.update(book=book_id, qty=book_qty)

        cartqty = cart.__len__()
        cartsubtotal = cart.get_subtotal_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': cartsubtotal})
        return response


