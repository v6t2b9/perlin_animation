import utils.functions as func
import matplotlib.pyplot as plt

def main():
    """
    Hauptfunktion des Skripts.

    Initialisiert die Parameter, generiert ein Bild, zeigt es an, erstellt eine Animation und speichert sie in einer Datei.
    """
    
    auswahl = func.benutzer_parameter_abfrage()
    
    if auswahl == 'n':
        # User Eingabe zur Bestimmung der Parameter
        params_datei = func.benutzer_parameter_eingabe_und_speichern()
            
    else:
        # User Eingabe zur Auswahl der params Datei
        params_datei = func.user_params_datei_auswahl()

    # Laden Sie die Parameter aus der Datei
    params = func.laden_params(params_datei)

    # Speichern Sie die Parameter in einer Datei
    func.speichern_params(params, 'params/params.json')

    # Laden Sie die Parameter aus der Datei
    params = func.laden_params('params/params.json')

    # Generieren Sie ein Bild
    image = func.generiere_bild(params)

    # Zeige das Bild an
    plt.figure(figsize=(10, 10))  # Optional: Ändern Sie die Größe des Bildes, hier 10x10 Zoll.
    plt.imshow(image)
    plt.axis('off')  # Schaltet die Achsen aus.
    plt.show()

    # Erstelle und speichere die Animation
    func.erstelle_und_speichere_animation(params, 'export/animation.gif')

if __name__ == "__main__":
    main()