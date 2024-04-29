from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('retrieveproduct')  # Change 'home' to the name of your desired redirect page
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

@unauthenticated_user
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('retrieveproduct')
    else:
      form = AuthenticationForm()
    return render(request,'login.html', {'form':form})


from django.shortcuts import redirect





# def logout_view(request):
#     logout(request)
#     return redirect('signup')


# @login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signup')
    context = {
        'user': request.user
    }
    return render(request, 'logout.html', context)