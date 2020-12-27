"""专家信息管理视图"""
from functools import wraps
import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import random
from Specialist.models import SpecialistCategory
from Specialist.models import *
from Specialist.models import SchoolList
from Specialist.models import ProjectSpecialist
from specialist_info.base import base
from .user import check_login


# Create your views here.
def check_admin(fun):
    """检测是否为管理员
    用于管理员操作页面之前检测，主要为防止直接输入url跳转到无权访问的页面
    - 如果是，则可以直接访问此页面
    - 如果不是，跳转主页
    """
    @wraps(fun)
    def inner(request, *arg, **kwargs):
        level = request.session['login_status']
        if level == '2':
            return fun(request, *arg, **kwargs)
        return redirect('/')
    return inner

@check_login
@check_admin
def view_specialist(request):
    """查看专家信息"""
    response = {}
    specialist = Specialist.objects.get(id=request.GET.get('id'))
    response['specialist'] = specialist
    response['projects'] = ProjectSpecialist.objects.filter(sid=specialist)
    return render(request, 'specialist_view.html', response)

@check_login
@check_admin
def del_specialist(request):
    """查看专家信息"""
    objs = Specialist.objects.filter(id=request.GET.get('id'))
    if objs:
        for obj in objs:
            obj.delete()
    return redirect('/specialist/list/')

@check_login
@check_admin
@base
def add_specialist(request, *arg):
    """新增学生信息"""
    if request.method == 'GET':
        response = {}
        student_list = Studentlist.objects.all()
        response['student_list'] = student_list
        for istudent in response['student_list']:
            print("学生名称为：" + istudent.name)
        return render(request, 'specialist_add.html', response)
    if request.method == 'POST':
        rank =random.randint(0, 1e5)
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        volunteer1 = request.POST.get('volunteer1')
        volunteer2 = request.POST.get('volunteer2')
        volunteer3 = request.POST.get('volunteer3')

        studentlist = Studentlist(
            rank = rank,
            name=name, sex=sex,
            phone=phone, email=email,
            volunteer1=volunteer1, volunteer2=volunteer2, volunteer3=volunteer3
            )
        print("新增学生成功:%s,名次为%d", studentlist.name, studentlist.rank)
        studentlist.save()
        return render(request, 'specialist_add.html', arg[0])

@check_login
@check_admin
@base
def add_school(request, *arg):
    """新增学校信息"""
    if request.method == 'GET':
        response = {}
        school_list = SchoolList.objects.all()
        response['school_list'] = school_list
        for ischool in response['school_list']:
            print("学校名称为：" + ischool.schoolname)
        return render(request, 'school_add.html', response)
    if request.method == 'POST':
        name = request.POST.get('name')
        peopleCount = request.POST.get('peopleCount')

        schoollist = SchoolList(
            schoolname = name, peopleCount = peopleCount
        )
        schoollist.save()
        myData = SchoolList.objects.all()
        print("增加学校成功"+myData[0].schoolname)
        return render(request, 'school_add.html', arg[0])

@check_login
@check_admin
def update_specialist(request):
    """修改学生信息"""
    if request.method == 'POST':
        r_id = request.POST.get('id')
        specialist = Specialist.objects.get(id=r_id)
        specialist.phone = request.POST.get('phone')
        specialist.email = request.POST.get('email')
        specialist.save()
        return redirect('/specialist/view?id=' + r_id)
    response = {}
    response['specialist'] = Specialist.objects.get(id=request.GET.get('id'))
    return render(request, 'specialist_update.html', response)


def category(request):
    """获取学校信息"""
    response = {}
    school_list = SchoolList.objects.all()
    for obj in school_list:
        response[obj.schoolname] = obj.peopleCount
    return HttpResponse(json.dumps(response))

def student(request):
    """获取学生信息"""
    response = {}
    studentList = Studentlist.objects.all()
    for obj in studentList:
        response[obj.name] = obj.rank
    return HttpResponse(json.dumps(response))

def get_specialist_list(name, cate):
    if name or cate:
        if name == '':
            if cate == '0':
                return Specialist.objects.all()
            else:
                return Specialist.objects.filter(category=cate)
        else:
            if cate == '0':
                return Specialist.objects.filter(name__contains=name)
            else:
                return Specialist.objects.filter(name__contains=name).filter(category=cate)
    else:
        return Specialist.objects.all()

