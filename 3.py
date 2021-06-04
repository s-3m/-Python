import os
import shutil


my_list = []
main_dir = 'my_project'
for root, dir, files in os.walk(main_dir):
    for file in files:
        if file.lower().endswith('.html'):
            dir_file = os.path.join(root, file)
            dir_copy = os.path.join('templates', root.split('\\')[-1])
            if not os.path.exists(os.path.join('templates', root.split('\\')[-1])):
                os.makedirs(os.path.join('templates', root.split('\\')[-1]))
                shutil.copy(dir_file, dir_copy)
            else:
                path_of_copy = os.path.join('templates', root.split('\\')[-1])
                if not os.path.exists(os.path.join(path_of_copy, file)):
                    shutil.copy(dir_file, os.path.join('templates', root.split('\\')[-1]))
                else:
                    print(f'file {file} exist already.')
                    continue



