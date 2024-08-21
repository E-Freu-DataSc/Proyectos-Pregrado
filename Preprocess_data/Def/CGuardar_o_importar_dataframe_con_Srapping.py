import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import numpy as np

# Lista de formatos de fecha
formatos = [
    '%Y-%m-%d %H:%M:%S',
    '%d-%b-%Y',
    '%d-%b-%y',
    '%Y-%m-%d'
]

def convertir_fecha(data: pd.DataFrame) -> pd.DataFrame:
    """
    Convierte las fechas en las columnas 'date_of_birth' y 'date_of_birth_gold' del DataFrame usando múltiples formatos.
    :param data: DataFrame que contiene las fechas a convertir.
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

def Guardar_o_importar_Srapping_fechas_nacimiento(data: pd.DataFrame) -> pd.DataFrame:
    """
    Guarda o importa las fechas de nacimiento, nacionalidad y género obtenidos mediante scraping.
    """ 
    processed_data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Espacio_Trabajo_Oscars\Proyectos-Pregrado\Data_used\processed"
    file_path = os.path.join(processed_data_path, "Scrapped.csv")
    
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
    else:
        data = actualizar_info(data, 'date_of_birth', 'Born')
        if 'Nationality' not in data.columns or data['Nationality'].isnull().any():
            data = actualizar_info(data, 'Nationality', 'Nationality')
        if 'gender' not in data.columns or data['gender'].isnull().any():
            data = actualizar_info(data, 'gender', 'Gender')
        os.makedirs(processed_data_path, exist_ok=True)
        data.to_csv(file_path, index=False)
    
    return data

def actualizar_info(data: pd.DataFrame, info_type: str, html_label: str) -> pd.DataFrame:
    """
    Realiza scraping de la información especificada (fecha de nacimiento, nacionalidad o género).
    :param data: DataFrame con los datos a actualizar.
    :param info_type: Tipo de información a actualizar (e.g., 'date_of_birth', 'Nationality', 'gender').
    :param html_label: Etiqueta HTML que precede la información en la página.
    :return: DataFrame con la información actualizada.
    """
    if info_type not in data.columns:
        data[info_type] = np.nan

    cols = ['biourl', 'person', info_type]
    for index, row in data[data[cols].isnull().any(axis=1)][cols].iterrows():
        url = row['biourl']
        person_name = row['person']
        try:
            response = requests.get(url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, "html.parser")
            if info_type == 'date_of_birth':
                # Caso especial para fecha de nacimiento
                paragraphs = soup.find_all("p")
                for paragraph in paragraphs:
                    if "Born:" in paragraph.get_text():
                        birth_info = paragraph.get_text().split("Born:")[1].split("Birthplace:")[0].strip()
                        data.loc[data['person'] == person_name, ['date_of_birth', 'date_of_birth_gold']] = birth_info, birth_info
                        print(f"Scraping successful for {person_name}, Date of Birth: {birth_info}")
                        break
            else:
                # Para otros tipos de información (nacionalidad, género)
                info_value = soup.find("b", string=f"{html_label}:").next_sibling.strip()
                data.loc[data['person'] == person_name, info_type] = info_value
                print(f"Scraping successful for {person_name}, {info_type.capitalize()}: {info_value}")

        except requests.RequestException as e:
            print(f"Error accessing the page {url} for {person_name}: {e}")
        except Exception as e:
            print(f"Error processing the data for {person_name}: {e}")
        
    return data

