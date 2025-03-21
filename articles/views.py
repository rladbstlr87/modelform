from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)

def create(request):
    # new/ => 빈 종이를 보여주는 기능
    # create/ => 사용자가 입력한 데이터 저장
    # ================================
    # GET create/
    # POST create/

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    # 1. GET 요청    
    else:
        # 2. 비어있는 form을 만든다
        form = ArticleForm()
    # 3. context dict에 비어있는 form을 담는다
    context = {
        'form': form,
    }
    # 4. create.html을 렌더링
    return render(request, 'create.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')