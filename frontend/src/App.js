import React from "react";
import UserList from "./components/User";
import ToDoList from "./components/ToDo";
import {ProjectList, ProjectDetail} from "./components/Project";

import NotFound404 from "./components/NotFound4004";
import axios from "axios";



import { BrowserRouter, Route, Routes, Link, Navigate } from "react-router-dom"


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'todos': [],
      'projects': []

    }
  }

  componentDidMount() {

    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
      const users = response.data.results
      this.setState({
        'users': users
      })
    }).catch(error => {
      console.log(error)
    })

    axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
      const projects = response.data.results
      this.setState({
        'projects': projects
      })
    }).catch(error => {
      console.log(error)
    })

    axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
      const todos = response.data.results
      todos.map((todo_) => {
        todo_.deleted = todo_.deleted ? 'true' : 'false'; 
      })
      this.setState({
        'todos': todos
      })
    }).catch(error => {
      console.log(error)
    })

  }



  render() {
    return (
      <div>
        <BrowserRouter>
          <nav class="navigation">
            <li><Link to='/users'>Users</Link></li>
            <li><Link to='/projects'>Projects</Link></li>
            <li><Link to='/todos'>ToDos</Link></li>
          </nav>
          <main class="table_wrapper">
            <Routes>

              <Route exact path='/users' element={<UserList users={this.state.users} />} />

              <Route exact path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} />} />
                <Route path=':projectId' element={<ProjectDetail projects={this.state.projects} />} />
              </Route>

              <Route exact path='/todos' element={<ToDoList todos={this.state.todos} />} />
              <Route exact path='/user' element={<Navigate replace to='/users'/>} />
              <Route exact path='*' element={<NotFound404/>} />
              
            </Routes>
          </main>




        </BrowserRouter>
      </div>
    )
  }
}

export default App;
