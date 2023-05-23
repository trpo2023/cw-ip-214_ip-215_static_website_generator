import os
from utils.argparser import parse_args
from utils.server import start_server
from utils.pages import create_file, delete_file

if __name__ != "__main__":
    exit(0)

args = parse_args()
print(args)
path = args.path
port = args.port

if (os.path.exists(path) is False):
    print("Указанный путь не существует.")
    exit(1)

if (args.command == 'page'):
    name = args.page_name

    if (args.subcommand == 'create'):
        template_path = False
        if (args.template_path):
            template_path = os.path.abspath(args.template_path)
        static_folder_path = os.path.abspath(args.path)

        create_file(static_folder_path, name, template_path)

    if (args.subcommand == 'delete'):
        delete_file(path, name)
else:
    start_server(path=os.path.abspath(path), port=port)
