from django.shortcuts import render

# Create your views here.
def create(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('author'))
        print(request.POST.get('rating'))
    return render(request,'create.html')

def list(request):
    books_list={
        'books':[
    {
        'title':'Origin',
        'author':'Dan Brown',
        'rating' : '6/10',
        'success': False,
        'img': 'origin.jpeg'
    },{
        'title':'Angels and Demons',
        'author':'Dan Brown',
        'rating' : '9/10',
        'success': True,
        'img': 'angels.jpg'
    }
    ,{
        'title':'Percy Jackson and the Sea of monsters',
        'author':'Rick Riordan',
        'rating' : '8.5/10',
        'success': True,
        'img': 'percy.jpg'
    },{
        'title':'Harry Potter and the Chamber of Secrets',
        'author':'JK Rowling',
        'success': True,
        'img': 'harry.jpg'
    }]}
    return render(request,'list.html',books_list)

def edit(request):
    return render(request,'edit.html')

def menu(request):
    return render(request, 'menu.html')
