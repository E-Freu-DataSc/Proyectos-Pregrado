import re

def limpiar_valor(valor) -> str:
    """
    Remove punctuation and replace spaces with underscores in a string.
    """
    if isinstance(valor, str):  # Check if valor is a string
        # Remove punctuation
        valor_sin_puntuacion = re.sub(r'[^\w\s]', '', valor)
        # Replace spaces with underscores
        valor_limpio = valor_sin_puntuacion.replace(' ', '_')
        return valor_limpio
    else:
        return valor