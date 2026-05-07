import uuid
from datetime import date

class Task:
    def __init__(self, name,due_date, priority):
        self.id = str(uuid.uuid4())
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.created_at = str(date.today())
        self.completed = False
    
    def __str__(self):
        return f"Name: {self.name} Due Date: {self.due_date} Priority: {self.priority} Created At: {self.created_at} Completed: {self.completed}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'due_date': self.due_date,
            'priority': self.priority,
            'created_at': self.created_at,
            'completed': self.completed
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'], data['due_date'], data['priority'])
        task.id = data['id']
        task.name = data['name']
        task.due_date = data['due_date']
        task.priority = data['priority']
        task.created_at = data['created_at']
        task.completed = data['completed']
        return task