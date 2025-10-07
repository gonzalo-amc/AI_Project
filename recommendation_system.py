def simple_validator(data):
    if not isinstance(data, dict):
        return False
    required_keys = ['name', 'email']
    for key in required_keys:
        if key not in data or not data[key]:
            return False
    return True