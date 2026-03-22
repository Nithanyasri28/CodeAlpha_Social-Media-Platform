from django.shortcuts import render,redirect
from django.shortcuts import redirect, get_object_or_404
# Create your views here.
from .models import Post,Comment
from .models import Follow,User
from .models import Profile
from django.db.models import Q

def feed(request):
    query = request.GET.get('q')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = Post.objects.filter(
            Q(caption__icontains=query) |
            Q(user__username__icontains=query)
        ).order_by('-created_at')

    following_users = request.user.following.values_list('following__id', flat=True)

    return render(request, 'feed.html', {
        'posts': posts,
        'query': query,
        'following_users': following_users
    })

def create_post(request):
    if request.method == "POST":
        caption = request.POST.get('caption')
        media = request.FILES.get('media')  # 👈 GET MEDIA

        image = None
        video = None

        if media:
            if media.content_type.startswith('image'):
                image = media
            elif media.content_type.startswith('video'):
                video = media

        Post.objects.create(
            user=request.user,
            caption=caption,
            image=image,
            video=video
        )

        return redirect('feed')

    return render(request, 'create_post.html')


def like_post(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("feed")

def add_comment(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        text = request.POST.get("comment")

        Comment.objects.create(
            post=post,
            user=request.user,
            text=text
        )

    return redirect("feed")


def follow_user(request, user_id):
    user_to_follow = User.objects.get(id=user_id)

    if request.user != user_to_follow:
        follow, created = Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

        if not created:
            follow.delete()

    return redirect('profile', user_id=user_id)

def profile(request, user_id):
    user_profile = User.objects.get(id=user_id)
    posts = Post.objects.filter(user=user_profile)

    is_following = Follow.objects.filter(
        follower=request.user,
        following=user_profile
    ).exists()

    followers_count = Follow.objects.filter(following=user_profile).count()
    following_count = Follow.objects.filter(follower=user_profile).count()

    context = {
        'user_profile': user_profile,
        'posts': posts,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count
    }

    return render(request, 'profile.html', context)

def my_profile(request):
    user = request.user
    profile = user.profile
    posts = Post.objects.filter(user=user)

    followers_count = Follow.objects.filter(following=user).count()
    following_count = Follow.objects.filter(follower=user).count()

    return render(request, 'profile.html', {
        'profile': profile,
        'posts': posts,
        'followers_count': followers_count,
        'following_count': following_count,
    })



def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user == post.user:
        post.delete()

    return redirect('/feed/')


def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        bio = request.POST.get('bio')
        image = request.FILES.get('profile_pic')

        profile.bio = bio

        if image:
            profile.profile_pic = image

        profile.save()
        return redirect('/myprofile/')

    return render(request, 'edit_profile.html', {'profile': profile})



"""
def search(request):
    query = request.GET.get('q')

    users = []
    posts = []

    if query:
        users = User.objects.filter(username__icontains=query)

        posts = Post.objects.filter(
            Q(caption__icontains=query) |
            Q(user__username__icontains=query)
        )

    context = {
        'query': query,
        'users': users,
        'posts': posts
    }

    return render(request, 'search.html', context)
"""