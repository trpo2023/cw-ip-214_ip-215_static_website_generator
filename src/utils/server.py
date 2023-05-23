import os
import markdown
from flask import Flask, render_template


def start_server(path: str, port: int) -> bool:
    try:
        app = Flask(__name__)
        app.static_folder = path

        @app.route("/")
        def index():
            path_index_html = os.path.join(path + '/index.html')
            print(path_index_html)
            if (os.path.isfile(path_index_html)):
                return app.send_static_file('index.html')

            return "No Index file found"

        @app.route("/<path:filename>")
        def serve_static(filename):
            file_path = os.path.join(path, filename)

            if filename.endswith('.md'):
                with open(file_path, 'r') as f:
                    md_content = f.read()

                html_content = markdown.markdown(md_content)
                return html_content

            return app.send_static_file(filename)

        app.run(port=port)
        return True
    except OSError:
        print(f"Failed to start server on port {port}.")
        return False
