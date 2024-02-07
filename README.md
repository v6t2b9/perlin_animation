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

## Parameter

- **breite**: Die Breite des generierten Rauschens in Pixeln. Muss größer oder gleich 1 sein. Bestimmt die horizontale Größe des Ausgabebildes.

- **hoehe**: Die Höhe des generierten Rauschens in Pixeln. Muss größer oder gleich 1 sein. Bestimmt die vertikale Größe des Ausgabebildes.

- **t**: Der Zeitpunkt, für den das Rauschen generiert wird. Dies ermöglicht die Erzeugung von animiertem Rauschen, indem für jeden Frame ein anderer Wert verwendet wird.

- **scale_x**: Der Skalierungsfaktor in x-Richtung. Ein höherer Wert bewirkt eine "zoom-in"-Effekt, während ein niedrigerer Wert eine feinere, detailliertere Textur erzeugt.

- **scale_y**: Der Skalierungsfaktor in y-Richtung. Funktioniert ähnlich wie `scale_x`, aber für die vertikale Dimension.

- **scale_t**: Der Skalierungsfaktor in der Zeitdimension. Beeinflusst die Geschwindigkeit der Änderungen zwischen den Frames bei animiertem Rauschen.

- **octaves**: Die Anzahl der Oktaven für das Perlin-Rauschen. Mehr Oktaven führen zu einer komplexeren und detaillierteren Textur.

- **persistence**: Die Persistenz für das Perlin-Rauschen. Ein niedrigerer Wert führt zu einem schnellen Abfall der Amplitude mit jeder Oktave, was eine glattere Textur erzeugt.

- **lacunarity**: Die Lacunarität für das Perlin-Rauschen. Bestimmt den Abstand zwischen den einzelnen Oktaven. Ein höherer Wert führt zu einer "raueren" Textur.

- **repeatx**: Die Wiederholungsperiode des Rauschens in x-Richtung. Ermöglicht die Erzeugung eines nahtlosen Musters durch Wiederholung des Rauschens.

- **repeaty**: Die Wiederholungsperiode des Rauschens in y-Richtung. Funktioniert wie `repeatx`, aber für die vertikale Dimension.

- **repeatz**: Die Wiederholungsperiode des Rauschens in der Zeitdimension. Ermöglicht die Wiederholung des animierten Rauschens, sodass es endlos abgespielt werden kann.

- **base**: Ein Startwert für den Zufallsgenerator. Durch Verwendung des gleichen Wertes kann das gleiche Rauschen reproduziert werden.

- **rot_scale**: Der Skalierungsfaktor für die rote Farbkomponente. Bestimmt die Intensität der roten Farbe im Rauschen.

- **gruen_scale**: Der Skalierungsfaktor für die grüne Farbkomponente. Bestimmt die Intensität der grünen Farbe im Rauschen.

- **blau_scale**: Der Skalierungsfaktor für die blaue Farbkomponente. Bestimmt die Intensität der blauen Farbe im Rauschen.

- **rot_invertiert**: Gibt an, ob die rote Farbkomponente invertiert werden soll. Dies kehrt die Intensität der roten Farbe um.

- **gruen_invertiert**: Gibt an, ob die grüne Farbkomponente invertiert werden soll. Dies kehrt die Intensität der grünen Farbe um.

- **blau_invertiert**: Gibt an, ob die blaue Farbkomponente invertiert werden soll. Dies kehrt die Intensität der blauen Farbe um.

- **frames**: Die Anzahl der Frames für die Animation. Bestimmt die Gesamtlänge der Animation, wenn `t` verwendet wird.

- **interval**: Das Intervall zwischen den Frames in Millisekunden. Bestimmt die Geschwindigkeit der Animation.

## Verwendung

Passen Sie die Parameter an Ihre Bedürfnisse an, um das gewünschte Rauschen zu erzeugen. Diese können für visuelle Effekte, Terrain-Generierung in Spielen oder als Grundlage für weitere grafische Anwendungen dienen.


## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.

