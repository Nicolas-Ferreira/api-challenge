from db import db

class IndicatorModel(db.Model):
    __tablename__ = 'indicators'

    id = db.Column(db.Integer, primary_key=True)
    id_country = db.Column(db.String(80))
    country_name = db.Column(db.String(80))
    id_indicador = db.Column(db.String(80))
    indicator_name = db.Column(db.String(80))
    id_measure = db.Column(db.String(80))
    measure_name = db.Column(db.String(80))
    id_inequality = db.Column(db.String(80))
    inequality_name = db.Column(db.String(80))
    unit_code = db.Column(db.String(80))
    unit = db.Column(db.String(80))
    powercode_code = db.Column(db.Integer)
    powercode = db.Column(db.String(80))
    reference_period_code = db.Column(db.Float(precision=2))
    reference_period = db.Column(db.Float(precision=2))
    value = db.Column(db.Float(precision=2))
    flag_codes = db.Column(db.String(80))
    flags = db.Column(db.String(80))

    def __init__(self, id_country, country_name, id_indicador, indicator_name, id_measure, measure_name,
        id_inequality, inequality_name, unit_code, unit, powercode_code, powercode, reference_period_code,
        reference_period, value, flag_codes, flags):
        self.id_country = id_country
        self.country_name = country_name
        self.id_indicador = id_indicador
        self.indicator_name = indicator_name
        self.id_measure = id_measure
        self.measure_name = measure_name
        self.id_inequality = id_inequality
        self.inequality_name = inequality_name
        self.unit_code = unit_code
        self.unit = unit
        self.powercode_code = powercode_code
        self.powercode = powercode
        self.reference_period_code = reference_period_code
        self.reference_period = reference_period
        self.value = value
        self.flag_codes = flag_codes
        self.flags = flags

    def json(self):
        return {
            'id': self.id,
            'id_country': self.id_country,
            'country_name': self.country_name,
            'id_indicador': self.id_indicador,
            'indicator_name': self.indicator_name,
            'id_measure': self.id_measure,
            'measure_name': self.measure_name,
            'id_inequality': self.id_indicador,
            'inequality_name': self.inequality_name,
            'unit_code': self.unit_code,
            'unit': self.unit,
            'powercode_code': self.powercode_code,
            'powercode': self.powercode,
            'reference_period_code': self.reference_period_code,
            'reference_period': self.reference_period,
            'value': self.value,
            'flag_codes': self.flag_codes,
            'flags': self.flags
        }

    @classmethod
    def find_by_name(cls, indicator_name):
        return cls.query.filter_by(indicator_name=indicator_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
