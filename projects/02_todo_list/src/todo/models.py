from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: str
    priority: str
    status: str
