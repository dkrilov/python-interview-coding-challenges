import requests
import pytest


def test_fuzz_malformed_json():
    malformed = '{"sensorId": "abc123", "reading": 23.4'  # missing closing }
    response = requests.post('http://api.aetheos.com/v1/telemetry', data=malformed, headers={'Content-Type': 'application/json'})
    assert response.status_code in (400, 422), f'Expected 400 or 422, got {response.status_code}'


def test_fuzz_large_payload():
    large_payload = '{"sensorId": "abc123", "reading": ' + '0.1' * 10000 + '}'  # very large reading
    response = requests.post(
        'http://api.aetheos.com/v1/telemetry', data=large_payload, headers={'Content-Type': 'application/json'}
    )
    assert response.status_code in (400, 413), f'Expected 400 or 413, got {response.status_code}'


def test_fuzz_invalid_data_type():
    data = '<invalid>data</invalid>'  # not valid JSON
    response = requests.post('http://api.aetheos.com/v1/telemetry', data=data, headers={'Content-Type': 'application/json'})
    assert response.status_code in (400, 415), f'Expected 400 or 415, got {response.status_code}'


def test_fuzz_sql_injection():
    sql_injection = '{"sensorId": "abc123", "reading": "1; DROP TABLE sensors;"}'
    response = requests.get(
        'http://api.aetheos.com/v1/telemetry', data=sql_injection, headers={'Content-Type': 'application/json'}
    )
    assert response.status_code in (400, 422), f'Expected 400 or 422, got {response.status_code}'
