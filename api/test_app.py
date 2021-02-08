import unittest
import json
import pandas as pd
from flask import jsonify

import app

BASE_URL = 'http://127.0.0.1:5000/filter_country_by_indicator'


class TestIndicatorFilter(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_missing_indicator_name(self):
        indicator = {"value": 4}
        response = self.app.post(
            BASE_URL,
            data=json.dumps(indicator),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_missing_value(self):
        indicator = {"indicator_name": "Life satisfaction"}
        response = self.app.post(
            BASE_URL,
            data=json.dumps(indicator),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_dtype_indicator_name(self):
        indicator = {"value": "4"}
        response = self.app.post(
            BASE_URL,
            data=json.dumps(indicator),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_wrong_dtype_value(self):
        indicator = {"indicator_name": 1}
        response = self.app.post(
            BASE_URL,
            data=json.dumps(indicator),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_life_satisfaction_filter(self):
        # Load data from file
        df = pd.read_csv('data/BLI_28032019144925238.csv')
        expected = df[
            (df['Indicator'] == 'Life satisfaction') &
            (df['Value'] > 7.5)
        ]

        indicator = {"indicator_name": "Life satisfaction", "value": 7.5}
        response = self.app.post(
            BASE_URL,
            data=json.dumps(indicator),
            content_type='application/json'
        )
        data = response.get_json()
        self.assertEqual(len(data['countries']), len(expected.index))
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
