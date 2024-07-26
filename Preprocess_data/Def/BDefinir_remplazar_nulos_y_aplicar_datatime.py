import pandas as pd
def Definir_remplazar_nulos_y_aplicar_datatime(self):
    self['year_of_award_gold'] = self['year_of_award_gold'].astype(str).str.replace(r'\.$', '', regex=True).fillna(pd.NA)
    self['year_of_award_gold'] = self['year_of_award_gold'].astype(float).astype('Int64').fillna(pd.NA)

    updates = {
        'Michael_Cimino': '3-Feb-1939', 'Danny_Boyle': '20-Oct-1956', 'Van_Heflin': '13-Dec-1910',
        'Jason_Robards': '26-Jul-1922', 'James_Coburn': '31-Aug-1928', 'Elizabeth_Taylor': '27-Feb-1932',
        'Maggie_Smith': '28-Dec-1934', 'Faye_Dunaway': '14-Jan-1941', 'Gwyneth_Paltrow': '27-Sep-1972',
        'Hilary_Swank': '30-Jul-1974', 'Mary_Astor': '3-May-1906', 'Angelina_Jolie': '4-Jun-1975',
        'Marcia_Gay_Harden': '14-Aug-1959', 'Rachel_Weisz': '7-Mar-1971', 'Hilary_Swank': '30-Jul-1974'
    }
    for person, dob in updates.items():
        self.loc[self['person'] == person, ['date_of_birth_gold', 'date_of_birth']] = dob

    # Creating masks for both False and True _golden values
        mask_false = (self["_golden"] == False)
        mask_true = (self["_golden"] == True)

        columns_to_update = ['date_of_birth', 'race_ethnicity', 'religion', 'birthplace', 'sexual_orientation', 'year_of_award']

        for column in columns_to_update:
            gold_column = f"{column}_gold"

            # Updating for _golden == False
            self.loc[mask_false & self[column].notnull(), gold_column] = self.loc[mask_false & self[column].notnull(), column]
            self.loc[mask_false & self[gold_column].notnull(), column] = self.loc[mask_false & self[gold_column].notnull(), gold_column]

            # Updating for _golden == True
            self.loc[mask_true & self[column].notnull(), gold_column] = self.loc[mask_true & self[column].notnull(), column]
            self.loc[mask_true & self[gold_column].notnull(), column] = self.loc[mask_true & self[gold_column].notnull(), gold_column]


    for column in columns_to_update:
        gold_column = f"{column}_gold"
        self[gold_column] = self[column]

    self['birthplace_gold'] = self['birthplace']
    self['date_of_birth_gold'] = self['date_of_birth']
    self['race_ethnicity_gold'] = self['race_ethnicity']
    self['religion_gold'] = self['religion']
    self['sexual_orientation_gold'] = self['sexual_orientation']
    self['year_of_award_gold'] = self['year_of_award']
    
    self['date_of_birth_gold'] = pd.to_datetime(self['date_of_birth_gold'], errors='coerce')
    self['date_of_birth'] = pd.to_datetime(self['date_of_birth'], errors='coerce')

    return self
