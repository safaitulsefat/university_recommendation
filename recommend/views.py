from django.http import HttpResponse
from django.shortcuts import render
from .models import University
from .forms import RecommendationForm
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

def home(request):
    return render(request,'recommend/home.html')

def recommend_universities(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method == 'POST':
            form = RecommendationForm(request.POST)
            if form.is_valid():
                department = form.cleaned_data['department']
                cost = form.cleaned_data['cost']
                gpa = form.cleaned_data['gpa']

                universities = University.objects.filter(department=department, cost__lte=cost, minimum_gpa__lte=gpa)
                
                if not universities.exists():
                    return render(request, 'recommend/results.html', {'message': 'No universities found matching the criteria.'})
                
                # Prepare data for KNN
                df = pd.DataFrame(list(universities.values()))
                X = df[['cost', 'minimum_gpa']]
                y = df['rank']
                
                knn = KNeighborsClassifier(n_neighbors=5)
                knn.fit(X, y)
                
                input_data = [[cost, gpa]]
                neighbors = knn.kneighbors(input_data, return_distance=False)
                
                recommended_universities = df.iloc[neighbors[0]].sort_values(by='rank')
                
                return render(request, 'recommend/results.html', {'universities': recommended_universities.to_dict(orient='records')})
        else:
            form = RecommendationForm()
        return render(request, 'recommend/index.html', {'form': form})
    else:
        return HttpResponse("You need to be logged in to access this page.")
