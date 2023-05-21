import os
from utils.argparser import parse_args
from utils.server import start_server

if __name__ != "__main__": 
    exit(0)

args = parse_args()
print(args)
path = args.path
port = args.port

if(os.path.exists(path) == False):
    print("Указанный путь не существует.")
    exit(1)

if(args.command == 'page'):
    page_path = args.page_path

    if(args.subcommand == 'create'):
        # TODO: HANDLE CREATE
        template_path = args.template_path
        print('create')
    if(args.subcommand == 'delete'):
        # TODO HANDLE DELETE
        print('delete')
else:
    start_server(path=path, port=port)
