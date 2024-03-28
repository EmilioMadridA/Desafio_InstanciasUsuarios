import json

class Usuario:
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

def main():
    usuarios = []
    with open('usuarios.txt', 'r') as archivo_usuarios:
        for linea in archivo_usuarios:
            try:
                datos_usuario = json.loads(linea)
                usuario = Usuario(**datos_usuario)
                usuarios.append(usuario)
            except Exception as e:
                with open('error.log', 'a') as archivo_log:
                    archivo_log.write(f'Error al procesar la línea: {linea}\nExcepción: {str(e)}\n')

    # Opcional: imprimir las instancias de Usuario para verificar
    for usuario in usuarios:
        print(f'Nombre: {usuario.nombre}, Apellido: {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}')

if __name__ == '__main__':
    main()
