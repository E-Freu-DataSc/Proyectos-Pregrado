import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Lista de formatos de fecha
formatos = [
    '%Y-%m-%d %H:%M:%S',
    '%d-%b-%Y',
    '%d-%b-%y',
    '%Y-%m-%d'
]
def convertir_fecha(data):
    """
    Convierte las fechas en las columnas 'date_of_birth' y 'date_of_birth_gold' del DataFrame usando múltiples formatos.
    :param df: DataFrame que contiene las fechas a convertir.
    :return: DataFrame con las fechas convertidas.
    """
    columnas = ['date_of_birth', 'date_of_birth_gold']
    
    def convert(fecha):
        for formato in formatos:
            try:
                return pd.to_datetime(fecha, format=formato)
            except (ValueError, TypeError):
                continue
        return pd.NaT
    
    for columna in columnas:
        data[columna] = data[columna].apply(convert)
    
    return data

# Función para guardar o importar fechas de nacimiento scrapeadas
def Guardar_o_importar_Srapping_fechas_nacimiento(data):
    processed_data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Data_used\processed"
    file_path = os.path.join(processed_data_path, "Scrapped.csv")
    
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        updated_data = actualizar_fecha_nacimiento(data)
        os.makedirs(processed_data_path, exist_ok=True)
        updated_data.to_csv(file_path, index=False)
        return updated_data

# Función para actualizar las fechas de nacimiento mediante scraping
def actualizar_fecha_nacimiento(data):
    cols = ['biourl', 'person', 'date_of_birth', 'date_of_birth_gold']
    for index, row in data[data[cols].isnull().any(axis=1)][cols].iterrows():
        url = row['biourl']
        person_name = row['person']
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")
            
            for paragraph in paragraphs:
                if "Born:" in paragraph.get_text():
                    birth_info = paragraph.get_text().split("Born:")[1].split("Birthplace:")[0].strip()
                    birth_date = birth_info.split(" ")[0]
                    data.loc[data['person'] == person_name, ['date_of_birth_gold', 'date_of_birth']] = birth_date, birth_date
                    break
        except requests.RequestException as e:
            print(f"Error accessing the page {url}: {e}")
        except Exception as e:
            print(f"Error processing the data for {person_name}: {e}")
        
    return data
