from django.contrib.auth import get_user
from django.shortcuts import render, redirect
from property.models import Property


def home(request):
    last_posts = None
    context = {}
    user = get_user(request)
    if user.is_authenticated and user.adress:
        context['user'] = user
        user_city, user_country = user.adress.city, user.adress.country
        last_posts = Property.objects.filter(adress__city=user_city).order_by('-posted_date')
        # if there were at least 3 posts of the same city of the user
        if len(last_posts) < 3:
            last_posts = Property.objects.filter(adress__country=user_country).order_by('-posted_date')

    last_posts = Property.objects.all().order_by('-posted_date') if not last_posts else last_posts
    rows_of_posts = len(last_posts) // 3
    context['posts'] = last_posts[:rows_of_posts*3]

    if request.method == 'POST':
        # delete objects of type Property because he is not json serializable
        del context['posts']

        context.update({k: v for k, v in request.POST.items()})

        # Store the data in the session
        request.session['context_data'] = context
        request.session.save()

        return redirect('search_property')

        # return render(request, 'property/search_property.html', context)
    return render(request, 'users/base.html', context)





