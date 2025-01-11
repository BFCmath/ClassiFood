def load_classes(filepath):
    with open(filepath, 'r') as f:
        classes = f.read().splitlines()
    return classes