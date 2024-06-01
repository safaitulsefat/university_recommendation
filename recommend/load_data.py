import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_recommendation.settings')
django.setup()

from recommend.models import University

# Load data from CSV files
cse_data = pd.read_csv('data/cse_data.csv')
print(cse_data.head())

def load_data(df):
    for _, row in df.iterrows():
        University.objects.create(
            university=row['University'],
            rank=row['Rank'],
            department='CSE',
            cost=row[' CSE-cost'],
            credit=row['Credit'],
            weiver=row['Weiver ']== 'Yes',
            admission_fee=row['Admission Fee'],
            minimum_gpa=row['Minimum GPA (SSC+HSC)'],
            hostel=row['Hostel']== 'Yes',
            location=row['Location ']
        )

load_data(cse_data)

