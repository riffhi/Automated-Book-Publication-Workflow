def read_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def save_text_file(filepath, text):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(text)
