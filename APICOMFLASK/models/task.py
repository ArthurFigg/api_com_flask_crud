class Task:
    def __init__(self, id, title, description, completed=False) -> None:
        self.id = id  # Corrigido o operador
        self.title = title  # Corrigido o operador
        self.description = description
        self.completed = completed  # Corrigido o operador

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,  # Corrigido: antes estava retornando "self.id" no lugar de "self.title"
            "description": self.description,
            "completed": self.completed
        }
