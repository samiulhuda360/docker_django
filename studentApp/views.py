from django.views.generic import ListView
from .models import Student

# Create your views here.

class StudentListView(ListView):
    model = Student
    context_object_name = 'student_list'
    template_name = 'studentApp/student_list.html'
