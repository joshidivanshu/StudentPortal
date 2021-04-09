from django.shortcuts import render
from .forms import TeacherRegistration
from .models import Teacher
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class TeacherForm(TemplateView):
    def get(self,request):
        form = TeacherRegistration()
        teach = Teacher.objects.all()
        return render(request, 'crudajax/tdetails.html', {'form': form, 'teach': teach})

# def teacherform(request):
#     form = TeacherRegistration()
#     teach = Teacher.objects.all()
#     return render(request,'crudajax/tdetails.html',{'form':form,'teach':teach})


class SaveTeacher(TemplateView):
    def post(self,request):
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            eno = request.POST['eno']
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            experience = request.POST['experience']
            tchr = Teacher(eno=eno, name=name, email=email, subject=subject, experience=experience)
            tchr.save()
            # print()
            tch = Teacher.objects.values()
            teacher_data = list(tch)
            return JsonResponse({'status': 'Saved Successfully', 'teacher_data': teacher_data})
        else:
            return JsonResponse({'status': 'Invalid Form'})

#@csrf_exempt
# def saveteacher(request):
#     if(request.method == "POST"):
#         form = TeacherRegistration(request.POST)
#         if(form.is_valid()):
#             eno = request.POST['eno']
#             name = request.POST['name']
#             email = request.POST['email']
#             subject = request.POST['subject']
#             experience = request.POST['experience']
#             tchr =  Teacher(eno=eno,name=name,email=email,subject=subject,experience=experience)
#             tchr.save()
#             #print()
#             tch = Teacher.objects.values()
#             teacher_data = list(tch)
#             return JsonResponse({'status':'Saved Successfully','teacher_data':teacher_data})
#         else:
#             return JsonResponse({'status':'Invalid Form'})


class TeacherDel(TemplateView):
    def post(self,request):
        eno = request.POST.get('eno')
        ti = Teacher.objects.get(eno=eno)
        ti.delete()
        return JsonResponse({'status': 1})

    def get(self,request):
        return JsonResponse({'status':0})

# def teacherdel(request):
#     if(request.method == "POST"):
#         eno = request.POST.get('eno')
#         ti = Teacher.objects.get(eno=eno)
#         ti.delete()
#         return JsonResponse({'status':1})
#     else:
#         return JsonResponse({'status':0})


class TeacherEdit(TemplateView):
    def post(self,request):
        eno = request.POST.get('eno')
        ti = Teacher.objects.get(eno=eno)
        teacher_data = {"eno": ti.eno, "name": ti.name, "email": ti.email, "subject": ti.subject,
                        "experience": ti.experience}
        return JsonResponse(teacher_data)

# def teacheredit(request):
#     if(request.method == 'POST'):
#         eno = request.POST.get('eno')
#         ti = Teacher.objects.get(eno=eno)
#         teacher_data = {"eno":ti.eno,"name":ti.name,"email":ti.email,"subject":ti.subject,"experience":ti.experience}
#         return JsonResponse(teacher_data)


class TeacherUpdate(TemplateView):
    def post(self,request):
        eno = request.POST['eno']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        experience = request.POST['experience']
        tchr = Teacher(eno=eno, name=name, email=email, subject=subject, experience=experience)
        tchr.save()
        tch = Teacher.objects.values()
        teacher_data = list(tch)
        return JsonResponse({'status': 'Saved Successfully', 'teacher_data': teacher_data})
#
# def teacherupdate(request):
#     eno = request.POST['eno']
#     name = request.POST['name']
#     email = request.POST['email']
#     subject = request.POST['subject']
#     experience = request.POST['experience']
#     tchr = Teacher(eno=eno, name=name, email=email, subject=subject, experience=experience)
#     tchr.save()
#     tch = Teacher.objects.values()
#     teacher_data = list(tch)
#     return JsonResponse({'status': 'Saved Successfully', 'teacher_data': teacher_data})

