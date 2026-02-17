from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# # username = "ishak" password = "isha00000" 
# #admin usermane = "isha" pass = "isha"

def index(request):
    return render(request, "index.html")




def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/dashboard/")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("/")
@login_required
def dashboard(request):
    return render(request , "dashboard.html")
@login_required
def career(request):
    return render( request , "career.html" )
@login_required
def sports(request):
    return render(request , "sports.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        auth_login(request, user)
        return redirect("/login/")

    return render(request, "signup.html")
@login_required
def sports_result(request):
     if request.method == "POST":
        q1 = int(request.POST.get("q1", 0))
        q2 = int(request.POST.get("q2", 0))
        q3 = int(request.POST.get("q3", 0))
        q4 = int(request.POST.get("q4", 0))
        q5 = int(request.POST.get("q5", 0))
        
        total_score = q1 +q2 +q3 +q4 + q5
        if total_score >= 22:
            result = "Professional Athlete Potential 🏆"
        elif total_score >= 18:
            result = "Competitive Sports Player ⚡"
        elif total_score >= 12:
            result = "Casual Sports Enthusiast 🎯"
        else:
            result = "Sports may not be your primary interest 🤔"
            
        return render(request , "result.html" ,{
            "score": total_score,
            "result": result
        })
     return render(request ,"sports.html") 
 
 
    
@login_required        
def career_result(request):
     if request.method == "POST":
        q1 = int(request.POST.get("q1", 0))
        q2 = int(request.POST.get("q2", 0))
        q3 = int(request.POST.get("q3", 0))
        q4 = int(request.POST.get("q4", 0))
        q5 = int(request.POST.get("q5", 0))
        
        total_score = q1 +q2 +q3 +q4 + q5
        if q1 >= 4 and q3 >= 4:
            result = "Software Developer / Engineer 💻"

        elif q2 >= 4:
            result = "Doctor / Healthcare Professional 🏥"

        elif q3 >= 4:
            result = "Designer / Creative Artist 🎨"

        elif q4 >= 4 and q5 >= 4:
            result = "Manager / Entrepreneur 🚀"

        elif total_score >= 20:
            result = "Multi-Talented Professional 🌟"

        else:
            result = "Explore multiple fields to discover your strength 🤔"

            
        return render(request , "result_career.html" ,{
            "score": total_score,
            "result": result
        })
     return render(request ,"career.html")    

