import requests
from settings import NOAA_NWS_URL, CONTACT_EMAIL

def grab_weather_alerts():
    url = f'{NOAA_NWS_URL}/alerts/active?status=actual&message_type=alert,update&region_type=land&severity=Extreme,Severe,Moderate&certainty=Observed,Likely,Possible'
    headers = {
        "Accept": "application/geo+json",
        "User-Agent": f"(WeatherAlertMap, {CONTACT_EMAIL})"
    }

def parse_nws_weather_alerts(raw_data):
    pass
