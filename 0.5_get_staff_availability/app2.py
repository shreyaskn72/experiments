# Check Staff Availability
def check_staff_availability(staff_id, start_time, end_time):
    url = f"{BASE_URL}/users/{staff_id}/calendar/getschedule"
    params = {
        'startTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'endTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'availabilityViewInterval': 15 # Interval in minutes
    }
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=params)
    data = response.json()
    availability = data.get('value', [])
    if availability:
        return True
    return False