import os

os.mkdir('some_file') if not os.path.exists('some_file') else None
os.remove('some_file') if os.path.exists('some_file') else None
