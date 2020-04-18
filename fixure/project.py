from model.project import Project


class Projecthelper:


    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@href='/mantisbt-1.2.20/manage_overview_page.php']").click()
        wd.find_elements_by_xpath("//*[contains(text() , 'Manage Projects')]")[-1].click()

    def get_project_list(self):
        wd = self.app.wd
        list = []
        i = 0
        self.open_project_page()
        for element in wd.find_elements_by_xpath("//*[contains(@class,'row-')]//*[contains(@href,'id')]/../.."):
            cells = element.find_elements_by_tag_name("td")
            id = wd.find_elements_by_xpath("//*[contains(@class,'row-')]//*[contains(@href,'id')]")[i].get_attribute("href")
            i = i+1
            id = id[-1:]
            name = cells[0].text
            status = cells[1].text
            enabled = cells[2].text
            view_status = cells[3].text
            description = cells[4].text
            list.append(Project(id=id, name=name, status=status, enabled=enabled, view_status=view_status,
                                description=description))
        return list


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@value="Create New Project"]').click()
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        wd.find_element_by_xpath('//*[@value="Add Project"]').click()

    def delete_project(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[contains(@class,'row-')]//*[contains(@href,'id=%s')]" % id).click()
        wd.find_element_by_xpath('//*[@value="Delete Project"]').click()
