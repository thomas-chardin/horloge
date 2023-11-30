
import time

def convertir_12h(heures):
        if heures == 0:
            return 12
        elif heures > 12:
            return heures - 12
        else:
            return heures
def main():
    format_24h = True
    format_24h = bool(input("Remplir pour le format 24H : "))
    heures = int(input("Entrez l'heure(format 24 heures) : "))
    minutes = int(input("Entrez les minutes: "))
    secondes = int(input("Entrez les secondes: "))
    alarme_h = int(input("Entrez l'heure de l'alarme (format 24 heures) : "))
    alarme_min = int(input("Entrez les minutes de l'alarme : "))
    
    
    while True:
        if format_24h:
            heure_affichage = f"Heure actuelle : {heures:02d}:{minutes:02d}:{secondes:02d}"
            heure_alarme = f"Alarme à : {alarme_h:02d}:{alarme_min:02d}"
        else:
            heure_affichage = f"Heure actuelle : {convertir_12h(heures)}:{minutes:02d}:{secondes:02d} {'AM' if heures < 12 else 'PM'}"
            heure_alarme = f"Alarme à : {convertir_12h(alarme_h)}:{alarme_min:02d} {'AM' if alarme_h < 12 else 'PM'}"

        print(heure_affichage, end="\r")
        if heures == alarme_h and minutes == alarme_min and secondes == 0:
            print("\nAlarme !")
        time.sleep(1)
        secondes += 1
        if secondes == 60:
            secondes = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                heures += 1
                if heures == 24:
                    heures = 0
main()