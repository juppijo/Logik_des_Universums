from bs4 import BeautifulSoup
import os

def strukturiere_html(datei_pfad):
    if not os.path.exists(datei_pfad):
        print(f"Oje, die Datei {datei_pfad} wurde nicht gefunden. 🐈")
        return

    try:
        # 1. Datei einlesen
        with open(datei_pfad, 'r', encoding='utf-8') as f:
            html_inhalt = f.read()

        # 2. BeautifulSoup nutzen, um die Struktur zu analysieren
        soup = BeautifulSoup(html_inhalt, 'html.parser')

        # 3. Den Code "schön" machen (Prettify)
        sauberer_html = soup.prettify()

        # 4. In einer neuen Datei speichern, damit das Original sicher bleibt
        neuer_dateiname = "sauber_" + datei_pfad
        with open(neuer_dateiname, 'w', encoding='utf-8') as f:
            f.write(sauberer_html)

        print(f"Fertig! Deine strukturierte Datei findest du hier: {neuer_dateiname} ✨")
        print("Jetzt sieht alles so ordentlich aus wie Zenjios Garten!")

    except Exception as e:
        print(f"Es gab einen kleinen Fehler: {e}")

# Beispielaufruf für deine Datei
if __name__ == "__main__":
    # Hier den Namen deiner Datei eintragen
    strukturiere_html('wrapper.html')