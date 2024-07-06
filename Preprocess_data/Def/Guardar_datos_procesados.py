    # Guardar datos procesados
    save_paths = {
        "Oscars_Limpio.csv": ["_golden", "_unit_state", "birthplace_gold", "date_of_birth_gold", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"],
        "Oscars_gold.csv": ["_golden", "_unit_state", "birthplace_gold", "date_of_birth_gold", "race_ethnicity_gold", "sexual_orientation_gold", "year_of_award_gold"],
        "Oscars_para_graficos.csv": ["birthplace","date_of_birth","race_ethnicity","sexual_orientation","year_of_award","award","movie","person"],
        "Oscars_con_coordenadas.csv": ["birthplace","date_of_birth","race_ethnicity","sexual_orientation","year_of_award","award","movie","person","Coordinates"]
    }
    
    for filename, columns in save_paths.items():
        save_path = os.path.join(r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\proyecto_7\data\processed", filename)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        processor.data[columns].to_csv(save_path, index=False)