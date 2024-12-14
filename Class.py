class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def __repr__(self):
        return "\n".join(str(task) for task in self.tasks)

# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-10-10")
task_manager.add_task("Сделать домашнее задание", "2023-10-12")
task_manager.mark_task_as_completed(0)

print("Все задачи:")
print(task_manager)

print("\nТекущие задачи:")
print(task_manager.get_pending_tasks())