import re
def eliminar_puntuacion_y_espacios_a_guion_bajo(valor):
            if isinstance(valor, str):
                valor_sin_puntuacion = re.sub(r'[^\w\s]', '', valor)
                valor_limpio = valor_sin_puntuacion.replace(' ', '_')
                return valor_limpio
            else:
                 return valor