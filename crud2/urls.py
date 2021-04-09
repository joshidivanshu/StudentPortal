"""crud2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from studentreg import views
from crudajax import views as view1

# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.OpenHomeView.as_view(), name='homepage'),
    path('insert/', views.InsertView.as_view(), name='insert'),
    path('show/', views.ShowView.as_view(), name='show'),
    path('delete/<int:id>', views.DelView.as_view(), name='delete'),
    path('update/<int:id>', views.update_view, name='update'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('insert/upload_csv', views.DataUpload.as_view(), name="data_upload"),
    path('insert/upload_text', views.TextUpload.as_view(), name='text_upload'),
    path('insertteacher/', view1.TeacherForm.as_view(), name='tinsert'),
    path('saveteacher/', view1.SaveTeacher.as_view(), name='saveteacher'),
    path('teacherdel/', view1.TeacherDel.as_view(), name='teacherdel'),
    path('teacheredit/', view1.TeacherEdit.as_view(), name='teacheredit'),
    path('teacherupdate', view1.TeacherUpdate.as_view(), name='teacherupdate'),
    path('studdel/',views.DelViewAjax.as_view(),name='studel'),
]

# handler404 = 'account.views.error_404'
# handler500 = 'account.views.error_500'
# handler403 = 'account.views.error_403'
# handler400 = 'account.views.error_400'

# #just for the development purpose
# if settings.DEBUG:
#     urlpatterns +=
#      static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
