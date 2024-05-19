from tasksClasses.task_list import TaskList
from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

def menu(): 
    """
    Muestra el menú principal y maneja la interacción con el usuario para gestionar la lista de tareas.
    """
    tasks_list = TaskList() # Crear una instancia de TaskList
    while True:
        # Mostrar el menú de opciones
        print(Fore.MAGENTA + "\n\nAdministrador de Tareas Pendientes")
        print(Fore.CYAN + "\n1. Agregar una nueva tarea")
        print(Fore.CYAN + "2. Marcar la tarea como completada")
        print(Fore.CYAN + "3. Mostrar todas las tareas")
        print(Fore.CYAN + "4. Eliminar una tarea")
        print(Fore.RED + "5. Salir")

        option = input(Fore.YELLOW + "\nSeleccione una opción: ")

        if option == "1":
             # Agregar una nueva tarea
            description = input(Fore.BLUE + "\nIntroduzca la descripción de la tarea: ")
            tasks_list.add_task(description)
        elif option == "2":
            # Marcar una tarea como completada
            try:
                position = int(input(Fore.BLUE + "\nIntroduzca la posición de la tarea a marcar como completada: "))
                tasks_list.mark_task_as_completed(position)
            except ValueError:
                print(Fore.RED +"\nError: Debe ingresar un número entero.")
        elif option == "3":
             # Mostrar todas las tareas
            tasks_list.show_all_tasks()
        elif option == "4":
              # Eliminar una tarea
            try: 
                position = int(input(Fore.BLUE + "\nIntroduzca la posición de la tarea a eliminar: "))
                tasks_list.delete_task(position)
            except ValueError:
                print(Fore.RED + "\nError: Debe ingresar un número entero.")
        elif option == "5":
             # Salir del programa
            print(Fore.RED + "\nAdministrador de tareas cerrado.")
            break
        else:
            print(Fore.RED + "\nOpción no válida. Por favor, inténtelo de nuevo.")

if __name__ == "__main__":
    menu()