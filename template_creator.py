import os
from os.path import join, normpath
from typing import List, Dict
from jinja2 import Template
from dataclasses import dataclass


@dataclass
class TemplateOptions:
    shared_component = 'shared'
    function_component = 'function-component'
    styles = 'styles'
    readme = 'readme'
    test = 'test'


class TemplatesCreator:
    template_names: List
    folder_name: str
    component_type_to_file_name_dict: Dict

    def __init__(self, template_name, folder_name):
        self.template_names = template_name
        self.folder_name = folder_name
        self.component_type_to_file_name_dict = {
            TemplateOptions.function_component: f'{folder_name}.component.jsx',
            TemplateOptions.styles: f'{folder_name}.styles.js',
            TemplateOptions.readme: f'{folder_name}.readme.md',
            TemplateOptions.test: f'{folder_name}.test.jsx'
        }

    def create(self):
        self.create_folder()
        self.create_files()

    def create_folder(self):
        path = normpath(join(os.getcwd(), self.folder_name))
        try:
            os.mkdir(path)
        except OSError:
            print(f'Creation of the directory {path} failed directory probably already exists')
        else:
            print(f'Successfully created the directory {path}')

    def create_files(self):
        for template_name in self.template_names:
            template = self.get_template(template_name)
            file_name = self.component_type_to_file_name_dict[template_name]
            self.write_to_file(template, normpath(join(self.folder_name, file_name)))
            print(f'{file_name} was written successfully')

    def get_template(self, template_name):
        for filename in os.listdir('templates'):
            if template_name in filename:
                template_path = normpath(join('templates', filename))
                string_template = self.file_to_string(template_path)
                t = Template(string_template)
                class_name = self.get_component_name(self.folder_name)
                return t.render(component_name=class_name)

    @staticmethod
    def file_to_string(path):
        with open(path, 'r') as file:
            return file.read()

    @staticmethod
    def write_to_file(file_content, file_name):
        f = open(file_name, 'w')
        f.write(file_content)
        f.close()

    @staticmethod
    def get_component_name(word):
        return ''.join(x.capitalize() or '-' for x in word.split('-')) + 'Component'
