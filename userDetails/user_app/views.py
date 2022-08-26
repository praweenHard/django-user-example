from django.shortcuts import render

# Create your views here.
def index(request):
    data_dic={'title':"India's Best Examination Site ",'name':'Pragati','date':'2022-06-12'}
    return render(request,'basicApp/index.html',data_dic)
def relative(request):
    return render(request,'basicApp/relative_url_template.html')
def other(request):
    return render(request,'basicApp/other.html')
def basic(request):
    return render(request,'basicApp/basic.html')
