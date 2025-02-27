#!/usr/bin/python3

# advanced_questions.py

# Store advanced level questions as a list of dictionaries
PROBLEM_SETS = [
    {
        "question": "What is the output of the following code?\n\nmy_list = [1, 2, 3, 4, 5]\nnew_list = [x for x in my_list if x % 2 == 0]\nprint(new_list)",
        "options": {
            "a": "[2, 4]",
            "b": "[1, 3, 5]",
            "c": "[2, 4, 6]",
            "d": "[1, 2, 3, 4, 5]"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\ndef my_func(a, b, c):\n    print(a, b, c)\n\nargs = (1, 2, 3)\nmy_func(*args)",
        "options": {
            "a": "1 2 3",
            "b": "(1, 2, 3)",
            "c": "TypeError: my_func() takes 3 positional arguments but 4 were given",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\ndef my_func(a, b, c=0):\n    print(a, b, c)\n\nmy_func(1, 2)",
        "options": {
            "a": "1 2 0",
            "b": "1 2",
            "c": "TypeError: my_func() missing 1 required positional argument: 'b'",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is a metaclass in Python?",
        "options": {
            "a": "A class used to define the behavior of other classes.",
            "b": "A class used to define the behavior of other metaclasses.",
            "c": "A class used to define the behavior of class instances.",
            "d": "A class used to define the behavior of function calls."
        },
        "answer": "a"
    },
    {
        "question": "What is the purpose of the __slots__ attribute in Python classes?",
        "options": {
            "a": "It is used to define a set of allowed attributes for a class instance",
            "b": "It is used to define a set of forbidden attributes for a class instance",
            "c": "It is used to define a set of class-level attributes",
            "d": "It is used to define a set of static attributes."
        },
        "answer": "a"
    },
    {
        "question": "Which of the following is not a Python built-in module for working with files?",
        "options": {
            "a": "os",
            "b": "io",
            "c": "pathlib",
            "d": "file"
        },
        "answer": "d"
    },
    {
        "question": "Which of the following is a Python decorator that can be used for caching expensive function calls?",
        "options": {
            "a": "@staticmethod",
            "b": "@classmethod",
            "c": "@property",
            "d": "@lru_cache"
        },
        "answer": "d"
    },
    {
        "question": "What is the difference between a shallow copy and a deep copy in Python?",
        "options": {
            "a": "A shallow copy creates a copy of the object's reference while a deep copy creates a copy of the object's data.",
            "b": "A shallow copy creates a new object while a deep copy does not.",
            "c": "A shallow copy only copies the first level of the object while a deep copy copies all levels.",
            "d": "A shallow copy is slower than a deep copy."
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\nimport re\nmy_string = 'The quick brown fox jumps over the lazy dog'\nresult = re.findall('[aeiou]', my_string)\nprint(result)",
        "options": {
            "a": "['a', 'e', 'i', 'o', 'u']",
            "b": "['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']",
            "c": "['aeiou']",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n\nmy_dict = {1: 'one', 2: 'two', 3: 'three'}\nfor key, value in my_dict.items():\n    print(key, value)",
        "options": {
            "a": "1 'one', 2 'two', 3 'three'",
            "b": "1 one, 2 two, 3 three",
            "c": "['one', 'two', 'three']",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "b"
    },
    {
        "question": "What is the difference between the print() function and the return statement in Python?",
        "options": {
            "a": "print() displays output to the console, while return statement returns a value from a function",
            "b": "print() is used for debugging purposes, while return statement is used to terminate a loop",
            "c": "print() and return statement are interchangeable and can be used interchangeably",
            "d": "print() and return statement are not valid functions in Python"
        },
        "answer": "a"
    },
    {
        "question": "What is the purpose of the urllib module in Python?",
        "options": {
            "a": "To perform HTTP requests and handle responses",
            "b": "To generate random numbers",
            "c": "To manipulate strings",
            "d": "To perform mathematical operations"
        },
        "answer": "a"
    },
    {
        "question": "What is the purpose of test-driven development (TDD) in software development?",
        "options": {
            "a": "To ensure that code is thoroughly tested before it is released to production",
            "b": "To write tests after the code has been written to ensure it works properly",
            "c": "To write code without testing and fix any bugs that arise later",
            "d": "To write code quickly without worrying about testing"
        },
        "answer": "a"
    },
    {
        "question": "What is object-relational mapping (ORM) in Python?",
        "options": {
            "a": "A technique for mapping objects in Python to relational database tables",
            "b": "A technique for mapping Python functions to RESTful APIs",
            "c": "A technique for mapping Python modules to object-oriented programming (OOP) concepts",
            "d": "A technique for mapping Python scripts to network protocols"
        },
        "answer": "a"
    },
    {
        "question": "What is the difference between the input() function and the raw_input() function in Python 2.x?",
        "options": {
            "a": "The input() function returns a string, while the raw_input() function returns the input as it is typed",
            "b": "The raw_input() function is not a valid function in Python 2.x",
            "c": "The input() function is not a valid function in Python 2.x",
            "d": "The input() and raw_input() functions are interchangeable and can be used interchangeably in Python 2.x"
        },
        "answer": "a"
    },
    {
        "question": "Which of the following is a valid way to open a file named \"example.txt\" in read mode?",
        "options": {
            "a": "file = open(\"example.txt\", mode=\"w\")",
            "b": "file = open(\"example.txt\", mode=\"r+\")"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n\ndef greet(name):\n    return f\"Hello, {name}!\"\n\nprint(greet(\"Alice\"))",
        "options": {
            "a": "Hello, Alice!",
            "b": "Hello, !",
            "c": "TypeError: greet() missing 1 required positional argument: 'name'",
            "d": "SyntaxError: invalid syntax"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n lst = [1, 2, 3, 4, 5]\n new_lst = [num * 2 for num in lst if num % 2 == 0]\n print(new_lst)",
        "options": {
            "a": "[2, 4, 6, 8, 10]",
            "b": "[4, 8]",
            "c": "[2, 6, 10]",
            "d": "[1, 2, 3, 4, 5]"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following is not a built-in function in Python?",
        "options": {
            "a": "sum()",
            "b": "len()",
            "c": "sort()",
            "d": "range()"
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n a = [1, 2, 3]\n b = a\n b[0] = 0\n print(a)",
        "options": {
            "a": "[0, 2, 3]",
            "b": "[1, 2, 3]",
            "c": "[0, 1, 2, 3]",
            "d": "[1, 0, 2, 3]"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n class MyClass:\n\t def init(self, num):\n\t\t self.num = num\n a = MyClass(5)\n b = MyClass(10)\n print(a.num + b.num)",
        "options": {
            "a": "15",
            "b": "'5 10'",
            "c": "TypeError",
            "d": "AttributeError"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n def my_func(a, b, c, d):\n\t print(a, b, c, d)\n lst = [1, 2, 3, 4]\n my_func(*lst)",
        "options": {
            "a": "TypeError",
            "b": "1 2 3 4",
            "c": "4 3 2 1",
            "d": "1 4 2 3"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n def my_func(a, b=2, c=3):\n\t print(a, b, c)\n my_func(1, c=4)",
        "options": {
            "a": "1 2 3",
            "b": "1 3 4",
            "c": "1 2 4",
            "d": "SyntaxError"
        },
        "answer": "c"
    },
    {
        "question": "Which of the following is true about Python's Global Interpreter Lock (GIL)?",
        "options": {
            "a": "It allows multiple threads to execute Python code simultaneously.",
            "b": "It prevents deadlocks from occurring in Python programs.",
            "c": "It ensures that only one thread executes Python bytecode at a time.",
            "d": "It prevents race conditions from occurring in Python programs."
        },
        "answer": "c"
    },
    {
        "question": "What is the output of the following code?\n def my_gen(n):\n\t for i in range(n):\n\t\t yield i\n gen = my_gen(3)\n print(next(gen), next(gen), next(gen), next(gen))",
        "options": {
            "a": "0 1 2 StopIteration",
            "b": "0 1 2 None",
            "c": "0 1 2 TypeError",
            "d": "SyntaxError"
        },
        "answer": "a"
    },
    {
        "question": "What is the output of the following code?\n x = 10\n y = 20\n x, y = y, x\n print(x, y)",
        "options": {
            "a": "10 20",
            "b": "20 10",
            "c": "SyntaxError",
            "d": "TypeError"
        },
        "answer": "b"
    },
    {
        "question": "What is the output of the following code?\n def my_func(x):\n\t if x % 2 == 0:\n\t\t return True\n\t else:\n\t\t return False\n lst = [1, 2, 3, 4, 5]\n new_lst = filter(my_func, lst)\n print(list(new_lst))",
        "options": {
            "a": "[1, 3, 5]",
            "b": "[2, 4]",
            "c": "[False, True, False, True, False]",
            "d": "TypeError"
        },
        "answer": "b"
    },
    {
        "question": "Which of the following statements is true about Python's asyncio library?",
        "options": {
            "a": "It allows multiple threads to execute in parallel",
            "b": "It is used for parallel processing of CPU-bound tasks",
            "c": "It is based on the concept of coroutines",
            "d": "It is not compatible with Python 3"
        },
        "answer": "c"
    },
    {
        "question": "What will this code print \nnum1 = 4\nnum2 = 2\nres = num1 * num2\n\nprint(\"Multiplication is\", res)",
        "options": {
            "a": "4",
            "b": "42",
            "c": "8",
            "d": "6"
        },
        "answer": "c"
    },
     {
            "question": "What does this function do?\ndef write_file(filename="", text=""):\n\t\twith open(filename, \"w\", encoding=\"utf-8\") as f:\n\t\treturn f.write(text)",
        "options": {
            "a": "a function that writes a string to a text file (UTF8) and returns the number of characters written",
            "b": "a function that appends a string at the end of a text file (UTF8) and returns the number of characters added",
            "c": "afunction that returns an object (Python data structure) represented by a JSON string",
            "d": "a function that writes an Object to a text file, using a JSON representation"
        },
         "answer": "a"
    },
       {
            "question": "What does the function below do?\nimport json\n\ndef load_from_json_file(filename):\n\t\twith open(filename) as f:\n\t\treturn json.load(f)",
        "options": {
            "a": "writes an Object to a text file, using a JSON representation",
            "b": "returns an object (Python data structure) represented by a JSON string",
            "c": "creates an Object from a JSON file",
            "d": "returns the JSON representation of an object (string)"
        },
        "answer": "c"
    },
      {
            "question": "What function can be used to read input from the user in Python3?",
        "options": {
            "a": "raw_input()",
            "b": "input()",
            "c": "read_input()",
            "d": "read_input()"
        },
         "answer": "b"
    },
      {
            "question": "Which Python module is used to create network sockets?",
        "options": {
            "a": "Urllib",
            "b": "network",
            "c": "request",
            "d": "socket"
        },
         "answer": "d"
    },
       {
            "question": "What is the first step in test-driven development?",
        "options": {
            "a": "Write the code",
            "b": "Debug the code",
            "c": "Deploy the code",
            "d": "Write the tests"
        },
         "answer": "d"
    },
      {
            "question": "In object-relational mapping (ORM), what is an entity?",
        "options": {
            "a": "A database table",
            "b": "A database column",
            "c": "A Python class",
            "d": "An SQL query"
        },
         "answer": "c"
    },
      {
            "question": "What is a database connection pool?",
        "options": {
            "a": "A distributed database",
            "b": "A cache of database connections that can be reused",
            "c": "A backup copy of a database",
            "d": "A group of users who share access to a database"
        },
         "answer": "b"
    },
       {
            "question": "When reading a file in Python, which method can be used to read the entire file as a single string?",
        "options": {
            "a": "read()",
            "b": "readline()",
            "c": "readlines()",
            "d": "file()"
        },
         "answer": "a"
    },
      {
            "question": "Which of the following is not a benefit of using test-driven development (TDD)?",
        "options": {
            "a": "Faster development time",
            "b": "Reduced maintenance costs",
            "c": "Increased risk of bugs",
            "d": "Improved code quality"
            },
            "answer": "c"
        },
        {
            "question": "What is the output of the below code?\n\nmyList=[1,2,3,5,3,4,6,9]\nmyList[-6:6]",
        "options": {
            "a": "[]",
            "b": "[3, 5, 3, 4]",
            "c": "[4, 3, 5, 3]",
            "d": "Index Error"
        },
        "answer": "b"
    },
    {
        "question": "What is the run time of the below code?\n\nfor i in range(n):\n\tj=1\nwhile(j<n):\n\nprint(i,j)\nj*=2",
        "options": {
            "a": "O(n)",
            "b": "O(n^2)",
            "c": "O(log(n))",
            "d": "O(n*log(n))"
        },
        "answer": "d"
    },
    {
        "question": "What is the method that is bound to class but not the instance?",
        "options": {
            "a": "Static method",
            "b": "Class method",
            "c": "Main method",
            "d": "None of the above"
        },
        "answer": "b"
         {
        "question": "What will be the output of the following Python code?\n print("Hello {0[0]} and {0[1]}".format(('foo', 'bin')))",
        "options": {
            "a": "Hello (‘foo’, ‘bin’) and (‘foo’, ‘bin’)",
            "b": "Error",
            "c": "Hello foo and bin",
            "d": "None of the mentioned"
        },
        "answer": "c"
          {
        "question": "Which of the following is the use of id() function in python?",
        "options": {
            "a": "Every object in Python doesn’t have a unique id",
            "b": "In Python Id function returns the identity of the object",
            "c": "None of the mentioned",
            "d": "All of the mentioned"
        },
        "answer": "b"
           {
        "question": "What will be the output of the following Python code?\n x = [[0], [1]]\n print((' '.join(list(map(str, x))),))",
        "options": {
            "a": "01",
            "b": "[0] [1]",
            "c": "(’01’)",
            "d": " (‘[0] [1]’,)"
        },
        "answer": "d"
           {
        "question": "What will be the output of the following Python code?\ndef foo():\ntry:\nreturn 1\nfinally:\nreturn 2\nk = foo()\nprint(k)",
        "options": {
            "a": "error, there is more than one return statement in a single try-finally block",
            "b": "3",
            "c": "2",
            "d": "1"
        },
        "answer": "c"
          {
        "question": "What will be the output of the following Python code?\n x = ['ab', 'cd']\n for i in x:\n  i.upper()\n print(x)", 
        "options": {
            "a": "[‘ab’, ‘cd’]",
            "b": "[‘AB’, ‘CD’]",
            "c": "[None, None]",
            "d": "none of the mentioned"
        },
        "answer": "a"
           {
        "question": "What will be the output of the following Python code?\n x = ['ab', 'cd']\n for i in x:\n x.append(i.upper())\n print(x)",
        "options": {
            "a": "[‘AB’, ‘CD’]",
            "b": "[‘ab’, ‘cd’, ‘AB’, ‘CD’]",
            "c": " [‘ab’, ‘cd’]",
            "d": "none of the mentioned"
        },
        "answer": "d"
          {
        "question": "What will be the output of the following Python code?\n i = 1\n while True:\n  if i%3 == 0:\n break\n print(i)\n i + = 1",
        "options": {
            "a": "1 2",
            "b": "1 2 3",
            "c": "error",
            "d": " none of the mentioned"
        },
        "answer": "c"
        {
        "question": "What will be the output of the following Python code?\n i = 5\n while True:\n if i%0O11 == 0:\n  break\n print(i)\n i += 1",
        "options": {
            "a": "5 6 7 8 9 10",
            "b": "5 6 7 8",
            "c": "5 6",
            "d": "error"
        },
        "answer": "b"
        {
        "question": "What will be the output of the following Python code?\n for i in range(10):\n if i == 5:\n break\n  else:\n   print(i)\n else:\n print("Here")",
        "options": {
            "a": "0 1 2 3 4 Here",
            "b": "0 1 2 3 4 5 Here",
            "c": "0 1 2 3 4",
            "d": "1 2 3 4 5"
        },
        "answer": "c"
        {
        "question": "What will be the output of the following Python code?\n string = "my name is x"\n for i in string.split():\n print (i, end=", ")",
        "options": {
            "a": "m, y, , n, a, m, e, , i, s, , x,",
            "b": "m, y, , n, a, m, e, , i, s, , x",
            "c": "my, name, is, x,",
            "d": "error"
        },
        "answer": "c"
                {
        "question": "What will be the output of the following Python code snippet?\n [0, 1, 2, 3]\n i = -2\n for i not in a:\n print(i)\n  i += 1",
        "options": {
            "a": "-2 -1",
            "b": "0",
            "c": "error",
            "d": "none of the mentioned"
        },
        "answer": "c"
              {
        "question": "What will be the output of the following Python code?\n y = 6\n z = lambda x: x * y\n print z(8)",
        "options": {
            "a": "48",
            "b": "14",
            "c": "64",
            "d": "none of the mentioned"
        },
        "answer": "a"
        {
         "question": "What will be the output of the following Python code?\n lamb = lambda x: x ** 3\n print(lamb(5))",
        "options": {
            "a": "15.",
            "b": "555",
            "c": "125",
            "d": "none of the mentioned"
        },
        "answer": "c"
    },
    {
        "question": "What is the run time of the following  code?\n\nx = [12, 34]\nprint(len(list(map(int, x))))\n",
        "options": {
            
            "a": "2",
           "b": "1",
           "c": "error",
           "d": "none of the mentioned"
           },
           "answer": "a"
           },
    {
       "question": "What will be the output of the following Python code?\n\nx = [12.1, 34.0]\nprint(len(' '.join(list(map(str, x)))))\n",

       "options": {
           "a": "6",
           "b": "8",
           "c": "9",
           "d": "none of the mentioned"
       },
       "answer": "c"
   },
    {
       "question": "What will be the output of the following Python code?\n\nx = [12.1, 34.0]\nprint(' '.join(list(map(str, x))))\n",

       "options": {
           "a": "12 1 34 0",
           "b": "12.1 34",
           "c": "121 340",
           "d": "12.1 34.0"
       },
       "answer": "d"
   },
    {
       "question": "Which of the following statements create a dictionary?",
       "options": {
            "a": " d = {}",
           "b": "d = {“john”:40, “peter”:45}",
           "c": "d = {40:”john”, 45:”peter”}",
           "d": "All of the above"
       },
       "answer": "d"
   },
   { 
    "question": " Suppose d = {“john”:40, “peter”:45}, to delete the entry for “john” what command do we use?",

       "options": {
           "a": "d.delete(“john”:40)",
           "b": "d.delete(“john”)",
           "c": " del d[“john”]",
           "d": "del d(“john”:40)"
       },
       "answer": "c"
   },
   {
       "question": "What will be the output of the following Python code?\nd = {"john":40, "peter":45}\nprint(list(d.keys()))\n",

       "options": {
           "a": "[“john”, “peter”]",
           "b": "[“john”:40, “peter”:45]",
           "c": "(“john”, “peter”)",
           "d": "(“john”:40, “peter”:45)"
       },
       "answer": "a"
   },
    {
       "question": "What will be the output of the following Python code?\ndef f(x):\n\tyield x+1\ng=f(8)\nprint(next(g))\n",

       "options": {
           "a": "8",
           "b": "9",
           "c": "7",
           "d": "error"
       },
       "answer": "b"
   },
    {
       "question": "What will be the output of the following Python code?\ndef f(x):\n\tfor i in range(5):\n\tyield i\n\ng=f(8)\nprint(list(g))\n",

       "options": {
           "a": "[0, 1, 2, 3, 4]",
           "b": " [1, 2, 3, 4, 5, 6, 7, 8]",
           "c": "[1, 2, 3, 4, 5]",
           "d": "[0, 1, 2, 3, 4, 5, 6, 7]"
       },
       "answer": "a"
   },
]
