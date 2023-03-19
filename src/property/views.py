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
from django.db.models import F, Func


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


def filter_property(request):
    id_type_of_property = request.GET.get('id_type_of_property')
    id_rent_buy = request.GET.get('id_rent_buy')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_rooms = request.GET.get('min_num_rooms')
    max_rooms = request.GET.get('max_num_rooms')
    furniture = request.GET.get('furniture')
    elevator = request.GET.get('elevator')
    balcony = request.GET.get('balcony')
    renovated = request.GET.get('renovated')
    storage = request.GET.get('storage')
    disable_access = request.GET.get('disable_access')
    safe_room = request.GET.get('safe_room')
    central_air_conditioner = request.GET.get('central_air_conditioner')
    quiet_neighborhood = request.GET.get('quiet_neighborhood')

    properties = Property.objects.all()

    if id_type_of_property:
        properties = properties.filter(id_type_of_property=int(id_type_of_property))

    if id_rent_buy:
        properties = properties.filter(id_rent_buy=int(id_rent_buy))

    if min_price:
        properties = properties.filter(price__gte=min_price)

    if max_price:
        properties = properties.filter(price__lte=max_price)

    if min_rooms:
        properties = properties.filter(num_rooms__gte=min_rooms)

    if max_rooms:
        properties = properties.filter(num_rooms__lte=max_rooms)

    if furniture:
        properties = properties.filter(furniture=int(furniture))

    if elevator:
        properties = properties.filter(elevator=int(elevator))

    if balcony:
        properties = properties.filter(balcony=balcony)

    if renovated:
        properties = properties.filter(renovated=renovated)

    if storage:
        properties = properties.filter(storage=storage)

    if disable_access:
        properties = properties.filter(disable_access=disable_access)

    if safe_room:
        properties = properties.filter(safe_room=safe_room)

    if central_air_conditioner:
        properties = properties.filter(central_air_conditioner=central_air_conditioner)

    if quiet_neighborhood:
        properties = properties.filter(quiet_neighborhood=quiet_neighborhood)


    return properties


def get_closes_properties(long, lat, distance_coordinate=0.05):
    """
    Get the houses that are close to the given adress
    """
    properties = Property.objects.annotate(diff=Func(F('adress__longitude') - long, function='ABS')).filter(diff__lte=distance_coordinate)
    properties = properties.annotate(diff=Func(F('adress__latitude') - lat, function='ABS')).filter(diff__lte=distance_coordinate)
    return properties


def search_property(request, context={}):
    if request.method == 'GET':
        context_data = request.session.get('context_data')
        if 'filter-form' in request.GET:
            list_property = filter_property(request)
            context['properties'] = list_property

        if context_data:
            form = AddPropertyForm
            context['form'] = form
            context['api_key'] = api_key
            context['street_number'] = context_data.get('street_number')
            context['route'] = context_data.get('route')
            context['locality'] = context_data.get('locality')
            context['administrative_area_level_1'] = context_data.get('administrative_area_level_1')
            context['country'] = context_data.get('country')
            context['latitude'] = context_data['latitude']
            context['longitude'] = context_data['longitude']
            context['properties'] = get_closes_properties(float(context_data['longitude']), float(context_data['latitude']))
            context['user'] = get_user(request)

            # Clear the data from the session
            del request.session['context_data']
            request.session.save()

        else:
            print('Enter here when clickin on properties form menu')

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

