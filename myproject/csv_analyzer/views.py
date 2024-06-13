import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO
from django.shortcuts import render, redirect
from .forms import CSVFileForm
from .models import CSVFile


def home(request):
    return render(request,'csv_analyzer/home.html')


def upload_file(request):
    if request.method == "POST":
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.save()
            return redirect('csv_analyzer:analyze',csv_file.id)
    else:
        form = CSVFileForm()
    return render(request, 'csv_analyzer/upload.html',{'form':form})


def analyze(request,file_id):
    csv_file = CSVFile.objects.get(id=file_id)
    df = pd.read_csv(csv_file.file)

    head = df.head()

    summary_stats = df.describe().transpose()

    missing_values = df.isnull().sum()

    img_data = []
    for column in df.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(df[column].dropna())
        plt.title(f'Histogram for {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')

        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        img_data.append(image_base64)
        plt.close()

    return render(request, 'csv_analyzer/analyze.html',{
        'head':head.to_html(classes='table table-striped'),
        'summary_stats':summary_stats.to_html(classes='table table-striped'),
        'missing_values':missing_values.to_dict(),
        'img_data':img_data,
    })