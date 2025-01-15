from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD
# Create, Read, Update, Delete

tasks = []
task_id_control = 1


@app.route('/tasks', methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data["title"], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso"}), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task_to_update = None
    for t in tasks:
        if t.id == id:
            task_to_update = t
            break

    if task_to_update is None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task_to_update.title = data['title']
    task_to_update.description = data.get('description', task_to_update.description)
    task_to_update.completed = data.get('completed', task_to_update.completed)
    return jsonify({"message": "Tarefa atualizada com sucesso"})


@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if not task:
        return jsonify({"message": "naõ foi possivel encontrar a atividade"}), 404
    

    task.remove(task)
    return jsonify({"message": "tarefa deletada com sucesso"})



if __name__ == "__main__":
    app.run(debug=True)
