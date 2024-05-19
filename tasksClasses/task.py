class Task:
    def __init__(self, description):
        """
        Inicializa una nueva tarea con una descripción y un estado de completada en False.
        """
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        """
        Marca la tarea como completada.
        """
        self.completed = True
    
    def __str__(self):
        """
        Retorna una representación en cadena de la tarea, mostrando su descripción y estado.
        """
        status = "Completada" if self.completed else "Pendiente"
        return f"{self.description} - {status}"