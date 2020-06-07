from django.shortcuts import render
from django.http.response import HttpResponse
import pickle
import numpy as np

# Create your views here.

def index(request):
  return render(request,'index.html')

def blood_test(request):
  if request.method == 'POST':
    ldh = request.POST['ldh']
    hcr_protein = request.POST['hcr_protein']
    lymph = request.POST['lymph']
    file = open('model_covid.pkl','rb')

    classifier = pickle.load(file)
    file.close()

    user_data = np.array((ldh,hcr_protein,lymph)).reshape(1,3)

    result = classifier.predict_proba(user_data) 
    result=round(result[0][1]*100,2)
    print(f"Result: {result}")
    return render(request,'result.html',{'result':result})
  else:
    return render(request,'blood-test.html')
