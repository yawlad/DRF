import React from "react"

class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            project_name: '',
            repository_url: '',
            users: ''
        }
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleProjectsChange(event) {
        if(!event.target.selectedOptions){
            this.setState({'users': []})
            return
        }
        let users = []
        for(let i; i <event.target.selectedOptions.length; i++) {
            users.push(event.target.selectedOptions.item(i).value)
        }
    }

    handleSubmit(event) {
        this.props.create_book(this.state.project_name, this.state.repository_url, this.state.users);
        event.preventDefault();
        
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                <input type="text" name="project_name" placeholder="name"
                    value={this.state.project_name}
                    onChange={(event) => this.handleChange(event)} />

                <input type="text" name="repository_url" placeholder="description"
                    value={this.state.repository_url}
                    onChange={(event) => this.handleChange(event)} />
                </div>

                <select name="users" multiple onChange={(event)=> this.handleProjectsChange}>
                    {this.props.users.map((item) => <option value={item.id}>{item.username}</option>)} 
                    

                </select>

                <input type="submit" value="Save" />
            </form>);
    }
}

export default ProjectForm;