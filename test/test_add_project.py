from generator import project as generator
from model.project import Project

def test_add_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    app.project.open_project_page()
    old_projects = app.soap.get_project_info(username, password)
    print(old_projects)
    project = Project(name=generator.random_string("name", 10), description=generator.random_string("description", 10))
    app.project.add_project(project)
    app.project.open_project_page()
    old_projects.append(project)
    new_projects = app.soap.get_project_info(username, password)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)



