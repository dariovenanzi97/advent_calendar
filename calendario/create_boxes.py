import os
import django
import sys

# Configura le impostazioni Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advent_calendar.settings')
django.setup()

from datetime import date
from calendario.models import CalendarBox

def create_boxes():
    # Lista delle date da creare (8-25 dicembre 2024)
    dates = [date(2024, 12, day) for day in range(8, 26)]
    
    messages = [
        "Massaggetto Soft",
        "Pacchetto Deluxe (Sessione di kiss e double)",
        "Beef Experience (Total Touch)",
        "Double Night",
        "Cena Personalizzata",
        "Doccia Col Beef",
        "Pelle a pelle",
        "Massaggio Deluxe",
        "Essenzietti + Bulipi",
        "All you can kiss",
        "Rilassetti (con Leo)",
        "Super Cuddle Time",
        "Movie Night & Coccole",
        "50 sfumature di beef",
        "Colazione coi kiss",
        "Surprise Box (tu scegli)",
        "Massaggio Beef Special",
        "Christmas Deluxe"
    ]
    
    for i, box_date in enumerate(dates):
        CalendarBox.objects.create(
            date=box_date,
            message=messages[i % len(messages)],
            is_opened=False
        )

if __name__ == '__main__':
    create_boxes()
    print("Caselle create con successo!")