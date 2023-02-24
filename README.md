<div align="center">
  <img src="https://github.com/Wayzer2318/holbertonschool-AirBnB_clone/raw/main/banner.png">
</div>

<div align="center">
  <h1>HolbertonBnB</h1>
  <p>A Holberton School Project</p>
</div>

## Description

This is the first part of the project where we will be writing an airbnb-like application.  We're currently building up the persistent data management part with models that are saved to the filesystem in json. A console provided to allow for easy data operations.

## Requirements

This project is tested on Ubuntu 20.04
Python 3.4+ has to be installed


### Ubuntu

```sh
sudo apt-get install python3
```

## Installation

All you need to do is to clone the repository files

```sh
git clone https://github.com/Wayzer2318/holbertonschool-AirBnB_clone.git
cd holbertonschool-AirBnB
```

## Testing

All tests are done with the `unittest` module
You can run them with the following command

```sh
python3 -m unittest discover tests
```

## Command Interpreter

This project contains a console written in python that allows operators to manually edit the different data models stored.
Once the repository is installed, you can start the console with:

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

Additionally, you can pass in commands into the console by doing as following
```sh
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

Detailed usage guides are available under the `help` command

### Example commands

Create a user

```
(hbnb) create User
50890020-2d86-49d4-b868-c0bdd69a73fb
```

List all objects

```
(hbnb) all
["[User] (50890020-2d86-49d4-b868-c0bdd69a73fb) {'id': '50890020-2d86-49d4-b868-c0bdd69a73fb', ...}"]
```

Update an object's field

```
(hbnb) update User 50890020-2d86-49d4-b868-c0bdd69a73fb email 6969@holbertonstudents.com
(hbnb) show User 50890020-2d86-49d4-b868-c0bdd69a73fb
[User] (50890020-2d86-49d4-b868-c0bdd69a73fb) {'id': '50890020-2d86-49d4-b868-c0bdd69a73fb', 'email': '6969@holbertonstudents.com', ...}
```

Desstroy an object

```
(hbnb) destroy User 50890020-2d86-49d4-b868-c0bdd69a73fb
(hbnb) show User 50890020-2d86-49d4-b868-c0bdd69a73fb
** no instance found **
```

## Authors

- Arezki Ait Kettout arezki.ait.kettout@gmail.com
- Thibault R. 1337snavy@gmail.com
