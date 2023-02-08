# AirBnB

# [__ABOUT PROJECT__]

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

![IMG](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D/20230208/us-east-1/s3/aws4_request&X-Amz-Date=20230208T181751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=038f6d1d37bf02a1eb0254aedaac09a33c94b99dfe4cef7fa21bc01487c96dab)