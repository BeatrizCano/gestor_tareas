from tasksClasses.task import Task
from colorama import Fore, Style

class TaskList:
    def __init__(self):
        """
        Inicializa una nueva lista de tareas vacía.
        """
        self.tasks = []

    def add_task(self, description):
        """
        Agrega una nueva tarea a la lista de tareas con la descripción proporcionada.
        """
        new_task = Task(description)
        self.tasks.append(new_task)
        print(Fore.GREEN + f"\nTarea: '{description}' agregada.")

    def mark_task_as_completed(self, position):
        """
        Marca la tarea en la posición especificada como completada.
        Maneja IndexError si la posición no es válida.
        """
        try:
            completed_task = self.tasks[position]
            completed_task.mark_as_completed()
            print(Fore.GREEN + f"\nTarea '{completed_task.description}' marcada como completada.")
            return completed_task
        except IndexError:
            print(Fore.RED + "\nError: No existe una tarea en esa posición.")
            return None

    def show_all_tasks(self):
        """
        Muestra todas las tareas en la lista, indicando su estado.
        """
        if not self.tasks:
            print(Fore.RED + "\nNo hay tareas pendientes.")
        else:
            for idx, task in enumerate(self.tasks):
                color = Fore.GREEN if task.completed else Fore.LIGHTRED_EX
                print(color + f"{idx}. {task}")

    def delete_task(self, position):
        """
        Elimina la tarea en la posición especificada de la lista.
        Maneja IndexError si la posición no es válida.
        """
        try:
            deleted_task = self.tasks.pop(position)
            print(Fore.GREEN + f"\nTarea: '{deleted_task.description}' eliminada.")
            return deleted_task
        except IndexError:
            print(Fore.RED + "\nError: No existe una tarea en esa posición.")
            return None