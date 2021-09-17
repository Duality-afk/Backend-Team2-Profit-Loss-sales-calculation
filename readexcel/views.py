from django.shortcuts import render
import pandas as pd
# Create your views here.
def home(request):
    if request.method=="POST":
        file = request.FILES["myFile"]
        df = pd.read_csv(file)
        df['Profit'] = df['SELLING PRICE'] - df['COST PRICE']
        print(df.head())
        df['Loss'] = df['COST PRICE'] - df['SELLING PRICE']
        items = df['ITEM DESCRIPTION']
        sellingp = df['SELLING PRICE']
        costp = df['COST PRICE']
        profit = df['Profit'].sum()
        loss = df['Loss'].sum()
        if profit<0:
            print(loss)
        return render(request, "index.html", {"something":True, "profit":profit, "loss":loss,"items":items,"sellingp":sellingp,"costp":costp})
    else:
        return render(request,"index.html")

def upload(request):
    return render(request, "fileupload.html")