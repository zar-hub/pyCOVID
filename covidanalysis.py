"""FIle per analisi dei dati sull'epidemia COVID-19"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as matp

dati = pd.read_csv('covid.csv')

FVG = dati[dati["denominazione_regione"]=="Friuli Venezia Giulia"]
print(FVG)


