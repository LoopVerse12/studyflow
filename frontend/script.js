const API_URL = "http://127.0.0.1:5000";

function loadTasks() {
    fetch(`${API_URL}/tasks`)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("task-list");
            list.innerHTML = "";

            data.forEach(task => {
                const li = document.createElement("li");
                li.textContent = task.title;
                list.appendChild(li);
            });
        });
}

function addTask() {
    const input = document.getElementById("task-input");
    const task = input.value;

    if (!task) return;

    fetch(`${API_URL}/add-task`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ task: task })
    })
    .then(() => {
        input.value = "";
        loadTasks();
    });
}

loadTasks();
