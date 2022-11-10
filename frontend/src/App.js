import React from "react";
import UserList from "./components/User";
import ToDoList from "./components/ToDo";
import {ProjectList, ProjectDetail} from "./components/Project";
import LoginForm from "./components/Auth";

import NotFound404 from "./components/NotFound4004";
import axios from "axios";
import Cookies from "universal-cookie";



import { BrowserRouter, Route, Routes, Link, Navigate } from "react-router-dom"
import ProjectForm from "./components/ProjectForm";


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'users': [],
      'todos': [],
      'projects': [],
      'token': ''

    }
  }

  componentDidMount() {

    this.get_token_from_storage();

  }

  load_data() {
    const headers = this.get_headers();
    axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response => {
      const users = response.data.results
      this.setState({
        'users': users
      })
    }).catch(error => {
      console.log(error)
    })

    axios.get('http://127.0.0.1:8000/api/projects/', {headers}).then(response => {
      const projects = response.data.results
      this.setState({
        'projects': projects
      })
    }).catch(error => {
      console.log(error)
    })

    axios.get('http://127.0.0.1:8000/api/todos/', {headers}).then(response => {
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

  get_token(username, password) {
    const data = {username: username, password: password};
    axios.post('http://127.0.0.1:8000/api/auth_token/', data).then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('ERROR'));
  }

  set_token(token) {
    const cookies = new Cookies();
    cookies.set('token', token);
    this.setState({'token': token}, ()=>{ this.load_data() })
  }

  is_auth() {
    return !!this.state.token
  }

  logout() {  
    this.set_token('')
    this.setState({'users': []}, ()=>{ this.load_data() })
    this.setState({'todos': []}, ()=>{ this.load_data() })
    this.setState({'projects': []}, ()=>{ this.load_data() })

  }

  get_headers() {
    let headers = {
      'Content-Type': 'applications/json',
    }
    if (this.is_auth()) {
      headers['Authorization'] = 'Token ' + this.state.token;
    }
    return headers;
  }

  get_token_from_storage() {
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.set_token(token)
  }

  create_project(project_name, project_url, users) {
    const headers =this.get_headers() 
    const data = {project_name:project_name, project_url:project_url, users:users}
    axios.post(`http://127.0.0.1:8000/api/projects/`,data, {headers, headers}).then(response => { 
      this.load_data()
    }).catch(error =>console.log(error)) 
  }

  delete_todo(id) {
    const headers =this.get_headers() 
    axios.delete(`http://127.0.0.1:8000/api/todos/${id}`,{headers, headers}).then(response => { 
      this.load_data()
    }).catch(error =>console.log(error)) 
  }

  render() {
    return (
      <div>
        <BrowserRouter>
          <nav class="navigation">
            <li><Link to='/users'>Users</Link></li>
            <li><Link to='/projects'>Projects</Link></li>
            <li><Link to='/todos'>ToDos</Link></li>
            
            <li>
              {this.is_auth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
            </li>
          </nav>
          <main class="table_wrapper">
            <Routes>

              <Route exact path='/users' element={<UserList users={this.state.users} />} />

              <Route exact path='/projects'>
                <Route index element={<ProjectList projects={this.state.projects} />} />
                <Route path=':projectId' element={<ProjectDetail projects={this.state.projects} />} />
              </Route>
              <Route exact path='/projects/create' element={<ProjectForm users={this.state.users} create_project={(project_name, project_url, users)=>this.create_project(project_name, project_url, users)}/>} />

              <Route exact path='/todos' element={<ToDoList todos={this.state.todos} delete_todo={id=>this.delete_todo(id)}/>} />
              <Route exact path='/user' element={<Navigate replace to='/users'/>} />
              <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>} />
              <Route exact path='*' element={<NotFound404/>} />
              
            </Routes>
          </main>




        </BrowserRouter>
      </div>
    )
  }
}

export default App;
