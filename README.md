# pycamp

Homeschool camp projects for learning python.


## You will need

#### Python
The python language runtime, compiler and interpreter.
https://www.python.org/ftp/python/3.7.5/python-3.7.5-webinstall.exe


#### Git 
This is a source control management client you will use to interact with source code repositories, including the pycamp lessons
Download from https://git-scm.com/download/ and make sure to inlcude the 'git_bash' option.

You can get ("git") all of the code from **pycamp** repository using **git clone <repository_url>**, which in this case is

`git clone https://github.com/gbegley/pycamp.git`

Once you've cloned the repository, you can begin modifying, and committing code using

`git add <file>` 

and

`git commit -m "Some message" <file_or_directory>`




#### Atom IDE
IDE stands for "Integrated Development Environment", and you can download the AtomIDE from 
https://atom.io/packages/atom-ide-ui. The Atom IDE has built in support for git and git hub.

You can add "python language specific" support to the Atom IDE from 
https://atom.io/packages/ide-python


## Using a git repository

### Clone the repository

`git clone https://github.com/gbegley/pycamp.git`

### Add a file to the repository

Create a file named *hello.txt*, for example, by echo some text into a file

`echo "Hello from the echo command." > hello.txt`

You will now have a file called hello.txt that can be added to the local repository using `git add <file>`, which in this case will be

`git add hello.txt`

git will now be tracking the file *hello.txt*. Git is aware of the file, but you need to **commit** the **add**ed file before it will truely be in the repository, using 

`git commit -m "some message" <file>`

`git commit -m "Added hello" hello.txt`

The new file is now part of the repository.

### Push the changes back to the server
You can push the change to the origin repository (The repository you clone at the start) using `git push`

`git push`


