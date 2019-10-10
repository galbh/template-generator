# Template Generator

This project is intended unify boilerplate code between team members and make the setup process for starting a new component shorted and less tedious.

### Usage
```bash
template-generator.py --template shared --folder-name my-example
or
template-generator.py -t shared -n my-example
```  

Components with name constructed of multiple words should be separated by '-' this will result in camel cased class name (MyExampleComponent)

### Template options
#### shared
creates 4 files:
* my-component.component.jsx
* my-component.styles.js
* my-component.readme.md
* my-component.test.jsx 

### Add A Component
* Open template_options.py 
* Add another TemplateInfo(name='my-new-template', file_name=f'{folder_name}.custom.jsx')
* Update get_dictionary method with a key and a value of list of TemplateInfo to  create  
