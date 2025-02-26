# Lochauswertung

## Funktionsweise
Das Programm wertet die von ImageJ generierten Rohdaten zur Lochanteilanalyse aus.  
Dabei werden für jede Probe sowie für den gesamten Parametersatz folgende statistische Kennzahlen berechnet:

- Mittelwert
- Minimalwert
- Maximalwert
- +yErorr (positiver Fehlerbalken)
- -yErorr (negativer Fehlerbalken)
- Standardabweichung

Die Ergebnisse werden als CSV-Dateien im Unterordner `/data` abgelegt und zusätzlich in einem separaten Ordner `/Auswertungsergebnisse_Python` gespeichert.

## Nutzung des Skripts
### Eingabedaten
- Das Skript erwartet CSV-Dateien aus ImageJ mit den Spalten `"Slice"` und `"%Area"`.
- Die Dateien müssen sich im Unterordner `/data` befinden.
- Da am Ende alle Rohdaten in einem Batch zusammengefasst und ausgeweret werden, sollten nur Rohdaten des gleichen Parametersatzes auf einmal ausgewertet werden.

### Ausführung
1. Stelle sicher, dass sich die zu analysierenden CSV-Dateien im Verzeichnis `/data` befinden.
2. Starte das Skript `lochauswertung.py`
3. Das Skript wertet automatisch alle CSV-Dateien im /data-Ordner aus und erstellt eine Gesamtübersicht der Ergebnisse.
4. Die fertigen Auswertungen werden in /Auswertungsergebnisse_Python als CSV-Datei gespeichert.
### Ausgabe
- Für jede einzelne Datei wird eine Statistik berechnet.
- Zusätzlich wird eine Übersicht aller Messwerte als Batch-Auswertung erstellt.
- Die Ergebnisse werden in einer CSV-Datei mit dem Namen {Batchname}-Gesamtübersicht.csv gespeichert.