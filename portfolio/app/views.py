from django.shortcuts import render
from database.database import query_column_data

from pdb import set_trace as bp

def home(request):
    return render(
        request, 'home.html', {},
    )

def thm_profile(request):
    return render(
        request, 'thm_profile.html', {}
    )

def thm_badges(request):
    rows = query_column_data('thm_profile_badges','*')
    rows = [rows[i] for i in range(len(rows))]
    return render(
        request, 'thm_badges.html',
        {'badge_data':rows})