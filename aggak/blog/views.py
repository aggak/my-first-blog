from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/home.html', {'posts':posts})
    
def detail_article(request, pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            yes=form.save(commit=False)
            yes.post=post
            yes.save()
            return redirect('detail_article',pk=post.pk)
    else:
        form=CommentForm()
    return render(request, 'blog/detail_article.html', {'post':post,'form':form})

@login_required    
def ecrire_article(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail_article', pk=post.pk)
    else:
        form=PostForm()
    return render(request, 'blog/ecrire_article.html', {'form':form})

@login_required    
def modifier_article(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail_article',pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/modifier_article.html', {'form':form, 'post':post})

@login_required    
def draft(request):
    post=Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/draft.html', {'posts':post})

@login_required    
def publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('detail_article',pk=post.pk)

@login_required    
def supprimer_article(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home')
    
@login_required
def approuver_commentaire(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approved_comment()
    return redirect('detail_article',pk=comment.post.pk)

@login_required  
def supprimer_commentaire(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('detail_article',pk=comment.post.pk)