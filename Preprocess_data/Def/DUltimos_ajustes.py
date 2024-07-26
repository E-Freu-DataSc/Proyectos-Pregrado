import pandas as pd

def Ultimos_ajustes(Data):
    Data['date_of_birth_gold'] = pd.to_datetime(Data['date_of_birth_gold'], errors='coerce')
    Data['date_of_birth'] = pd.to_datetime(Data['date_of_birth'], errors='coerce')

    Data.loc[Data['sexual_orientation'] == 'Na', 'sexual_orientation'] = 'Straight'
    Data.loc[Data['person'] == 'Christoph_Waltz', ['date_of_birth_gold', 'date_of_birth']] = '4-Oct-1956'
    Data.loc[Data['person'] == 'Christoph_Waltz', ['birthplace', 'birthplace_gold']] = "Vienna_Austria"
    
    return Data
    
    