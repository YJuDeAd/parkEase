import os

def filepath(filename):
    # File paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the parent directory
    parent_dir = os.path.dirname(script_dir)
    # Path to the Images folder outside the script's folder
    images_dir = os.path.join(parent_dir, "Images")
    os.makedirs(images_dir, exist_ok=True)
    path = os.path.join(images_dir, filename)
    return path