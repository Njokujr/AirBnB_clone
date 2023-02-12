# AirBnB - The console

![Finalprod](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230211%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230211T235650Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c605f0795d12bd6c3f6aa49f7def1050a6f7a576e091ce2fcf5ca8c1a52293b1)

# [__ABOUT PROJECT__]

DESCRIPTION
This team project is part of the ALX School Full-Stack Software Engineer program. It's the first step towards building a first full web application: an AirBnB clone. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.


    **THE_CONSOLE**
    In this directory you will find a implementation of a AirBnB clone.
    In this first step is implemented the Console. Commands for create, update, destroy, show and manage diferent classes and attributes for the items that the app will be offer and for the users.

        * create your data model
        * manage (create, update, destroy, etc) objects via a console / command interpreter
        * store and persist objects to a file (JSON file)

    **COMMAND_INTERPRETER**
        *Create a new object (ex: a new User or a new Place)
        *Retrieve an object from a file, a database etc…
        *Do operations on objects (count, compute stats, etc…)
        *Update attributes of an object
        *Destroy an object

USAGE:

| COMMAND                                       | EXAMPLE                                                     |
| --------------------------------------------- | ----------------------------------------------------------- |
| Run the console                               |   ./console.py                                                |
| Quit the console                              |   (hbnb) quit                                                 |
| Display the help for a command                |   (hbnb) help <command>                                       |
| Create an object (prints its id)              |   (hbnb) create <class>                                       |
| Show an object                                |   (hbnb) show <class> <id> or (hbnb) <class>.show(<id>)       |
| Destroy an object                             |   (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>) |
| Show all objects, or all instances of a class |   (hbnb) all or (hbnb) all <class>                            |
| Update an attribute of an object              |   (hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") |
 
    

# LEARNING OBJECTIVES
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General

        - How to create a Python package
        - How to create a command interpreter in Python using the cmd module
        - What is Unit testing and how to implement it in a large project
        - How to serialize and deserialize a Class
        - How to write and read a JSON file
        - How to manage datetime
        - What is an UUID
        - What is *args and how to use it
        - What is **kwargs and how to use it
        - How to handle named arguments in a function.

# REQUIREMENTS
    PYTHON SCRIPTS.

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle (version 2.8.*)
    All your files must be executable
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


# EXECUTION
Your shell should work like this in interactive mode:
        $ ./console.py
        (hbnb) help

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit

        (hbnb) 
        (hbnb) 
        (hbnb) quit
        $

But also in non-interactive mode: (like the Shell project in C)

        $ echo "help" | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb) 
        $
        $ cat test_help
        help
        $
        $ cat test_help | ./console.py
        (hbnb)

        Documented commands (type help <topic>):
        ========================================
        EOF  help  quit
        (hbnb) 
        $

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

![IMG](C:\Users\DIDI\Desktop\AirBnB_clone\png\815046647d23428a14ca.png)