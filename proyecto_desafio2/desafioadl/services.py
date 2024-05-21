# Importa los modelos Tarea y SubTarea del modulo models.py
from .models import Tarea, SubTarea


# Función para recuperar todas las tareas y sus subtareas
def recupera_tareas_y_sub_tareas():
    ''' Función para recuperar las tareas y subtareas, devolviendo un diccionario en donde cada tarea tiene sus subtareas correspondientes'''
    tareas = Tarea.objects.all() # Obtiene todas las instancias de Tarea, guardandolas en la variable tareas.
    resultado = []  # inicializa una lista vacia para guardar el resultado
    for tarea in tareas: # Itera sobre cada tarea
        subtareas = tarea.subtareas.all() # Obtiene todas las subtareas relacionadas con la tarea correspondiente
        resultado.append({      # Añade un diccionario con la tarea y sus subtareas a la lista de resultados
            'tarea': tarea,
            'subtareas': list(subtareas)
        })
    return resultado # Devuelve la lista de diccionarios (tarea: [subtareas])

# Función para crear una nueva tarea
def crear_nueva_tarea(descripcion):
    ''' Crea una nueva tarea con la descripción proporcionada, devuelve el estado actualizado de tareas y subtareas'''
    Tarea.objects.create(descripcion=descripcion) # Crea una nueva tarea con la descripción proporcionada.
    return recupera_tareas_y_sub_tareas() # devuelve tareas y subtareas, reflejando cambios ssi es que los hay.

# Función para crear una nueva subtarea para una tarea especifica
def crear_sub_tarea(tarea_id, descripcion):
    '''Crea una nueva subtarea para una tarea especifica con la descripción proporcionada.'''
    tarea = Tarea.objects.get(id=tarea_id) # Obtiene la tarea (por su ID) en la cual agregaré la subtarea.
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion) # Crea una nueva subtarea para la tarea
    return recupera_tareas_y_sub_tareas() #devuelve las tareas y subtareas actualizadas.

# Función para marcar una tarea como eliminada
def elimina_tarea(tarea_id):
    '''Marca una tarea como eliminada.'''
    tarea = Tarea.objects.get(id=tarea_id) # Obtiene la tarea por su ID
    tarea.eliminada = True  # Marca la tarea como eliminada
    tarea.save()  # Guarda los cambios en la base de datos(se utiliza save ya que estamos modificando una instancia ya existente y debemos guardar los cambios realizados (en el caso de create los guarda automaticamente))
    return recupera_tareas_y_sub_tareas()

# Función para marcar una subtarea como eliminada
def elimina_sub_tarea(subtarea_id):
    '''Marca una subtarea como eliminada.'''
    subtarea = SubTarea.objects.get(id=subtarea_id) # Obtiene la subtarea por su ID
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

# Función para imprimir en pantalla todas las tareas y sus subtareas
def imprimir_en_pantalla(todas_las_tareas):
    '''Imprime en pantalla todas las tareas y sus subtareas de forma ordenada.'''
    todas_las_tareas = Tarea.objects.all() # Obtenemos todas las instancias de tareas
    for tarea in todas_las_tareas:   # Itera sobre cada tarea
        print(f"Tarea: {tarea.descripcion}")  # Imprime tarea con su descripción
        for subtarea in tarea.subtareas.all():  # Itera sobre cada subtarea
            print(f"  SubTarea: {subtarea.descripcion}")  # Imprime subtarea con su descripción




