import os

list_name = ['settings', 'mainapp', 'authapp']  # список для создания вложенных папок

for i in list_name:
    dir_path = os.path.join('my_project', i)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


dir_path = os.path.join('my_project', 'mainapp/templates/mainapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

dir_path = os.path.join('my_project', 'authapp/templates/authapp')
if not os.path.exists(dir_path):
    os.makedirs(dir_path)



# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
