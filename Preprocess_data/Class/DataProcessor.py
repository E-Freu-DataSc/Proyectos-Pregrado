import os
import pandas as pd
from Preprocess_data.Def.CGuardar_o_importar_dataframe_con_Srapping import Guardar_o_importar_Srapping_fechas_nacimiento
from Preprocess_data.Def.BDefinir_remplazar_nulos_y_aplicar_datatime import Definir_remplazar_nulos_y_aplicar_datatime
from Preprocess_data.Def.AEliminar_puntuacion_y_espacios_a_guion_bajo import limpiar_valor
from Preprocess_data.Def.DUltimos_ajustes import Ultimos_ajustes
from Plot_Maps.Creacion_datos_coordenadas import añadir_coordenadas

class DataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.categorical_columns = ["_golden", "_unit_state", "_trusted_judgments", "birthplace", "date_of_birth", "race_ethnicity", "sexual_orientation", "year_of_award", "award", "biourl", "birthplace_gold", "date_of_birth_gold", "movie", "person", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"]
        self.processed_data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets_Usados_Guardados_y_final\processed"

    def preprocess_data(self):
        self.data = pd.read_csv(self.data_path, encoding="latin1")
        
        columnas_a_limpiar = ['birthplace', 'race_ethnicity', 'religion', 'birthplace_gold', 'date_of_birth_gold', 'movie', 'person', 'race_ethnicity_gold', 'religion_gold', 'sexual_orientation_gold', 'award']
        
        for columna in columnas_a_limpiar:
            if columna in self.data.columns:
                self.data[columna] = self.data[columna].apply(limpiar_valor)
        
        self.data = Definir_remplazar_nulos_y_aplicar_datatime(self.data)
        self.data = Guardar_o_importar_Srapping_fechas_nacimiento(self.data)
        self.data = Ultimos_ajustes(self.data)
        self.data = añadir_coordenadas(self.data)
        self.save_processed_data()

    def save_processed_data(self):
        """
        Save different subsets of the processed data to CSV files.
        """
        save_paths = {
            "Oscars_Limpio.csv": ["_golden", "_unit_state", "birthplace_gold", "date_of_birth_gold", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"],
            "Oscars_gold.csv": ["_golden", "_unit_state", "birthplace_gold", "date_of_birth_gold", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"],
            "Oscars_para_graficos.csv": ["birthplace", "date_of_birth", "race_ethnicity", "sexual_orientation", "year_of_award", "award", "movie", "person"],
            "Oscars_con_coordenadas.csv": ["birthplace", "date_of_birth", "race_ethnicity", "sexual_orientation", "year_of_award", "award", "movie", "person", "Coordinates"]
        }

        base_dir = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets_Usados_Guardados_y_final\processed"
        
        for filename, columns in save_paths.items():
            try:
                save_path = os.path.join(base_dir, filename)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                if all(col in self.data.columns for col in columns):
                    self.data[columns].to_csv(save_path, index=False)
                    print(f"Processed data saved successfully to: {save_path}")
                else:
                    missing_cols = [col for col in columns if col not in self.data.columns]
                    print(f"Warning: Missing columns {missing_cols} in the data. Skipping {filename}.")
            except Exception as e:
                print(f"An error occurred while saving {filename}: {e}")

if __name__ == "__main__":
    data_path = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Datasets_Usados_Guardados_y_final\raw\Oscars-demographics-DFE.csv"
    processor = DataProcessor(data_path)
    processor.preprocess_data()