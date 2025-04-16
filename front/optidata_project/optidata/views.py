from django.shortcuts import render

# Create your views here.
# optidata/views.py
from django.shortcuts import render
from .models import Widget
import json

def dashboard(request):
    widgets = Widget.objects.all()
    # Transformer le QuerySet en liste de dictionnaires
    widgets_list = [
        {
            "id": widget.id,
            "name": widget.name,
            "view_path": widget.view_path,
            "position_x": widget.position_x,
            "position_y": widget.position_y,
            "width": widget.width,
            "height": widget.height,
        }
        for widget in widgets
    ]
    context = {
        "widgets": json.dumps(widgets_list)  # On convertit en JSON pour le passer à JavaScript
    }
    return render(request, "optidata/dashboard.html", context)
