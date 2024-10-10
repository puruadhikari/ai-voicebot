import os


def ensure_directory_exists(directory_path):
    # Ensure a directory exists, create if it does not
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def format_message(user_message):
    # Format a message to add some custom formatting
    return f"Formatted message: {user_message}"
