import joblib
import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import folium
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
import os 

sys.path.append(r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado")

from Preprocess_data.Def.Guardar_o_importar_dataframe_con_Srapping import Guardar_o_importar_Srapping_fechas_nacimiento
from Preprocess_data.Def.Definir_remplazar_nulos_y_aplicar_datatime import Definir_remplazar_nulos_y_aplicar_datatime
from Preprocess_data.Def.eliminar_puntuacion_y_espacios_a_guion_bajo import eliminar_puntuacion_y_espacios_a_guion_bajo
from Preprocess_data.Def.Ultimos_ajustes import Ultimos_ajustes
class DataProcessor:
    """
    Methods
    -------
    preprocess_data():
        Preprocess the data.
    """

    def __init__(self, data_path):
        self.data_path = data_path
        self.processed_data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets\processed\Oscars-demographics-DFE-updated_to_Scrapping.csv"
        self.data = None
        self.categorical_columns = ["_golden", "_unit_state", "_trusted_judgments", "birthplace", "date_of_birth", "race_ethnicity", "sexual_orientation", "year_of_award", "award", "biourl", "birthplace_gold", "date_of_birth_gold", "movie", "person", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"]
        
    def preprocess_data(self):
        self.data = pd.read_csv(self.data_path, encoding="latin1")
       
        columnas_a_limpiar = ['birthplace', 'race_ethnicity', 'religion', 'birthplace_gold', 'date_of_birth_gold', 'movie', 'person', 'race_ethnicity_gold', 'religion_gold', 'sexual_orientation_gold', 'award']
        for columna in columnas_a_limpiar:
            self.data[columna] = self.data[columna].apply(eliminar_puntuacion_y_espacios_a_guion_bajo)

        self.data = Definir_remplazar_nulos_y_aplicar_datatime(self.data)    
        self.data = Guardar_o_importar_Srapping_fechas_nacimiento(self.data, self.processed_data_path)
        self.data = Ultimos_ajustes(self.data)
        

if __name__ == "__main__":
    data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets\raw\Oscars-demographics-DFE.csv"
    processor = DataProcessor(data_path)
    processor.preprocess_data()
    

