import React from "react"
import { Link, useParams } from "react-router-dom"

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>
                <Link to={`/projects/${project.id}`}>{project.project_name}</Link>
            </td>
            <td>{project.repository_url}</td>
            <td>{project.users}</td>
        </tr>
    )
}

const ProjectList = ({ projects }) => {
    return (
        <table>
            <th>ID</th>
            <th>Project name</th>
            <th>Repository URL</th>
            <th>Users</th>
            {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

const ProjectDetail = ({ projects }) => {
    let { projectId } = useParams()
    let project = projects.find(project_ => project_.id == projectId)
    return (
        <div class="detail">
            <h1>{project.project_name}</h1>
            <p><b>Repository URL:</b> {project.repository_url}</p>
            <p><b>Users:</b> <br/>{project.users.map(user => {
                return <pre>         {user}<br/></pre>
            })}</p>
        </div>
    )
}

export {ProjectList, ProjectDetail}
