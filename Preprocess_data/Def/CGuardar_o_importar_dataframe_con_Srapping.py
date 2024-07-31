import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def Guardar_o_importar_Srapping_fechas_nacimiento(data):
    processed_data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets_Usados_Guardados_y_final\processed"
    file_path = os.path.join(processed_data_path, "Scrapped.csv")
    
    if os.path.exists(file_path):
        # If the file exists, load it
        return pd.read_csv(file_path)
    else:
        # If the file doesn't exist, perform scraping and save the result
        updated_data = actualizar_fecha_nacimiento(data)
        
        # Ensure the directory exists
        os.makedirs(processed_data_path, exist_ok=True)
        
        # Save the updated data
        updated_data.to_csv(file_path, index=False)
        
        return updated_data

def actualizar_fecha_nacimiento(data):
    cols = ['biourl', 'person', 'date_of_birth', 'date_of_birth_gold']
    rows_to_update = data[data[cols].isnull().any(axis=1)][cols]
    
    for index, row in rows_to_update.iterrows():
        url = row['biourl']
        person_name = row['person']
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")
            
            for paragraph in paragraphs:
                text = paragraph.get_text()
                if "Born:" in text:
                    birth_info = text.split("Born:")[1].split("Birthplace:")[0].strip()
                    birth_date = birth_info.split(" ")[0]
                    data.loc[data['person'] == person_name, ['date_of_birth_gold', 'date_of_birth']] = birth_date, birth_date
                    break
        except requests.RequestException as e:
            print(f"Failed to access the page for {person_name}: {url}. Error: {e}")
    
    return data