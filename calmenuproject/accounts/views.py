from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# def register(request):
#     if request.method == 'POST':
#         User.objects.create_user(
#             username = request.POST['username']


#         )
#         userid = request.POST['username']
#         pwd = request.POST['password']
#         user = auth.authenticate(request, username=userid, password=pwd)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html')

#     # GET 요청이 들어오면 login form 을 담고있는 login.html을 띄워주는 역할을 함
#     else:
#         return render(request, 'login.html')


#     form = RegisterForm()
#     if form.validate_on_submit(): #유효성 검사. 내용 채우지 않은 항목이 있는지까지 체크
#         usertable = User() 
#         usertable.userid = form.data.get('userid')
#         usertable.email = form.data.get('email')
#         usertable.password = form.data.get('password')

#         db.session.add(usertable) #DB저장
#         db.session.commit() #변동사항 반영
        
#         return "회원가입 성공" 
#     return render_template('register.html', form=form) 


def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

    # GET 요청이 들어오면 login form 을 담고있는 login.html을 띄워주는 역할을 함
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')        