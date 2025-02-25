import pandas as pd
import folium
import os

def create_map_folium(data_path: str) -> folium.Map:  
        
        data = pd.read_csv(data_path, encoding="latin1")
        data['Coordinates'] = data['Coordinates'].apply(eval) 
        # Create a map using folium
        mapa = folium.Map(location=[34.0928092, -118.3286614], zoom_start=4)
        for index, row in data.iterrows():
            coords = row['Coordinates']
            lat, lon = coords[0], coords[1]
            popup_text = f"Lugar nacimiento: {row['birthplace']}<br>Premiado: {row['person']}<br>Año premiación: {row['year_of_award']}"
            folium.Marker([lat, lon], popup=folium.Popup(popup_text, max_width=300)).add_to(mapa)
        save_directory = r"C:\Users\Usuario\OneDrive - udd.cl\Datos adjuntos\Bootcamp ciencia de datos\Modulo 7\Proyecto_7_Organizacion_Presentación_Esteban_Freudenberg_UDD\Github_Proyecto_7\Proyectos-Pregrado\Flask_Api\Deploy_Mapa_Oscars\templates"
        os.makedirs(save_directory, exist_ok=True)
        map_file_path = os.path.join(save_directory, 'mapa_premios_oscar.html')
        mapa.save(map_file_path)
        return mapa

def create_map_dash(data_path):
    
    data = pd.read_csv(data_path, encoding="latin1")
    data['Coordinates'] = data['Coordinates'].apply(eval)  # Convert string representation of list to actual list
    data[['lat', 'lon']] = pd.DataFrame(data['Coordinates'].tolist(), index=data.index)

    # Create a dashboard using Dash
    fig = px.scatter_mapbox(data, lat='lat', lon='lon', hover_name='person', hover_data={'lat': False, 'lon': False, 'birthplace': True, 'year_of_award': True}, zoom=4, height=600)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    app = dash.Dash(__name__)
    app.layout = html.Div([
        html.H1("Mapa de Premios Oscar"),
        dcc.Graph(figure=fig)
    ])
    if __name__ == '__main__':
        app.run_server(debug=True)