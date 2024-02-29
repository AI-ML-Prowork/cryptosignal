from django.shortcuts import render

# Create your views here.


def admin_base(request):
    return render(request, 'admin_base.html')



def profile(request):

    return render(request, 'admin_panel/myprofile.html')


def profile_list(request):
    some_variable = range(1, 51)
    return render(request, 'admin_panel/profile_list.html', {'some_variable': some_variable})