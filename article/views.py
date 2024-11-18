from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleLike, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article).order_by('-created_at')
    likes = ArticleLike.objects.filter(article=article).count()
    return render(request, 'article/article_detail.html', {'article': article, 'comments': comments, 'likes': likes})


@login_required
def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    like, created = ArticleLike.objects.get_or_create(user=request.user, article=article)
    
    if created:
        article.likes += 1
        article.save()
        like_count = ArticleLike.objects.filter(article=article).count()
        return JsonResponse({'likes': article.likes, 'like_count': like_count})
    else:
        return JsonResponse({'error': 'You have already liked this article.'}, status=400)



@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, article=article, content=content)
    return redirect('article_detail', pk=pk)
 


