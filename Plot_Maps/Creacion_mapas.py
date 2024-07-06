import pandas as pd
import folium
def create_map_folium(data_path: str):
        # Read the data
        data = pd.read_csv(data_path, encoding="latin1")
        # Assuming 'Coordinates' is a column with a list of [lat, lon]
        data['Coordinates'] = data['Coordinates'].apply(eval)  # Convert string representation of list to actual list

        # Create a map using folium
        mapa = folium.Map(location=[34.0928092, -118.3286614], zoom_start=4)
        for index, row in data.iterrows():
            coords = row['Coordinates']
            lat, lon = coords[0], coords[1]
            popup_text = f"Lugar nacimiento: {row['birthplace']}<br>Premiado: {row['person']}<br>Año premiación: {row['year_of_award']}"
            folium.Marker([lat, lon], popup=folium.Popup(popup_text, max_width=300)).add_to(mapa)
        mapa.save('mapa_premios_oscar.html')

def create_map_dash(data_path):
    # Read the data
    data = pd.read_csv(data_path, encoding="latin1")
    # Assuming 'Coordinates' is a column with a list of [lat, lon]
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