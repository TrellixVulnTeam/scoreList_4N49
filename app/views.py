from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from app.models import Client, Rank
# Create your views here.

# 登录
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('update/')
        else:
            print('1111111')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

# 注册
def register(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        result = User.objects.filter(username=username)
        if result:
            return JsonResponse({'message': 'username is already exists !!!'})

        User.objects.create_user(username=username, password=password)
        return JsonResponse({'username': username, 'message': 'register ok'})
    else:
        return render(request, 'register.html')



# 注销
@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')

# 上传
@login_required(login_url='/')
def update(request):
    if request.method == 'POST':
        score = request.POST.get('score', '')
        # 存入分数数据
        if score:
            pre_score = Client.objects.filter(client_num=request.user).first()
            if pre_score:
                pre_score.score = score
                pre_score.save()
            else:
                Client.objects.create(client_num=request.user, score=score)

            # 名次表更新
            Rank.objects.all().delete()
            score_li = [score_obj.id for score_obj in Client.objects.all().order_by('-score')]
            n = 1
            for i in score_li:
                Rank.objects.create(c_id_id=i, rank=n)
                n = n + 1
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'})
    else:
        return render(request, 'update.html')


# 查询
def search(request):
    content = {'scores': [{'ranking': score.rank.rank, 'client': score.client_num, 'score': score.score} for score in Client.objects.all().order_by('-score')]}
    your_score = Client.objects.filter(client_num=request.user).first()
    your_score = {'ranking': your_score.rank.rank, 'score': your_score.score}
    count = Client.objects.all().count()
    if request.method == 'POST':
        start = int(request.POST.get('start', ''))
        end = int(request.POST.get('end', ''))

        content = {'scores': [{'ranking': score.rank.rank, 'client': score.client_num, 'score': score.score} for score in
                              Client.objects.all().order_by('-score')[start - 1:end]]}
        # return JsonResponse({'state': 'ok', 'content':content})
        return render(request, 'search.html', {'content': content['scores'], 'range': range(start-1, end), 'your_score': your_score})
    else:
        return render(request, 'search.html', {'content': content, 'your_score': your_score, 'count': range(count)})

