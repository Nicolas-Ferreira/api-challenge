import pandas as pd
from models.indicator import IndicatorModel

def load_dataset():
    # Load data
    df = pd.read_csv('data/BLI_28032019144925238.csv')

    # Rename column names
    df.columns = [
        'id_country',
        'country_name',
        'id_indicador',
        'indicator_name',
        'id_measure',
        'measure_name',
        'id_inequality',
        'inequality_name',
        'unit_code',
        'unit',
        'powercode_code',
        'powercode',
        'reference_period_code',
        'reference_period',
        'value',
        'flag_codes',
        'flags'
    ]

    # Iterate over DF and insert objs in DB
    # This will be executed before first request, so it will make first request perform badly
    # For the purpose of this challenge DB improvements were left aside
    for index, row in df.iterrows():
        # Create new object
        new_indicator = IndicatorModel(
            row['id_country'],
            row['country_name'],
            row['id_indicador'],
            row['indicator_name'],
            row['id_measure'],
            row['measure_name'],
            row['id_inequality'],
            row['inequality_name'],
            row['unit_code'],
            row['unit'],
            row['powercode_code'],
            row['powercode'],
            row['reference_period_code'],
            row['reference_period'],
            row['value'],
            row['flag_codes'],
            row['flags']
        )
        # Save object to DB
        new_indicator.save_to_db()
