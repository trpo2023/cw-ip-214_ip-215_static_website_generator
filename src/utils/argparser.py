import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Static website generator')
    subparsers = parser.add_subparsers(dest='command')

    page_parser = subparsers.add_parser('page')
    page_subparsers = page_parser.add_subparsers(dest='subcommand')

    create_parser = page_subparsers.add_parser('create')
    create_parser.add_argument('--name', dest='page_name', required=True,
                               help='имя создаваемой страницы [обязательный]')
    create_parser.add_argument('--template-path', dest='template_path', required=False,
                               help='путь к шаблону страницы [обязательный]')

    delete_parser = page_subparsers.add_parser('delete')
    delete_parser.add_argument('--name', dest='page_name', required=True,
                                help='путь к удаляемому файлу')

    parser.add_argument('--path', dest='path', required=True,
                        help='путь к статичной директории [обязательный]')
    parser.add_argument('--port', dest='port', default=3000, type=int,
                        help='порт на котором будет создан сервер')

    args = parser.parse_args()
    return args
