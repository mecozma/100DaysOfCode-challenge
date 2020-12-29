import os


# Get current working dir.
current_dir = os.getcwd()
print(current_dir)


# Change current working directory.
# os.chdir('insert path here')


# List directories and files.
print(os.listdir())

# Make a new directory.
os.mkdir('test')
print(os.listdir())

# Rename a directory.
os.rename('test', 'renamed-test')
print(os.listdir())

# Remove a file or a dirrectory.
# Remove a file.
# os.remove('file-name')
# Remove a folder.
os.rmdir('renamed-test')
print(os.listdir())
