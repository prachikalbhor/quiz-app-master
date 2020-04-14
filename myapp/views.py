from django.shortcuts import render,redirect
from .models import Questions,Review

# Create your views here.
def home(request):
    return render(request,'home.html')
def allreview(request):
    r = Review.objects.all()
    return render(request,'allreviews.html',{'reviews':r})    
def test(request):
    question= Questions.objects.all()
    list_of_id=[q.id for q in question]
    global counter
    counter = 0
    global counter2
    counter2=0
    global id_of_incorrect
    id_of_incorrect=[]

    
    context={
            'question':question,
            
            
        }
    if request.POST:
        list_of_input = list(request.POST)[1:]
        list_of_input = [int(request.POST[x]) for x in list_of_input]
        list_of_ans = [q.right for q in question]
        
        for i in range(len(list_of_input)):
            if(list_of_input[i] == list_of_ans[i]):
                counter=counter+1
            else:
                counter2=counter2+1
                id_of_incorrect.append(list_of_id[i])
        
        
        return redirect('review')

    
    return render(request,'question.html',context)    

def review(request):
    
    question=[]
    for i in id_of_incorrect:
        question.append(Questions.objects.get(id=i))
    context={
        'question':question,
        'correct':counter,
        'incorrect':counter2,
        'p':(counter2/(counter+counter2))*100
        
        
    }

    if request.POST:
        name = request.POST['name']
        review = request.POST['review']
        stars=request.POST['stars']
        Review.objects.create(name=name,review=review,rating=stars)
        return redirect('/')

    return render(request,'review.html',context)