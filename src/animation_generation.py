import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import src.image_generation as image_generation

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
    bild = image_generation.generiere_bild(params)

    # Aktualisiere das Bild der Animation
    im.set_array(bild)

def erstelle_und_speichere_animation(params, filepath, figsize=(10,10)):
    """
    Erstellt eine Animation basierend auf den gegebenen Parametern und speichert sie in einer Datei.

    Args:
        params (dict): Ein Wörterbuch mit den Parametern für die Animation.
        filepath (str): Der Pfad, unter dem die Animation gespeichert werden soll.
    """
    # Generiere ein Anfangsbild
    bild = image_generation.generiere_bild(params)

    # Erstelle die Animation
    fig, ax = plt.subplots(figsize=figsize)  # Setzt die Größe des Subplots auf 6x6 Zoll
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)  # Entfernt die Ränder
    im = ax.imshow(bild)
    ax.axis('off')  # Schaltet die Achsen aus.
    
    ani = animation.FuncAnimation(fig, aktualisiere_bild, fargs=(params, im), frames=params['frames'], interval=params['interval'])

    # Speichern Sie die Animation in einer Datei
    ani.save(filepath, fps=30)

    print(f'{filepath} gespeichert')