from django.shortcuts import render
from form.forms import Alunoform
# Create your views here.
def form_aluno(request):
    if request.method == 'POST':
        form = Alunoform(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = Alunoform()

    
    context = {'form': form}
    return render(request,'forms/index.html',context)