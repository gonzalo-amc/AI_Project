# Código generado por Copilot basado en un prompt de validación.

def validar_datos_usuario(data):
    """
    Valida que el objeto de datos sea un diccionario y 
    que contenga las claves 'name' y 'email' con valores no vacíos.
    """
    if not isinstance(data, dict):
        return False
        
    required_keys = ['name', 'email']
    
    for key in required_keys:
        if key not in data or not data[key]:
            return False
            
    return True

# Uso de ejemplo:
# valido = validar_datos_usuario({'name': 'Alice', 'email': 'a@example.com'})