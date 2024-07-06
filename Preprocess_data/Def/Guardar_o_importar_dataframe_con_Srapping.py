import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def Guardar_o_importar_Srapping_fechas_nacimiento(data, processed_data_path):
    if os.path.exists(processed_data_path):
        data = pd.read_csv(processed_data_path, encoding="latin1")
    else:
        data = actualizar_fecha_nacimiento(data)
        data.to_csv(processed_data_path, index=False)
    return data

def actualizar_fecha_nacimiento(data):
    cols = ['biourl', 'person', 'date_of_birth', 'date_of_birth_gold']
    for index, row in data[data[cols].isnull().any(axis=1)][cols].iterrows():
        url = row['biourl']
        person_name = row['person']
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = soup.find_all("p")
            for paragraph in paragraphs:
                if "Born:" in paragraph.get_text():
                    birth_info = paragraph.get_text().split("Born:")[1].split("Birthplace:")[0].strip()
                    birth_date = birth_info.split(" ")[0]
                    data.loc[data['person'] == person_name, ['date_of_birth_gold', 'date_of_birth']] = birth_date, birth_date
                    break
        else:
            print("No se pudo acceder a la página:", url)
    return data