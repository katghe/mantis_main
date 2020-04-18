from generator import project as generator
from model.project import Project
import random


def test_project_delete(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    app.project.open_project_page()
    if app.soap.get_project_info(username, password)==0:
        project = Project(name=generator.random_string("name", 10),
                          description=generator.random_string("description", 10))
        app.project.add_project(project)
    old_projects = app.soap.get_project_info(username, password)
    project = random.choice(old_projects)
    app.project.delete_project(project.id)
    app.project.open_project_page()
    new_projects = app.soap.get_project_info(username, password)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)