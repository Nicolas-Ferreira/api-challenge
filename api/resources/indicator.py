from flask_restful import Resource, reqparse
from models.indicator import IndicatorModel

class IndicatorFilter(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'indicator_name',
        type=str,
        required=True,
        help="Bad used of 'indicator_name' field, must be a string"
    )
    parser.add_argument(
        'value',
        type=float,
        required=True,
        help="Bad used of 'value' field, must be a float"
    )

    def post(self):
        data = IndicatorFilter.parser.parse_args()
        if not IndicatorModel.find_by_name(data['indicator_name']):
            return {
                'message': "indicator with name '{}' do not exists".format(data['indicator_name'])
            }, 400

        return {
            'countries': [country.json() for country in IndicatorModel.query.filter(
                IndicatorModel.indicator_name == data['indicator_name'],
                IndicatorModel.value > data['value']
            ).all()]
        }
