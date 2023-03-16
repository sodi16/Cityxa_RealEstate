from django.contrib.auth import get_user_model, get_user
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from property.models import Property, ImageDescription
from users.forms import AdressForm, PropertyForm
from cityxa import settings
from property.forms import AddPropertyForm, AddAdressForm, AddPhotoForm
from users.models import Adress
from env.api_key import api_key


def temp(request):
    if request.method == "POST":
        print()
        breakpoint()
    return render(request, 'property/search_bar.html')


def add_property(request):
    property_form = AddPropertyForm()
    context = {'form': property_form, 'api_key': api_key}
    if request.method == 'POST':
        property_form = AddPropertyForm(request.POST)
        long, lat = request.POST['longitude'], request.POST['latitude']
        if property_form.is_valid() and long and lat:
            # get the Property and user instances objects
            country, city, street, num_apt = request.POST['country'], request.POST['locality'], request.POST['route'], request.POST['street_number']
            adress = Adress.objects.create(country=country, city=city, street=street, num_apt=num_apt, longitude=long, latitude=lat)
            property = property_form.save(commit=False)
            user = get_user(request)
            property.adress = adress

            # add the images to the property
            images = request.FILES.getlist('images')
            property.owner = user
            property.save()

            # if user uploaded images, we add them to the property
            if images:
                for img in images:
                    img_desc = ImageDescription.objects.create(image=img)
                    property.images.add(img_desc)
            else:
                img_desc = ImageDescription.objects.create()
                property.images.add(img_desc)

            property.save()

            # save the property in user properties
            user.properties.add(property)
            user.save()

            context.update({'message': 'Property correctly added'})
            return render(request, 'property/add_property.html', context)
    return render(request, 'property/add_property.html', context)


def autocomplete(request):
    return render(request, 'property/map.html', {'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY})


class display_property(DetailView):
    model = Property
    context_object_name = 'property'
    template_name = 'property/display_property.html'

    def get_queryset(self):
        self.property = Property.objects.get(pk=self.kwargs['pk'])
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_images_url = [img.image.url for img in self.property.images.all()]
        context['images'] = all_images_url
        context['user'] = self.request.user
        return context


def search_property(request):
    form = AddPropertyForm()
    context = {'form': form}
    if request.method == 'POST':
        breakpoint()
    return render(request, 'property/search_property.html', context)


class CreatePropertyView(CreateView):
    form_class = AddPropertyForm
    template_name = 'property/add_property.html'
    success_url = reverse_lazy("home")
    extra_context = {'api_key': api_key}


class DeletePropertyView(DeleteView):
    model = Property
    template_name = 'property/delete.html'
    context_object_name = 'property'
    success_url = reverse_lazy(f'home')


class UpdatePropertyView(UpdateView):
    model = Property
    form_class = AddPropertyForm
    template_name = 'property/add_property.html'

