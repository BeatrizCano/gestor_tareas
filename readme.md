### Descripción de Archivos

- **tasksClasses/\_\_init\_\_.py**: Este archivo puede estar vacío, pero es necesario para que Python trate esta carpeta como un paquete.

- **tasksClasses/task.py**: Define la clase `Task`, que representa una tarea individual. Cada tarea tiene una descripción y un estado de completada o pendiente.
    ```python
    class Task:
        def __init__(self, description):
            self.description = description
            self.completed = False

        def mark_as_completed(self):
            self.completed = True

        def __str__(self):
            status = "Completed" if self.completed else "Pending"
            return f"{self.description} - {status}"
    ```

- **tasksClasses/task_list.py**: Define la clase `TaskList`, que gestiona una lista de tareas. Permite agregar, marcar como completada, mostrar y eliminar tareas.
    ```python
    from tasksClasses.task import Task

    class TaskList:
        def __init__(self):
            self.tasks = []

        def add_task(self, description):
            new_task = Task(description)
            self.tasks.append(new_task)
            print(f"Task '{description}' added.")

        def mark_task_as_completed(self, position):
            try:
                self.tasks[position].mark_as_completed()
                print(f"Task at position {position} marked as completed.")
            except IndexError:
                print("Error: No task at that position.")

        def show_all_tasks(self):
            if not self.tasks:
                print("No tasks pending.")
            else:
                for idx, task in enumerate(self.tasks):
                    print(f"{idx}. {task}")

        def delete_task(self, position):
            try:
                deleted_task = self.tasks.pop(position)
                print(f"Task '{deleted_task.description}' deleted.")
            except IndexError:
                print("Error: No task at that position.")
    ```

- **main.py**: Archivo principal que contiene la lógica para interactuar con el usuario y manejar las opciones del menú.
    ```python
    from tasksClasses.task_list import TaskList
    from colorama import Fore, init

    # Inicializar colorama
    init(autoreset=True)

    def menu():
        task_list = TaskList()
        while True:
            print(Fore.MAGENTA + "\n\nTask Manager")
            print(Fore.CYAN + "1. Add new task")
            print("2. Mark task as completed")
            print("3. Show all tasks")
            print("4. Delete a task")
            print(Fore.RED + "5. Exit")

            option = input(Fore.YELLOW + "\nSelect an option: ")

            if option == "1":
                description = input(Fore.BLUE + "\nEnter the task description: ")
                task_list.add_task(description)
            elif option == "2":
                try:
                    position = int(input(Fore.BLUE + "\nEnter the position of the task to mark as completed: "))
                    task_list.mark_task_as_completed(position)
                except ValueError:
                    print(Fore.RED + "Error: You must enter an integer.")
            elif option == "3":
                task_list.show_all_tasks()
            elif option == "4":
                try:
                    position = int(input(Fore.BLUE + "\nEnter the position of the task to delete: "))
                    task_list.delete_task(position)
                except ValueError:
                    print(Fore.RED + "Error: You must enter an integer.")
            elif option == "5":
                print(Fore.RED + "Exiting the task manager.")
                break
            else:
                print(Fore.RED + "Invalid option. Please try again.")

    if __name__ == "__main__":
        menu()
    ```

## Ejecución del Programa

Para ejecutar el programa, sigue estos pasos:

1. Clona o descarga este repositorio en tu máquina local.
2. Navega al directorio raíz del proyecto:
    ```sh
    cd /ruta/a/gestor_tareas
    ```
3. Instala la biblioteca `colorama` si aún no está instalada:
    ```sh
    pip install colorama
    ```
4. Ejecuta el archivo `main.py` con Python:
    ```sh
    python main.py
    ```
5. Sigue las instrucciones en pantalla para agregar, marcar como completada, mostrar y eliminar tareas.

## Requisitos

- Python 3.6 o superior
- Biblioteca `colorama`

## Notas

- Asegúrate de tener instalado Python y de que tu intérprete de Python esté configurado correctamente.
- Si estás utilizando un entorno virtual, actívalo antes de ejecutar el script `main.py`.

## Contribución

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
