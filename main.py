import optparse
from template_creator import TemplatesCreator, TemplateOptions

parser = optparse.OptionParser()
parser.add_option('-t', '--template',
                  action="store", dest="template",
                  help=f'one of {TemplateOptions}', default="spam")

parser.add_option('-n', '--folder-name',
                  action="store", dest="folder_name",
                  help='any string')

options, args = parser.parse_args()

template_dictionary = {
    TemplateOptions.shared_component: [
        TemplateOptions.function_component,
        TemplateOptions.styles,
        TemplateOptions.readme,
        TemplateOptions.test
    ]
}

templates_to_create = template_dictionary.get(options.template)
if templates_to_create:
    TemplatesCreator(templates_to_create, options.folder_name).create()
else:
    print(f'no templates were found for {options.template}')
