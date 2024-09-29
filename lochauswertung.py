import os
from pathlib import Path
import pandas as pd
import numpy as np

from pathlib import Path

def ergebnisordner_erstellen(basispfad: Path) -> Path:
    """
    Creates a folder for storing evaluation results.

    Parameters:
        basispfad (Path): The base path where the folder will be created.

    Returns:
        Path: The path of the created folder.
    """
    ordnerpfad: Path = basispfad / "Auswertungsergebnisse_Python"
    ordnerpfad.mkdir(exist_ok=True)
    return ordnerpfad

import os
from pathlib import Path

def navigiere_zu_unterordner(zielordner: str) -> None:
    """
    Navigates to the specified subfolder from current working directory.

    Args:
        zielordner (str): The name of the subfolder to navigate to.

    Returns:
        None
    """
    ordnerpfad: Path = Path.cwd() / zielordner
    os.chdir(ordnerpfad)
    return

def auswertung_ImageJ(daten:pd.DataFrame)-> pd.DataFrame:

    parameter: str = dateiname.split(".")[0]
    mittelwert: float = daten["%Area"].mean()
    minimalwert: float = daten["%Area"].min()
    maximalwert: float = daten["%Area"].max()
    positiverFehlerbalken: float = maximalwert - mittelwert
    negativerFehlerbalken: float = mittelwert - minimalwert
    standardabweichung: float = daten["%Area"].std()
    return pd.DataFrame({"Parameter":[parameter], "Mittelwert":[mittelwert], "Minimalwert":[minimalwert], "Maximalwert":[maximalwert],"+yEr":positiverFehlerbalken ,"-yEr":negativerFehlerbalken,"Standardabweichung":[standardabweichung]})

def auswertung_batchdaten(daten: pd.DataFrame, batchname: str) -> pd.DataFrame:

    mittelwert: float = daten["%Area"].mean()
    minimalwert: float = daten["%Area"].min()
    maximalwert: float = daten["%Area"].max()
    positiverFehlerbalken: float = maximalwert - mittelwert
    negativerFehlerbalken: float = mittelwert - minimalwert  
    standardabweichung: float = daten["%Area"].std()
    return pd.DataFrame({"Parameter": [batchname], "Mittelwert":[mittelwert], "Minimalwert":[minimalwert], "Maximalwert":[maximalwert],"+yEr":positiverFehlerbalken ,"-yEr":negativerFehlerbalken,"Standardabweichung":[standardabweichung]})

if __name__=="__main__":
    # Pfad zu den Auswertungsdateien
    basispfad: Path = Path.cwd()
    ergebnisordnerpfad: Path = ergebnisordner_erstellen(basispfad)
    navigiere_zu_unterordner("data")
    ordnerinhalt: list = os.listdir()

    gesamtUebersicht = pd.DataFrame(columns=["Parameter", "Mittelwert", "Minimalwert", "Maximalwert","+yEr", "-yEr", "Standardabweichung"])
    batchdaten: pd.DataFrame = pd.DataFrame(columns=["Slice", "%Area"])
    for dateiname in ordnerinhalt:
        # Daten lesen & auswerten
        daten: pd.DataFrame = pd.read_csv(dateiname)
        batchdaten = pd.concat([batchdaten, daten[["Slice","%Area"]]], ignore_index=True)
        ergebnisse: pd.DataFrame = auswertung_ImageJ(daten)
        gesamtUebersicht = pd.concat([gesamtUebersicht,ergebnisse], ignore_index=True)
        print(f"Datei {dateiname} wurde ausgewertet.")
    
    # Batchdaten auswerten
    batchname: str = ordnerinhalt[0].split("-")[0]+"-"+ordnerinhalt[0].split("-")[-1].split(".")[0]
    ergebnis_batchdaten: pd.DataFrame = auswertung_batchdaten(batchdaten,batchname)
    gesamtUebersicht = pd.concat([gesamtUebersicht,ergebnis_batchdaten], ignore_index=True)
    
    # Ergebnisse speichern
    os.chdir(ergebnisordnerpfad)
    gesamtUebersicht.to_csv(batchname+"-Gesamtübersicht.csv",index=False)