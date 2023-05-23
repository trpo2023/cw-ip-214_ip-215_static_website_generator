import os


def has_valid_extension(file_name):
    file_name_lower = file_name.lower()
    return file_name_lower.endswith('.md') or file_name_lower.endswith('.html')


def create_file(folder_path, page_name, template_path):
    if not has_valid_extension(page_name):
        print("Incorrect file extension")
        return

    file_path = os.path.join(folder_path, page_name)
    if os.path.exists(file_path):
        print(f"File {file_path} already exists.")
        return

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
        with open(file_path, 'w') as new_file:
            new_file.write(template_content)
        print(f"Created file {file_path}.")
    except FileNotFoundError:
        print(f"Template file {template_path} not found.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def delete_file(file_path, name):
    if not os.path.exists(os.path.join(file_path, name)):
        print(f"File {file_path} does not exist.")
        return

    try:
        os.remove(os.path.join(file_path, name))
        print(f"Deleted file {os.path.join(file_path, name)}.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")
