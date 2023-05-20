# Perlin-Rauschen-Animationsgenerator

Dieses Projekt verwendet Perlin-Rauschen, um einzigartige, organisch anmutende Animationen zu erzeugen. Mit einem Satz von Parametern, die in einer JSON-Datei definiert sind, wird eine Reihe von Bildern generiert und in eine Animation zusammengefügt, die als GIF-Datei gespeichert wird.

## Installationsanweisungen

1. Ein Klon des Repositories wird erstellt, indem der Befehl `git clone [repository URL]` ausgeführt wird.
2. In das Repository-Verzeichnis wird mit dem Befehl `cd [Verzeichnisname]` gewechselt.
3. Alle erforderlichen Python-Bibliotheken werden installiert, indem `pip install -r requirements.txt` ausgeführt wird.

## Ausführungsanleitung

1. Das Python-Skript `main.py` wird ausgeführt, um eine Animation mit den Standardparametern zu generieren.
2. Zur Anpassung der Parameter wird die Datei `params.json` geöffnet und bearbeitet. Die Parameter steuern verschiedene Aspekte der Animation, einschließlich der Größe, Farbgebung und der Komplexität des Perlin-Rauschens.
3. Nach der Anpassung der Parameter wird `main.py` erneut ausgeführt, um eine neue Animation zu generieren.
4. Die erzeugte Animation wird in einer GIF-Datei im `export`-Verzeichnis gespeichert.

## Dateistruktur

- `main.py`: Die Hauptausführungsdatei. Sie initialisiert die Parameter, generiert eine einzelne Bildvorschau, erstellt eine Animation und speichert sie in einer Datei.
- `utils/functions.py`: Enthält alle Funktionen, die zum Generieren von Perlin-Rauschen und zum Erstellen von Animationen benötigt werden.
- `params/params.json`: Eine JSON-Datei, in der die Parameter für die Animation gespeichert sind. Hier können Anpassungen vorgenommen werden, um die generierte Animation zu beeinflussen.
- `export/`: Das Verzeichnis, in dem die erzeugte GIF-Animation gespeichert wird.

## Perlin Noise Parameter

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

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.

