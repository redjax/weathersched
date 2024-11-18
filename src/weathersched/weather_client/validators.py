def validate_api_key(api_key: str) -> str:
    if api_key is None:
        raise ValueError("api_key cannot be None")
    if not isinstance(api_key, str):
        raise TypeError(f"api_key must be of type str. Got type: ({type(api_key)})")
    if api_key == "" or api_key == " ":
        raise ValueError("api_key cannot be empty")
    
    return api_key