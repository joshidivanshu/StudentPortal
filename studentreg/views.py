import csv,io
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class OpenHomeView(View):
    def get(self,request):
        return render(request, 'star/homepage.html')

# def openhome(request):
#     return render(request, 'star/homepage.html')


class InsertView(View):
    form = StudentForm

    def get(self,request):
        return render(request, 'star/insert.html', {'form': self.form})

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'star/insert.html', {'message': 'Student information added successfully'})

# def insert_view(request):
#     form = StudentForm()
#     if (request.method == 'POST'):
#         form = StudentForm(request.POST)
#         if (form.is_valid()):
#             form.save()
#             return render(request, 'star/insert.html',{'message':'Student information added successfully'})
#     return render(request, 'star/insert.html', {'form': form})


@method_decorator(login_required,name='dispatch')
class ShowView(TemplateView):
    def get(self,request):
        student_list = Student.objects.all()
        paginator = Paginator(student_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'star/show.html', {'page_obj': page_obj})

# @login_required
# def show_view(request):
#     student_list = Student.objects.all()
#     paginator = Paginator(student_list,10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'star/show.html', {'page_obj': page_obj})
#     #return render(request, 'star/login.html')


@method_decorator(permission_required('admin.can_add_log_entry'),name='dispatch')
class DelView(TemplateView):
    def get(self,request,id):
        student = Student.objects.get(eno=id)
        student.delete()
        return redirect('/')

#
# @permission_required('admin.can_add_log_entry')
# def del_view(request, id):
#     student = Student.objects.get(eno=id)
#     student.delete()
#     return redirect('/')

def update_view(request, id):
    try:
        students = Student.objects.get(eno=id)
    except:
        students = None
    form = StudentForm(request.POST, instance=students)
    if (form.is_valid()):
        form.save(commit=True)
        return redirect('/')
    return render(request, 'star/update.html', {'students': students})


@method_decorator(permission_required('admin.can_add_log_entry'),name='dispatch')
class DataUpload(TemplateView):
    def post(self,request):
        csv_file = request.FILES['csvfile']
        data_set = csv_file.read().decode('UTF-8')
        list1 = data_set.split("\n")
        for i in range(1, len(list1) - 2):
            temp = list1[i].split(",")
            print(temp)
            Student.objects.update_or_create(
                eno=temp[0],
                fname=temp[1],
                lname=temp[2],
                email=temp[3],
                address=temp[4],
                phone=temp[5],
            )
        return render(request, 'star/homepage.html')

# @permission_required('admin.can_add_log_entry')
# def data_upload(request):
#     csv_file =  request.FILES['csvfile']
#     data_set = csv_file.read().decode('UTF-8')
#     list1 = data_set.split("\n")
#     for i in range(1,len(list1)-2):
#         temp = list1[i].split(",")
#         print(temp)
#         Student.objects.update_or_create(
#             eno=temp[0],
#             fname=temp[1],
#             lname=temp[2],
#             email=temp[3],
#             address=temp[4],
#             phone=temp[5],
#         )
#     return render(request,'star/homepage.html')


@method_decorator(permission_required('admin.can_add_log_entry'),name='dispatch')
class TextUpload(TemplateView):
    def post(self,request):
        txt_f = request.FILES['txtfile']
        # converting byte string to string class
        txt_file = txt_f.read().decode('UTF-8')
        li = txt_file.split("\n")
        for i in range(0, len(li) - 1):
            temp = list(li[i].split(" "))
            Student.objects.update_or_create(
                eno=temp[0],
                fname=temp[1],
                lname=temp[2],
                email=temp[3],
                address=temp[4],
                phone=temp[5],
            )
        return render(request, 'star/homepage.html')

        
@method_decorator(csrf_exempt,name='dispatch')
class DelViewAjax(TemplateView):
    def post(self,request):
        eno = request.POST.get('id')
        ti = Student.objects.get(eno=eno)
        ti.delete()
        return JsonResponse({'status': 1})
    def get(self,request):
        return JsonResponse({'status':0})        

# @permission_required('admin.can_add_log_entry')
# def text_upload(request):
#     txt_f = request.FILES['txtfile']
#     #converting byte string to string class
#     txt_file = txt_f.read().decode('UTF-8')
#     li = txt_file.split("\n")
#     for i in range(0,len(li)-1):
#         temp = list(li[i].split(" "))
#         Student.objects.update_or_create(
#             eno = temp[0],
#             fname = temp[1],
#             lname = temp[2],
#             email = temp[3],
#             address = temp[4],
#             phone = temp[5],
#         )
#     return render(request,'star/homepage.html')





