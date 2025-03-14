from challenge.models import Challenge, ChallengeCompleted
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from registration.models import UserProfile
from .forms import NameForm, UsernameForm, PasswordForm, UserForm


def dashboard(request):
    """Handles account page - not yet renamed to account"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    # retrieves current user object data by user id
    current_user_id = request.user.id
    current_user_object = UserProfile.objects.get(userId=current_user_id)
    username = current_user_object.user.username
    first_name = current_user_object.user.first_name
    last_name = current_user_object.user.last_name
    email = current_user_object.user.email
    points = current_user_object.points
    # checks which role user is and assigns role a string
    if current_user_object.is_admin:
        role = 'Admin'
    elif current_user_object.is_game_keeper:
        role = 'Game Keeper'
    else:
        role = 'User'
    # prepares to send data to html
    context = {
        'username': username,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'points': points,
        'role': role,
        'userId':current_user_id,
    }
    # only runs if a form is submitted (delete account in this case)
    if request.method == "POST":
        current_userprofile = UserProfile.objects.get(userId=request.user.id)
        current_user = User.objects.get(username=username)
        # deletes both User and UserProfile from database
        current_user.delete()
        current_userprofile.delete()
        return redirect("../../register")
    return render(request, 'dashboard.html', context)


def challenges(request):
    """Function handles account challenge pages"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # retrieves all challenges
    all_challenges = Challenge.objects.all()
    challenges_list = list(all_challenges)
    current_user_id = request.user.id
    current_user_object = UserProfile.objects.get(userId=current_user_id)
    # Retrives all completed challenges done by user
    all_completed = ChallengeCompleted.objects.filter(userId=current_user_object).values_list("challengeId", flat=True)
    # Fill with incompleted challenges, check and put any challenges not in completed
    incomplete_challenges = [challenge for challenge in challenges_list if challenge.challengeId not in all_completed]
    return render(request, 'dashboard_challenges.html', {'challenges': incomplete_challenges})


def change_uname(request):
    """
    Function to provide render html page and process username updating
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # initialise form
    form = UsernameForm()
    if request.method == "POST":
        # retrieve data from form
        username = request.POST.get('username')
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        # get User object from UserProfile object
        for current_user in current_user_list:
            current_user_object = current_user.user
        current_user_object.username = username
        current_user_object.save()
    return render(request, 'dashboard_username.html', {'form': form})


def change_name(request):
    """
    Function to provide render html page and process name updating
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    form = NameForm()
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user
        current_user_object.first_name = first_name
        current_user_object.last_name = last_name
        current_user_object.save()
    return render(request, 'dashboard_name.html', {'form': form})


def change_password(request):
    """
    Function to provide render html page and process password updating
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    form = PasswordForm()
    if request.method == "POST":
        password = request.POST.get('password')
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user
        # uses django set_password function to replace password (adds salting, hashing etc)
        current_user_object.set_password(password)
        current_user_object.save()
        # updates cookie so user isn't logged out and can carry on
        update_session_auth_hash(request, current_user_object)
        return redirect('change-password')
    return render(request, 'dashboard_password.html', {'form': form})


def logout_dashboard(request):
    # removes session and takes user to login page
    logout(request)
    return redirect("../../../")

def edit_account(request):
    userprofile = get_object_or_404(UserProfile, userId=request.user.id)
    user_instance = userprofile.user
    if request.method == "POST":
        form = UserForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('../')
    else: 
        form = UserForm(instance=user_instance)
    return render(request, 'edit_details.html', {'form': form})

def rewards(request):
    if request.method == 'GET':
        userprofile = get_object_or_404(UserProfile, userId=request.user.id)
        user_points = userprofile.points
      
        rewards = [['Bronze', 100, "cross.png"], ['Silver', 250, "cross.png"], ['Gold', 500, "cross.png"]]
        user_rewards = []
        if user_points >= rewards[0][1]:
            rewards[0][2] = "tick.png"
            user_rewards.append(rewards[0])
        else:
            user_rewards.append(rewards[0])
        
        if user_points >= rewards[1][1]:
            rewards[1][2] = "tick.png"
            user_rewards.append(rewards[1])
        else:
            user_rewards.append(rewards[1])

        if user_points >= rewards[2][1]:
            rewards[2][2] = "tick.png"
            user_rewards.append(rewards[2])
        else:
            user_rewards.append(rewards[2])



        context = {
            'rewards': user_rewards,
        }
        print(user_rewards)
    return render(request, 'rewards.html', context)

