import json
import requests

def check_if_reem(lat, lon, pk):
    url = f"https://eu1.locationiq.com/v1/reverse?key={pk}&lat={lat}&lon={lon}&format=json&"
    response = requests.get(url)
    if response.status_code == 200:  # Check if response is not empty
        try:
            if response.json().get('address') is not None:
                if response.json().get('address').get('suburb') is not None:
                    suburb = response.json().get('address').get('suburb')
                    if suburb == 'Al Reem Island':
                        return True, suburb
                    else:
                        return False, suburb
            else:
                return None, 'None Error'
        except json.JSONDecodeError:
            pass  # Ignore JSON decoding error
    else:
        return None, 'None Error'