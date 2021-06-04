import os

main_folder = 'my_project'
if not os.path.exists(main_folder):
    os.mkdir(main_folder)
name_need_dir = ['settings', 'mainapp', 'addminapp', 'authapp']
for i in name_need_dir:
    if not os.path.exists(os.path.join(main_folder, i)):
        os.mkdir(os.path.join(main_folder, i))