from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm  # Import the form

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect after successful form submission
    else:
        form = StudentForm()
    
    return render(request, 'application1/student_form.html', {'form': form})
