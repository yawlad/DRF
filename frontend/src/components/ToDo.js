import React from "react"

const ToDoItem = ({todo, delete_todo}) => {
    return(
        <tr>
            <td>{todo.id}</td>
            <td>{todo.todo_name}</td>
            <td>{todo.description}</td>
            <td>{todo.deleted}</td>
            <td>{todo.project_id}</td>
            <td><button onClick={()=>delete_todo(todo.id)} type="button">Delete</button></td>
        </tr>
    )
}

const ToDoList = ({todos, delete_todo}) => {
    return(
        <table>
            <th>ID</th>
            <th>ToDo name</th>
            <th>ToDo description</th>
            <th>Deleted</th>
            <th>Project ID</th>
            <th></th>
            {todos.map((todo_) => <ToDoItem todo={todo_} delete_todo={delete_todo}/>)}
        </table>
    )
}

export default ToDoList