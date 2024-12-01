from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import Profile, CustomUser
from django.views.generic.detail import DetailView

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('shop:all_products')

    def form_valid(self, form):

        response = super().form_valid(form)


        customer_group, created = Group.objects.get_or_create(name='Customer')
        self.object.groups.add(customer_group)

        login(self.request, self.object)
        return response 

class ManagerSignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        response = super().form_valid(form)

      
        manager_group, created = Group.objects.get_or_create(name='Manager')
        self.object.groups.add(manager_group)
        return response

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'