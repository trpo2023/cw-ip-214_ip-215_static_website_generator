import os
from flask import Flask, render_template

def start_server(path: str, port: int) -> bool:
    try:
        app = Flask(__name__)
        app.static_folder = path
        
        @app.route("/")
        def index():
            path_index_html = os.path.join(path + '/index.html')
            print(path_index_html)
            if(os.path.isfile(path_index_html)):
                return app.send_static_file('index.html')
            
            return "No Index file found"

        @app.route("/<path:filename>")
        def serve_static(filename):
            #TODO: HANDLE .md to html conversion
            file_path = os.path.join(path, filename)
            print(file_path)
            
            return app.send_static_file(filename=filename)

        app.run(port=port)
        return True
    except OSError:
        print(f"Failed to start server on port {port}.")
        return False
