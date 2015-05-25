import argparse
import CppHeaderParser
import os
from jinja2 import Environment, FileSystemLoader

def parse_shared_memory_header(args):
    # set up jinja2 environment for template parsing
    templates_dir = os.path.join(os.path.dirname(__file__), '../carseour/templates/')
    jinja2_env = Environment(loader=FileSystemLoader(templates_dir))
    templates = {}

    # add a check to see if the field is an array definition
    def is_array_definition(field):
        return 'array_size' in field

    jinja2_env.tests['array_definition'] = is_array_definition

    # retrieve and parse template definitions we know
    ext = '.template'
    ext_len = len(ext)

    for template_name in jinja2_env.list_templates():
        templates[template_name[:-ext_len]] = jinja2_env.get_template(template_name)

    # we'll find anonymous enums, which will generate warnings.
    # this doesn't work .. for some reason. but should. :(
    CppHeaderParser.print_warnings = 0

    print("Generating new file..\nAny \"[1103] WARN-enum: nameless enum\" warning can be IGNORED.\n\n")

    # parse the header file
    header_defs = CppHeaderParser.CppHeader(args.input_file)

    output_file = os.path.join(os.getcwd(), args.output_file)
    dst = open(output_file, "w")

    enums = []

    for header_enum in header_defs.enums:
        enum = {
            'values': []
        }

        for value in header_enum['values']:
            # replace "wrong" format for shifts from the parser
            if isinstance(value['value'], str):
                value['value'] = value['value'].replace("< <", "<< ")

            enum['values'].append(value)

        enums.append(enum)

    dst.write(templates['header'].render(enums=enums))

    for class_name in header_defs.classes:
        template = templates[class_name] if class_name in templates else templates['class']
        fields = header_defs.classes[class_name]['properties']['public']

        # we rename SharedMemory to GameInstance to better represent what it is
        if class_name == 'SharedMemory':
            class_name = 'GameInstance'

        dst.write(template.render(fields=fields, class_name=class_name))

    dst.close()

    print("\nWrote " + output_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Regenerate carseour data interface from C header file.')

    parser.add_argument('input_file',
                        metavar='SharedMemory.h',
                        type=str,
                        nargs='?',
                        help='The definition file from the Project Cars project.',
                        default='etc/SharedMemory.h'
                        )

    parser.add_argument('output_file',
                        metavar='OUTPUT',
                        type=str,
                        nargs='?',
                        help='file where the class definitions should be written.',
                        default='carseour/definitions.py'
                        )

    args = parser.parse_args()
    parse_shared_memory_header(args)
