import requests
from settings import NOAA_NWS_URL, CONTACT_EMAIL

def grab_weather_alerts():
    url = f'{NOAA_NWS_URL}/alerts/active?status=actual&message_type=alert,update&region_type=land&severity=Extreme,Severe,Moderate&certainty=Observed,Likely,Possible'
    headers = {
        "Accept": "application/geo+json",
        "User-Agent": f"(WeatherAlertMap, {CONTACT_EMAIL})"
    }
    
    response = requests.get(url=url,headers=headers)
    
    if response.status_code == 200:
        return parse_nws_weather_alerts(response.json())
    else:
        return {"status": 'error'}


def parse_nws_weather_alerts(raw_data):
    alerts = []
    for f in raw_data.get('features',[]):
        if f.get('geometry',None) != None and f.get('geometry',{}).get('type','') == 'Polygon':
            alerts.append({
                "geometry": f.get('geometry'),
                "effective": f.get('properties',{}).get('effective',None),
                "expires": f.get('properties',{}).get('expires',None),
                "severity": f.get('properties',{}).get('severity',None),
                "certainty": f.get('properties',{}).get('certainty',None),
                "event": f.get('properties',{}).get('event',None),
                "headline": f.get('properties',{}).get('headline',None),
                "description": f.get('properties',{}).get('description',None)
            })
        else:
            continue

    data = {
        "alerts": alerts,
        "alerts_count": len(alerts),
        "status": "success"
    }
    
    return data

