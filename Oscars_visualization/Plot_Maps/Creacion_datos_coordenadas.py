import pandas as pd

def añadir_coordenadas(oscar_df: pd.DataFrame) -> pd.DataFrame:
    "Creacion de 1 columna que las coordenadas de cada lugar de nacimiento"
    coordinates_dict = {
        'Port_Talbot_Wales': (51.5912, -3.7800),
        'East_Harlem_New_York_City': (40.7947, -73.9422),
        'Concord_Ca': (37.9779, -122.0311),
        'Long_Beach_Ca': (33.7701, -118.1937),
        'Toowoomba_Queensland_Australia': (-27.5610, 151.9530),
        'Misericordia_Arezzo_Tuscany_Italy': (43.4632, 11.8795),
        'South_Orange_Nj': (40.7492, -74.2611),
        'Burbank_Ca': (34.1808, -118.3089),
        'Terrell_Tx': (32.7357, -96.2753),
        'Fairport_Ny': (43.1001, -77.4179),
        'Longview_Tx': (32.5007, -94.7405),
        'Grayshott_Hampshire_England': (51.1152, -0.7457),
        'RueilMalmaison_HautsDeSeine_France': (48.8760, 2.1820),
        'Uvalde_Tx': (29.2097, -99.7861),
        'Swampscott_Ma': (42.4709, -70.9196),
        'Elizabeth_Nj': (40.6631, -74.2107),
        'Walters_Ok': (34.3626, -98.3052),
        'Savannah_Ga': (32.0836, -81.0998),
        'Dublin_Ireland': (53.3498, -6.2603),
        'North_Sydney_Nova_Scotia_Canada': (46.2487, -60.2519),
        'Vale_of_Glamorgan_Wales': (51.4274, -3.2694),
        'Toronto_Ontario_Canada': (43.6511, -79.3830),
        'Lima_Oh': (40.7421, -84.1052),
        'St_Petersburg_Russia': (59.9343, 30.3351),
        'Chihuahua_Mexico': (28.6353, -106.0889),
        'Hoboken_Nj': (40.7434, -74.0324),
        'Hunt_City_Il': (39.6797, -88.5289),
        'Marian_Glas_Anglesey_Wales': (53.3554, -4.2445),
        'Norwood_Oh': (39.1542, -84.4513),
        'Hartford_Ct': (41.7658, -72.6734),
        'Macon_Ga': (32.8407, -83.6324),
        'Bronx_Ny': (40.8448, -73.8648),
        'Malden_Ma': (42.4251, -71.0662),
        'St_Cloud_Mn': (45.5579, -94.1632),
        'Felixstowe_Suffolk_England': (51.9634, 1.3512),
        'Shidler_Ok': (36.8576, -96.6670),
        'Cleveland_Oh': (41.4993, -81.6944),
        'Bucharest_Romania': (44.4268, 26.1025),
        'Astoria_Ny': (40.7644, -73.9235),
        'Malibu_Ca': (34.0259, -118.7798),
        'Samrong_Young_Cambodia': (11.5350, 104.9247),
        'Kenosha_Wi': (42.5847, -87.8212),
        'Bermondsey_England': (51.4975, -0.0800),
        'Edinburgh_Scotland': (55.9533, -3.1883),
        'St_Louis_Mo': (38.6270, -90.1994),
        'Newark_Nj': (40.7357, -74.1724),
        'Lattimer_Mines_Pa': (40.9832, -75.9666),
        'San_Saba_Tx': (31.1965, -98.7170),
        'Laurel_Ne': (42.3947, -97.0991),
        'Lincoln_Lincolnshire_England': (53.2307, -0.5407),
        'West_Covina_Ca': (34.0686, -117.9389),
        'Memphis_Tn': (35.1495, -90.0490),
        'Lexington_Ky': (38.0406, -84.5037),
        'Las_Palmas_De_Gran_Canaria_Canary_Islands': (28.1248, -15.4340),
        'Perth_Australia': (-31.9505, 115.8605),
        'Haverfordwest_Pembrokeshire_Wales': (51.8020, -4.9710),
        'Bossier_City_La': (32.5150, -93.7321),
        'Montreal_Quebec_Canada': (45.5017, -73.5673),
        'Cobourg_Ontario_Canada': (43.9598, -78.1652),
        'Lowell_Ma': (42.6334, -71.3162),
        'Dusseldorf_Germany': (51.2277, 6.7735),
        'Darjeeling_India': (27.0478, 88.2636),
        'Independence_Mo': (39.0911, -94.4155),
        'Tulsa_Ok': (36.1540, -95.9928),
        'Stockholm_Sweden': (59.3293, 18.0686),
        'San_Antonio_Tx': (29.4241, -98.4936),
        'St_Joseph_Mo': (39.7675, -94.8467),
        'Brussels_Belgium': (50.8503, 4.3517),
        'Rome_Italy': (41.9028, 12.4964),
        'Thomasville_Ga': (30.8368, -83.9787),
        'Wiesbaden_Germany': (50.0782, 8.2398),
        'Pozzuoli_Italy': (40.8223, 14.1097),
        'Packard_Ky': (37.6889, -83.3037),
        'WaltononThames_Surrey_England': (51.3854, -0.4162),
        'Chabua_Assam_India': (27.4833, 95.1833),
        'Ilford_Essex_England': (51.5560, 0.0781),
        'Birkenhead_Cheshire_England': (53.3880, -3.0326),
        'Birmingham_Al': (33.5207, -86.8025),
        'Bascom_Fl': (30.8383, -85.1047),
        'Quitman_Tx': (32.7966, -95.4435),
        'Summit_Nj': (40.7159, -74.3646),
        'Kirksville_Mo': (40.1948, -92.5833),
        'Morton_Grove_Il': (42.0406, -87.7825),
        'El_Centro_Ca': (32.7920, -115.5631),
        'Conyers_Ga': (33.6676, -84.0177),
        'Cloquet_Mn': (46.7219, -92.4618),
        'Queens_Ny': (40.7282, -73.7949),
        'Culver_City_Ca': (34.0219, -118.3965),
        'Lincoln_Ne': (40.8136, -96.7026),
        'Smyrna_Ga': (33.8834, -84.5144),
        'Honolulu_Hi': (21.3069, -157.8583),
        'Benoni_South_Africa': (-26.1885, 28.3200),
        'New_Orleans_La': (29.9511, -90.0715),
        'Chiswick_London_England': (51.4892, -0.2610),
        'Reading_England': (51.4543, -0.9781),
        'Arlington_Va': (38.8816, -77.0910),
        'Jerusalem_Israel': (31.7683, 35.2137),
        'Louisville_Ky': (38.2527, -85.7585),
        'Melbourne_Victoria_Australia': (-37.8136, 144.9631),
        'Litchfield_Mn': (45.1276, -94.5265),
        'Wichita_Ks': (37.6872, -97.3301),
        'Palmyra_Mo': (39.7947, -91.5225),
        'Quincy_Il': (39.9356, -91.4099),
        'Athens_Greece': (37.9838, 23.7275),
        'Michigan_City_In': (41.7075, -86.8950),
        'Joliet_Il': (41.5250, -88.0817),
        'Newtonville_Ma': (42.3523, -71.2071),
        'Denison_Ia': (42.0256, -95.3530),
        'Otaro_Hokkaido_Japan': (43.0621, 141.3544),
        'Bramhall_Cheshire_England': (53.3600, -2.1580),
        'Charleroi_Pa': (40.1726, -79.9940),
        'Humacao_Puerto_Rico': (18.1546, -65.8278),
        'Elmhurst_Ny': (40.7376, -73.8785),
        'Hastings_Ne': (40.5865, -98.3912),
        'Marblehead_Ma': (42.5001, -70.8578),
        'Quincy_Ma': (42.2529, -71.0023),
        'Silver_Spring_Md': (39.0046, -77.0369),
        'Des_Moines_Ia': (41.5910, -93.6037),
        'Old_Westbury_Ny': (40.7759, -73.5931),
        'Newport_Ar': (35.6048, -91.2826),
        'Troy_Ny': (42.7284, -73.6918),
        'Morristown_Nj': (40.7968, -74.4815),
        'Wareham_Ma': (41.7598, -70.7222),
        'Winnipeg_Manitoba_Canada': (49.8951, -97.1384),
        'Tenafly_Nj': (40.9254, -73.9625),
        'Athens_Ga': (33.9519, -83.3576),
        'York_North_Yorkshire_England': (53.9591, -1.0815),
        'Catskill_Mountains_Ny': (42.1957, -74.1332),
        'Mumbles_Wales': (51.5680, -3.9763),
        'Katy_Tx': (29.7858, -95.8244),
        'Madrid_Spain': (40.4168, -3.7038),
        'Woodlawn_Md': (39.3051, -76.7720),
        'Montgomery_Al': (32.3668, -86.3006),
        'Mexico_City_Mexico': (19.4326, -99.1332)
    }
    
    other_coordinates_dict = {
        'Location': [
            'Chisinau_Moldova', 'Glasgow_Scotland', 'Chicago_Il', 'Salt_Lake_City_Ut',
            'Bisacquino_Sicily_Italy', 'Cape_Elizabeth_Me', 'Los_Angeles_Ca',
            'Pasadena_Ca', 'Mulhouse_HautRhin_Alsace_France', 'Budapest_Hungary',
            'New_York_City', 'Sucha_Galicia_Austria', 'Istanbul_Turkey', 'Nevada_Mo',
            'WilkesBarre_Pa', 'Oakland_Ca', 'Vienna_Austria', 'Lawrence_Ks',
            'Croydon_Surrey_England', 'Winchester_In', 'Shipley_Yorkshire_England',
            'Berlin_Germany', 'St_Louis_Park_Mn', 'London_England', 'Tokyo_Japan',
            'Minneapolis_Mn', 'Detroit_Mi', 'CÌÁslav_Czechoslovakia', 'Oak_Park_Il',
            'Brooklyn_Ny', 'Waxahachie_Tx', 'Santa_Monica_Ca', 'Richmond_Va',
            'Cambridge_England', 'North_Bergen_Nj', 'Lafayette_In',
            'Parma_EmiliaRomagna_Italy', 'Baltimore_Md', 'Lynwood_Ca', 'Baldwin_Ny',
            'San_Francisco_Ca', 'Cincinnati_Oh', 'Peekskill_Ny',
            'Ryde_Isle_of_Wight_England', 'Kapuskasing_Ontario_Canada',
            'Reading_Berkshire_England', 'Atlanta_Ga', 'Duncan_Ok', 'Paris_France',
            'Wellington_New_Zealand', 'Pingtung_Taiwan', 'Flushing_Ny',
            'Manchester_England', 'San_Carlos_Ca', 'Rorschach_Switzerland',
            'Columbus_Oh', 'Philadelphia_Pa', 'Kansas_City_Mo',
            'Victoria_Hotel_Scarborough_Yorkshire_England', 'Cadiz_Oh',
            'Tunbridge_Wells_Kent_England', 'Lviv_Ukraine', 'Milwaukee_Wi',
            'Withington_Manchester_England', 'Indiana_Pa', 'Helena_Mt', 'Manhattan_Ny',
            'Tacoma_Wa', 'Neath_Wales', 'Racine_Wi', 'Richmond_Surrey_England',
            'Dorking_Surrey_England', 'Santurce_Puerto_Rico', 'Ofallon_Il', 'Omaha_Ne',
            'Hamden_Ct', 'Vladivostok_Russia', 'Evanston_Il', 'La_Jolla_Ca', 'Miami_Fl',
            'Huyton_Lancashire_England', 'Hurstpierpoint_West_Sussex_England',
            'Westhampton_Ny', 'Winterset_Ia', 'Wise_Va', 'San_Bernardino_Ca', 'Newton_Ma',
            'Mount_Vernon_Ny', 'South_Kensington_London_England', 'Yonkers_Ny',
            'Grand_Island_Ne', 'Scarborough_Yorkshire_England', 'San_Diego_Ca',
            'Pittsburgh_Pa', 'Washington_Dc', 'Shaker_Heights_Oh', 'New_Brunswick_Nj',
            'Cowes_Isle_of_Wight_England'
        ],
        'Coordinates': [
            [47.010452, 28.86381], [55.864237, -4.251806], [41.878113, -87.629799], [40.760779, -111.891047],
            [37.795041, 13.258076], [43.563484, -70.22682], [34.052235, -118.243683], [34.147785, -118.144515],
            [47.750839, 7.335888], [47.497913, 19.040236], [40.712776, -74.005974], [49.634785, 22.67423],
            [41.008237, 28.97836], [37.839333, -94.354869], [41.245914, -75.881307], [37.804363, -122.271111],
            [48.208354, 16.372504], [38.971669, -95.23525], [51.376165, -0.098234], [40.174554, -85.488863],
            [53.833333, -1.783333], [52.520008, 13.404954], [44.948333, -93.348611], [51.507351, -0.127758],
            [35.682839, 139.759455], [44.977753, -93.265011], [42.331429, -83.045753], [49.903761, 15.377264],
            [41.885031, -87.784502], [40.650002, -73.949997], [32.386433, -96.848331], [34.019394, -118.491191],
            [37.540726, -77.43605], [52.205276, 0.119167], [40.804283, -74.012083], [40.416702, -86.875286],
            [44.801485, 10.327903], [39.290386, -76.61219], [33.930293, -118.21146], [40.652954, -73.607159],
            [37.774929, -122.419418], [39.103119, -84.512016], [41.290387, -73.920857], [50.730548, -1.160299],
            [49.416668, -82.433334], [51.454514, -0.973168], [33.748997, -84.387985], [34.502303, -97.957813],
            [48.856613, 2.352222], [-41.28664, 174.77557], [22.681614, 120.481592], [40.764462, -73.831693],
            [53.480759, -2.242631], [37.504311, -122.261796], [47.477522, 9.482359], [39.961178, -82.998795],
            [39.952583, -75.165222], [39.099731, -94.578568], [54.283333, -0.4], [40.273703, -81.865104],
            [51.132377, 0.263695], [49.839684, 24.029717], [43.038902, -87.906471], [53.441143, -2.257355],
            [40.621212, -79.15295], [46.58976, -112.03912], [40.78343, -73.96625], [47.252877, -122.44429],
            [51.661385, -3.804017], [42.726131, -87.782852], [51.461311, -0.303742], [51.231049, -0.324404],
            [18.439216, -66.061967], [38.592323, -89.910989], [41.256535, -95.934502], [41.383878, -72.902606],
            [43.115536, 131.885485], [42.044738, -87.693046], [32.832811, -117.271272], [25.76168, -80.19179],
            [53.408371, -2.839239], [50.93824, -0.235722], [40.830132, -72.689713], [41.330863, -94.013631],
            [36.975942, -82.575234], [34.10834, -117.289765], [42.33698, -71.209221], [40.9126, -73.8371],
            [51.494067, -0.174604], [40.93121, -73.89875], [40.926395, -98.342013], [54.282879, -0.401187],
            [32.715736, -117.161087], [40.440624, -79.995888], [38.89511, -77.03637], [41.473942, -81.53767],
            [40.486217, -74.451817], [50.762069, -1.298]
        ]
    }
    
    # Create DataFrame with coordinates from coordinates_dict
    Coordenadas_1 = pd.DataFrame(list(coordinates_dict.items()), columns=['Location', 'Coordinates'])

    # Create DataFrame with coordinates from other_coordinates_dict
    Coordenadas_2 = pd.DataFrame(other_coordinates_dict)

    # Combine both DataFrames
    Coordenadas_1['Coordinates'] = Coordenadas_1['Coordinates'].apply(lambda x: list(x))
    Coordenadas_combinadas = pd.concat([Coordenadas_1, Coordenadas_2], ignore_index=True)

    # Map coordinates in the main DataFrame using 'birthplace' as the key
    oscar_df['Coordinates'] = oscar_df['birthplace'].map(Coordenadas_combinadas.set_index('Location')['Coordinates'])

    return oscar_df

