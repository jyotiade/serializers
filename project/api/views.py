from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializers import StudentSerializer
# Create your views here.
def stu_list(request):
    # stu=Student.objects.create(stu_name='himanshi',stu_city='bhopal',roll=53)
    # print(stu)
    # stu=Student.objects.create(stu_name='jyoti',stu_city='bhopal',roll=29)
    # print(stu)

    # stu=Student.objects.all()
    # serializer=StudentSerializer(stu,many=True)
    # json_data=JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data,content_type='application/json')

    stu=Student.objects.get(id=1)
    serializer=StudentSerializer(stu)
    # json_data=JSONRenderer().render(serializer.data)

    return JsonResponse(serializer.data,safe=False)
