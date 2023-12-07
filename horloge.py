import time

def convertir_12h(heures):
    if heures == 0:
        return 12
    elif heures > 12:
        return heures - 12
    else:
        return heures

def main():
    format_24h = bool(input("Remplir pour le format 24H : "))
    temps_actuel = (int(input("Entrez l'heure(format 24 heures) :")),
                   int(input("Entrez les minutes: ")),
                   int(input("Entrez les secondes: ")))
    alarme = (int(input("Entrez l'heure de l'alarme (format 24 heures) :")),
              int(input("Entrez les minutes de l'alarme :")))

    while True:
        heures, minutes, secondes = temps_actuel
        if format_24h:
            heure_affichage = f"Heure actuelle : {heures:02d}:{minutes:02d}:{secondes:02d}"
            heure_alarme = f"Alarme à : {alarme[0]:02d}:{alarme[1]:02d}"
        else:
            heure_affichage = f"Heure actuelle : {convertir_12h(heures)}:{minutes:02d}:{secondes:02d} {'AM' if heures < 12 else 'PM'}"
            heure_alarme = f"Alarme à : {convertir_12h(alarme[0])}:{alarme[1]:02d} {'AM' if alarme[0] < 12 else 'PM'}"

        print(heure_affichage, end="\r")
        if temps_actuel == alarme + (0,):
            print("\nAlarme !")
        time.sleep(1)
        temps_actuel = (heures, minutes, secondes + 1)
        if temps_actuel[2] == 60:
            temps_actuel = (heures, minutes + 1, 0)
            if temps_actuel[1] == 60:
                temps_actuel = (heures + 1, 0, 0)
                if temps_actuel[0] == 24:
                    temps_actuel = (0, 0, 0)

main()
