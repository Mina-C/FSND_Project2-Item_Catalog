# Catalog Application
Goal of this project is to deploy CRUD using HTTP method and to implement thrid-party OAuth authentication. This application will show catalog and user can check details like item lists and descriptions.

## How to run
You need Python(ver.2.7), Vagrant and VirtualBox.
1. Please install Vagrant and VirtualBox. To make the virtual machine(VM) online, use the commands "vagrant up". Then log on it with "vagrant ssh".
2. Please download all the files and directories into shared directory.
3. To load the date, run 'python database_setup.py'.
4. To run the application, input the command ; 'python application.py'.
5. Open the browser and type address as ; 'http://localhost:8000'

## Program's design
From the Category page, you can explore more detail by clicking links. To add/edit/delete the information, you should login.

