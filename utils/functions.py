import json
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import noise
import numpy as np
from glob import glob

import os

def user_params_datei_auswahl():
    """
    Lässt den Benutzer eine Parameterdatei aus dem Ordner 'params' auswählen.

    Gibt den Dateinamen der ausgewählten Datei zurück.

    Returns:
        str: Der Pfad zur ausgewählten Datei.
    """
    files = glob('params/*.json')

    # Liste die Dateien auf
    for i, file in enumerate(files):
        print(f'{i}: {file}')

    while True:
        # Frage den Benutzer, welche Datei geladen werden soll
        print(f'Welche Datei soll geladen werden? (0 bis {len(files) - 1})')
        dateiauswahl = input('> ')

        # Validiere die Benutzereingabe
        if dateiauswahl.isdigit() and 0 <= int(dateiauswahl) < len(files):
            return files[int(dateiauswahl)]
        else:
            print("Ungültige Auswahl, bitte versuchen Sie es erneut.")


def benutzer_parameter_abfrage():
    """
    Fragt den Benutzer, ob er Parameter aus einer Datei laden oder neue Parameter eingeben möchte.

    Returns:
        str: 'l' für Laden, 'n' für neue Parameter.
    """
    while True:
        auswahl = input('Möchten Sie Parameter aus einer Datei laden (l) oder neue Parameter eingeben (n)? ')
        if auswahl.lower() in ('l', 'n'):
            return auswahl.lower()
        else:
            print("Ungültige Auswahl, bitte geben Sie 'l' oder 'n' ein.")

def validiere_input(nachricht, typ, min=None, max=None, default=None):
    """
    Fordert den Benutzer zur Eingabe eines Werts auf und validiert diesen.

    Args:
        nachricht (str): Die Nachricht, die dem Benutzer angezeigt wird.
        typ (type): Der erwartete Datentyp des Werts.
        min (Optional[Number]): Der minimale akzeptable Wert.
        max (Optional[Number]): Der maximale akzeptable Wert.
        default (Optional[Number]): Der Standardwert, falls der Benutzer keinen Wert eingibt.

    Returns:
        Der validierte Wert.
    """
    while True:
        try:
            ein = input(nachricht)
            if not ein and default is not None:
                return default
            ein = typ(ein)
            if min is not None and ein < min:
                print(f"Der Wert darf nicht kleiner sein als {min}. Bitte versuchen Sie es erneut.")
                continue
            if max is not None and ein > max:
                print(f"Der Wert darf nicht größer sein als {max}. Bitte versuchen Sie es erneut.")
                continue
            return ein
        except ValueError:
            print(f"Ungültige Eingabe. Bitte geben Sie einen Wert des Typs {typ.__name__} ein.")
            
def benutzer_parameter_eingabe_und_speichern():
    """
    Erlaubt dem Benutzer, Parameter einzugeben und speichert sie in einer Datei.

    Returns:
        str: Der Pfad zur Datei, in der die Parameter gespeichert sind.
    """
    params = {
        'breite': validiere_input('Die Breite des Rauschens.\nbreite (int >= 1): ', int, min=1, default=16),
        'hoehe': validiere_input('Die Höhe des Rauschens.\nhoehe (int >= 1): ', int, min=1, default=16),
        't': validiere_input('Der Zeitpunkt, für den das Rauschen generiert wird.\nt (float): ', float, default=0.0),
        'scale_x': validiere_input('Der Skalierungsfaktor in x-Richtung.\nscale_x (float >= 0): ', float, min=0.0, default=0.19),
        'scale_y': validiere_input('Der Skalierungsfaktor in y-Richtung.\nscale_y (float >= 0): ', float, min=0.0, default=0.19),
        'scale_t': validiere_input('Der Skalierungsfaktor in der Zeitdimension.\nscale_t (float >= 0): ', float, min=0.0, default=0.5),
        'octaves': validiere_input('Die Anzahl der Oktaven für das Perlin-Rauschen.\noctaves (int >= 1): ', int, min=1, default=6),
        'persistence': validiere_input('Die Persistenz für das Perlin-Rauschen.\npersistence (float zwischen 0 und 1): ', float, min=0.0, max=1.0, default=0.4),
        'lacunarity': validiere_input('Die Lacunarität für das Perlin-Rauschen.\nlacunarity (float >= 1): ', float, min=1.0, default=2.0),
        'repeatx': validiere_input('Die Wiederholungsperiode des Rauschens in x-Richtung.\nrepeatx (int >= 0): ', int, min=0, default=1024),
        'repeaty': validiere_input('Die Wiederholungsperiode des Rauschens in y-Richtung.\nrepeaty (int >= 0): ', int, min=0, default=1024),
        'repeatz': validiere_input('Die Wiederholungsperiode des Rauschens in der Zeitdimension.\nrepeatz (int >= 0): ', int, min=0, default=1024),
        'base': validiere_input('Ein Startwert für den Zufallsgenerator.\nbase (int): ', int, default=0),
        'rot_scale': validiere_input('Der Skalierungsfaktor für die rote Farbkomponente.\nrot_scale (float zwischen 0 und 1): ', float, min=0.0, max=1.0, default=0),
        'gruen_scale': validiere_input('Der Skalierungsfaktor für die grüne Farbkomponente.\ngruen_scale (float zwischen 0 und 1): ', float, min=0.0, max=1.0, default=1.0),
        'blau_scale': validiere_input('Der Skalierungsfaktor für die blaue Farbkomponente.\nblau_scale (float zwischen 0 und 1): ', float, min=0.0, max=1.0, default=0),
        'rot_invertiert': validiere_input('Soll die rote Farbkomponente invertiert werden?\nrot_invertiert (bool): ', bool, default=False),
        'gruen_invertiert': validiere_input('Soll die grüne Farbkomponente invertiert werden?\ngruen_invertiert (bool): ', bool, default=True),
        'blau_invertiert': validiere_input('Soll die blaue Farbkomponente invertiert werden?\nblau_invertiert (bool): ', bool, default=True),
        'frames': validiere_input('Die Anzahl der Frames.\nframes (int >= 1): ', int, min=1, default=200),
        'interval': validiere_input('Das Interval zwischen den Frames.\ninterval (int >= 1): ', int, min=1, default=200)
    }

    dateiname = input('Dateiname für die Speicherung der Parameter: ')
    if dateiname == '':
        dateiname = 'params'
    pfad = os.path.join('params', f'{dateiname}.json')
    try:
        with open(pfad, 'w') as f:
            json.dump(params, f)
        print(f"Parameter erfolgreich gespeichert unter {pfad}")
    except Exception as e:
        print(f"Fehler beim Speichern der Parameter: {e}")
        return None

    return pfad


def extrahiere_parameter(params):
    """
    Extrahiert Parameter aus einem Wörterbuch.

    Args:
        params (dict): Ein Wörterbuch mit den Parametern für das Bild.

    Returns:
        tuple: Ein Tupel, das alle extrahierten Parameter enthält.
    """
    return (params[key] for key in ('breite', 'hoehe', 't', 'scale_x', 'scale_y', 'scale_t', 
                                    'octaves', 'persistence', 'lacunarity', 'repeatx', 'repeaty', 
                                    'repeatz', 'base', 'rot_scale', 'gruen_scale', 'blau_scale', 
                                    'rot_invertiert', 'gruen_invertiert', 'blau_invertiert'))

def generiere_perlin_rauschen(breite, hoehe, t, scale_x, scale_y, scale_t, octaves, persistence, 
                              lacunarity, repeatx, repeaty, repeatz, base):
    """
    Generiert ein 2D-Array mit Perlin-Rauschen.

    Args:
        breite (int): Die Breite des Rauschens.
        hoehe (int): Die Höhe des Rauschens.
        t (float): Der Zeitpunkt, für den das Rauschen generiert wird.
        scale_x (float): Der Skalierungsfaktor in x-Richtung.
        scale_y (float): Der Skalierungsfaktor in y-Richtung.
        scale_t (float): Der Skalierungsfaktor in der Zeitdimension.
        octaves (int): Die Anzahl der Oktaven für das Perlin-Rauschen.
        persistence (float): Die Persistenz für das Perlin-Rauschen.
        lacunarity (float): Die Lacunarität für das Perlin-Rauschen.
        repeatx (int): Die Wiederholungsperiode des Rauschens in x-Richtung.
        repeaty (int): Die Wiederholungsperiode des Rauschens in y-Richtung.
        repeatz (int): Die Wiederholungsperiode des Rauschens in der Zeitdimension.
        base (int): Ein Startwert für den Zufallsgenerator.

    Returns:
        numpy.ndarray: Ein 2D-Array mit Perlin-Rauschen.
    """
    # Leeres Array für das Rauschen
    rauschen = np.zeros((hoehe, breite))

    # Fülle das Array mit Perlin-Rauschen
    for x in range(breite):
        for y in range(hoehe):
            # Generiere Perlin-Rauschen (Wert zwischen -1 und 1)
            n = noise.pnoise3(x*scale_x, y*scale_y, t*scale_t, octaves=octaves, persistence=persistence,
                              lacunarity=lacunarity, repeatx=repeatx, repeaty=repeaty, repeatz=repeatz, base=base)

            # Normalisiere auf [0, 1]
            rauschen[y, x] = (n + 1) / 2.0

    return rauschen

def generiere_bild(params):
    """
    Generiert ein Bild mit Perlin-Rauschen.

    Args:
        params (dict): Ein Wörterbuch mit den Parametern für das Bild.

    Returns:
        numpy.ndarray: Ein Array mit den Bildpixeln.
    """
    # Extrahiere die Parameter aus dem Wörterbuch
    breite, hoehe, t, scale_x, scale_y, scale_t, octaves, persistence, lacunarity, repeatx, repeaty, repeatz, base, \
    rot_scale, gruen_scale, blau_scale, rot_invertiert, gruen_invertiert, blau_invertiert = extrahiere_parameter(params)

    # Generiere Perlin-Rauschen
    rauschen = generiere_perlin_rauschen(breite, hoehe, t, scale_x, scale_y, scale_t, octaves, persistence, 
                                         lacunarity, repeatx, repeaty, repeatz, base)

    # Leeres Array für das Bild
    bild = np.zeros((hoehe, breite, 3))

    # Setze die Farben basierend auf dem Perlin-Rauschen
    for y in range(hoehe):
        for x in range(breite):
            n = rauschen[y, x]
            bild[y, x, 0] = (1 - n if rot_invertiert else n) * rot_scale  # Rot
            bild[y, x, 1] = (1 - n if gruen_invertiert else n) * gruen_scale  # Grün
            bild[y, x, 2] = (1 - n if blau_invertiert else n) * blau_scale  # Blau

    return bild

def aktualisiere_bild(i, params, im):
    """
    Aktualisiert das Bild für die Animation.

    Diese Funktion wird von der Animation für jedes Frame aufgerufen. Sie berechnet einen neuen Zeitpunkt `t` und generiert ein neues Bild mit diesem `t`.

    Args:
        i (int): Der Index des aktuellen Frames.
        params (dict): Ein Wörterbuch mit den Parametern für das Bild.
        im (matplotlib.image.AxesImage): Das aktuelle Bild der Animation.
    """
    # Berechne t mit einer Cosinus-Funktion, um eine Schleife zu erzeugen
    t = math.cos(i * 2 * math.pi / params['frames']) * 0.5

    # Aktualisiere `t` in den Parametern
    params['t'] = t

    # Generiere ein neues Bild mit dem aktuellen `t`
    bild = generiere_bild(params)

    # Aktualisiere das Bild der Animation
    im.set_array(bild)

def speichern_params(params, dateiname):
    """
    Speichert die Parameter in einer JSON-Datei.

    Args:
        params (dict): Ein Wörterbuch mit den Parametern.
        dateiname (str): Der Name der Datei, in der die Parameter gespeichert werden sollen.
    """
    with open(dateiname, 'w') as f:
        json.dump(params, f)

def laden_params(dateiname):
    """
    Lädt die Parameter aus einer JSON-Datei.

    Args:
        dateiname (str): Der Name der Datei, aus der die Parameter geladen werden sollen.

    Returns:
        dict: Ein Wörterbuch mit den geladenen Parametern.
    """
    with open(dateiname, 'r') as f:
        params = json.load(f)
    return params

def erstelle_und_speichere_animation(params, filepath):
    """
    Erstellt eine Animation basierend auf den gegebenen Parametern und speichert sie in einer Datei.

    Args:
        params (dict): Ein Wörterbuch mit den Parametern für die Animation.
        filepath (str): Der Pfad, unter dem die Animation gespeichert werden soll.
    """
    # Generiere ein Anfangsbild
    bild = generiere_bild(params)

    # Erstelle die Animation
    fig, ax = plt.subplots()
    im = ax.imshow(bild)
    ani = animation.FuncAnimation(fig, aktualisiere_bild, fargs=(params, im), frames=params['frames'], interval=params['interval'])

    # Speichern Sie die Animation in einer Datei
    ani.save(filepath, fps=30)

    print(f'{filepath} gespeichert')
	
def user_params_datei_auswahl():
    """
    Lässt den Benutzer eine Parameterdatei aus dem Ordner 'params' auswählen.

    Gibt den Dateinamen der ausgewählten Datei zurück.

    Returns:
        str: Der Pfad zur ausgewählten Datei.
    """
    files = glob('params/*.json')

    # Liste die Dateien auf
    for i, file in enumerate(files):
        print(f'{i}: {file}')

    while True:
        # Frage den Benutzer, welche Datei geladen werden soll
        print(f'Welche Datei soll geladen werden? (0 bis {len(files) - 1})')
        dateiauswahl = input('> ')

        # Validiere die Benutzereingabe
        if dateiauswahl.isdigit() and 0 <= int(dateiauswahl) < len(files):
            return files[int(dateiauswahl)]
        else:
            print("Ungültige Auswahl, bitte versuchen Sie es erneut.")
