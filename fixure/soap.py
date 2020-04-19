from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config["soap"]["soap_url"])
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_info(self, username, password):
        list = []
        client = Client(self.app.config["soap"]["soap_url"])
        projects = client.service.mc_enum_projections(username, password)
        for project in projects:
            list.append(Project(id=project.id, status=project.status, enabled=project.enabled,
                                view_status=project.view_state, description=project.description))
        return list
