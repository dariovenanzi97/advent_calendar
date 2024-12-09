from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import CalendarBox

def calendar_view(request):
    current_date = timezone.now().date()
    boxes = CalendarBox.objects.all().order_by('date')
    return render(request, 'calendario/calendar.html', {'boxes': boxes, 'current_date': current_date})

def open_box(request, box_id):
    box = get_object_or_404(CalendarBox, id=box_id)
    current_date = timezone.now().date()
    
    if box.date <= current_date and not box.is_opened:
        box.is_opened = True
        box.save()
        
    return JsonResponse({
        'success': True,
        'image_url': box.image.url if box.image else '',
        'message': box.message,
        'day': box.date.day
    })

from django.http import JsonResponse

def open_box(request, box_id):
    box = get_object_or_404(CalendarBox, id=box_id)
    current_date = timezone.now().date()
    
    response_data = {
        'success': True,
        'image_url': box.image.url if box.image else '',
        'message': box.message,
        'day': box.date.day
    }
    
    if box.date <= current_date and not box.is_opened:
        box.is_opened = True
        box.save()
    
    # Aggiungi questo print per debug
    print("Response data:", response_data)
    return JsonResponse(response_data)