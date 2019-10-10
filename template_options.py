from dataclasses import dataclass


@dataclass
class TemplateInfo:
    name: str
    file_name: str


@dataclass
class TemplateOptions:
    folder_name: TemplateInfo
    function_component: TemplateInfo
    styles: TemplateInfo
    readme: TemplateInfo
    test: TemplateInfo

    def __init__(self, folder_name: str):
        self.function_component = TemplateInfo(name='function-component', file_name=f'{folder_name}.component.jsx')
        self.styles = TemplateInfo(name='styles', file_name=f'{folder_name}.styles.js')
        self.readme = TemplateInfo(name='readme', file_name=f'{folder_name}.readme.md')
        self.test = TemplateInfo(name='test', file_name=f'{folder_name}.test.jsx')

    def get_dictionary(self):
        return {
            'shared': [
                self.function_component,
                self.styles,
                self.readme,
                self.test
            ]
        }
