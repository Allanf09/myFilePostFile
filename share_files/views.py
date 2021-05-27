from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


from .models import Post
from .forms import PostForm



def search_file(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        posts = Post.objects.filter(nombre_del_archivo__contains=searched)
        return render(request, 'share/search_file.html', {'searched': searched, 'posts': posts})
    else:
        return render(request, 'share/search_file.html', {})


def post_list(request):
    posts = Post.objects.order_by("-posted_at")
    return render(request, 'share/post_list.html', {'posts': posts})

def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('share_files:post_list')
    else:
        form = PostForm()
            
    return render(request, 'share/upload.html', {'form': form})









