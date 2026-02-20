from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Score thresholds
SPORTS_PROFESSIONAL = 22
SPORTS_COMPETITIVE = 18
SPORTS_CASUAL = 12

CAREER_HIGH = 20
CAREER_MEDIUM = 15
CAREER_LOW = 10

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

        # Input validation
        if not all([username, email, password]):
            return render(request, "signup.html", {"error": "All fields are required"})

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        auth_login(request, user)
        return redirect("/dashboard/")
if request.method == "POST":
        try:
            q1 = int(request.POST.get("q1", 0))
            q2 = int(request.POST.get("q2", 0))
            q3 = int(request.POST.get("q3", 0))
            q4 = int(request.POST.get("q4", 0))
            q5 = int(request.POST.get("q5", 0))
        except (ValueError, TypeError):
            return render(request, "sports.html", {"error": "Invalid input"})
        
        total_score = q1 + q2 + q3 + q4 + q5
        
        if total_score >= SPORTS_PROFESSIONAL:
            result = "Professional Athlete Potential 🏆"
        elif total_score >= SPORTS_COMPETITIVE:
            result = "Competitive Sports Player ⚡"
        elif total_score >= SPORTS_CASUAL:
            result = "Casual Sports Enthusiast 🎯"
        else:
            result = "Sports may not be your primary interest 🤔"
            
        return render(request, "result.html", {
            "score": total_score,
            "result": result
        })
    return render(request, t , "result.html" ,{
            "score": total_score,
            "result": result
        })
     return render(request ,"sports.html") 
 
 if request.method == "POST":
        try:
            q1 = int(request.POST.get("q1", 0))
            q2 = int(request.POST.get("q2", 0))
            q3 = int(request.POST.get("q3", 0))
            q4 = int(request.POST.get("q4", 0))
            q5 = int(request.POST.get("q5", 0))
        except (ValueError, TypeError):
            return render(request, "career.html", {"error": "Invalid input"})
        
        total_score = q1 + q2 + q3 + q4 + q5
        
        # Primary aptitude detection
        if q1 >= 4 and q3 >= 4:
            result = "Software Developer / Engineer 💻"
        elif q2 >= 4:
            result = "Doctor / Healthcare Professional 🏥"
        elif q3 >= 4:
            result = "Designer / Creative Artist 🎨"
        elif q4 >= 4 and q5 >= 4:
            result = "Manager / Entrepreneur 🚀"
        elif total_score >= CAREER_HIGH:
            result = "Multi-Talented Professional 🌟"
        else:
            result = "Explore multiple fields to discover your strength 🤔"
            
        return render(request, "result_career.html", {
            "score": total_score,
            "result": result
        })
    return render(request, "career.html"
        else:
            result = "Management / Public Relations"

        return render(request, "result_career.html", {"result": result})
