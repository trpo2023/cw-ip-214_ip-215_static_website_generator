import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Static website generator')
    parser.add_argument('--path', dest='path', required=True,
                        help='путь к статичной директории [обязательный]')
    parser.add_argument('--port', dest='port', default=3000, type=int,
                        help='порт на котором будет создан сервер')
    subparsers = parser.add_subparsers(dest='command')

    page_parser = subparsers.add_parser('page')
    page_subparsers = page_parser.add_subparsers(dest='subcommand')
    create_parser = page_subparsers.add_parser('create')
    create_parser.add_argument('page_path',
                               help='название страницы для создания')
    create_parser.add_argument(
        'template_path',
        help='путь к файлу шаблона, иначе будет пустая страница ')

    delete_parser = page_subparsers.add_parser('delete')
    delete_parser.add_argument('page_path',
                               help='название страницы для удаления')

    args = parser.parse_args()
    return args
