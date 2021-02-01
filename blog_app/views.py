from django.shortcuts import render

posts = [
    {
       'autor': 'Jorge Jesus',
       'titulo': 'post 1',
       'conteudo': 'primeiro post com conteudo',
       'data_postada': '28 de Janeiro, 2021'
    },
    {
       'autor': 'Abel Ferreira',
       'titulo': 'post 2',
       'conteudo': 'segundo post com conteudo',
       'data_postada': '02 de Fevereiro, 2021'
    },
    
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog_app/home.html', context)

def about(request):
    return render(request, 'blog_app/about.html')