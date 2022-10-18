import React from "react"

const ToDoItem = ({todo}) => {
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.todo_name}</td>
            <td>{todo.description}</td>
            <td>{todo.deleted}</td>
            <td>{todo.project_id}</td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return(
        <table>
            <th>ID</th>
            <th>ToDo name</th>
            <th>ToDo description</th>
            <th>Deleted</th>
            <th>Project ID</th>
            {todos.map((todo_) => <ToDoItem todo={todo_}/>)}
        </table>
    )
}

export default ToDoList