### Instrucciones para crear un ambiente virtual:

### Windows:

- Open a command prompt.
- Execute the following command to install the venv tool:
    pip install venv
- Once venv is installed, you can create a new virtual environment running the following command:
    python -m venv my_env
- This will create a new directory called my_env.The my_env directory contains an isolated Python interpreter and a Lib folder that contains the libraries installed for that virtual environment.

- To activate the virtual environment, open a command prompt in the my_env directory and execute the following command:
    .\Scripts\activate.bat
- Once the virtual environment is activated, the command prompt will change to indicate that you are using the virtual environment. For example, the system symbol window indicator can change C:\Users\[user name] to (my_env).

- Before installing any package, it is recommended to update PIP, using the command:
    python.exe -m pip install --upgrade pip
- Now you can install Python packages in the virtual environment running the Pip Install command. For example, to install the numpy package, you would run the following command:
    pip install numpy
- If you have a requirement.txt file, all the necessary packages of an environment at the same time with the command can be installed:
    pip install -r requirements.txt

- Once the packages are installed, you can use the virtual environment to execute your Python programs. To run a Python program, simply run the program file. For example, to execute a program file called My_program.py, you would execute the following command:
    python my_program.py
- When you have finished using the virtual environment, you can deactivate it by running the following command:
    deactivate.bat
- Once the virtual environment is deactivated, the system symbol window will return to its previous state.


Linux:

- Open a command prompt.
- Execute the following command to install the venv tool:
    pip install venv
- Once venv is installed, you can create a new virtual environment running the following command:
    python3 -m venv my_env
- This will create a new directory called my_env.The my_env directory contains an isolated Python interpreter and a Lib folder that contains the libraries installed for that virtual environment.

- To activate the virtual environment, open a command prompt in the my_env directory and execute the following command:
    source bin/activate
- Once the virtual environment is activated, the command prompt will change to indicate that you are using the virtual environment. For example, the system symbol window indicator can change ~/my_env to (my_env).

- Before installing any package, it is recommended to update PIP, using the command:
    python.exe -m pip install --upgrade pip
- Now you can install Python packages in the virtual environment running the Pip Install command. For example, to install the numpy package, you would run the following command:
    pip install numpy
- If you have a requirement.txt file, all the necessary packages of an environment at the same time with the command can be installed:
    pip install -r requirements.txt

- Once the packages are installed, you can use the virtual environment to execute your Python programs. To run a Python program, simply run the program file. For example, to execute a program file called My_program.py, you would execute the following command:
    python my_program.py
- When you have finished using the virtual environment, you can deactivate it by running the following command:
    deactivate
- Once the virtual environment is deactivated, the system symbol window will return to its previous state.
