# Librerias
import json

class Usuario:
    """ Clase que representa el objeto Usuario con su información básica.
    """
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        """ Metodo que inicializa una nueva instancia de Usuario.

        Args:
            nombre (str): Cadena de texto correspondiente al nombre del usuario.
            apellido (str): Cadena de texto correspondiente al apellido del usuario.
            email (str): Cadena de texto correspondiente al correo del usuario.
            genero (str): Cadena de texto correspondiente al genero del usuario.
        """
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

def main():
    """
    Funcion que ejecuta el código.
    """
    usuarios = []
    # Lectura del archivo txt y almacenamiento del texto.
    with open('usuarios.txt', 'r') as archivo_usuarios:
        for linea in archivo_usuarios:
            try:
                datos_usuario = json.loads(linea)
                usuario = Usuario(**datos_usuario)
                usuarios.append(usuario)
            except Exception as e:
                with open('error.log', 'a') as archivo_log:
                    archivo_log.write(f'Error al procesar la línea: {linea}\nExcepción: {str(e)}\n')

    # Impresión de las instancias para verificación.
    for usuario in usuarios:
        print(f'Nombre: {usuario.nombre}, Apellido: {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}')

# Test unitario.
if __name__ == '__main__':
    main()
