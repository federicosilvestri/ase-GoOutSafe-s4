# Advanced Development

In this document we will describe how use advanced techniques that
exploit the development and the debugging of GoOutSafe application.


## Jupyter Notebook

You can use Jupyter notebooks to run the code and create
code snippets that can be useful for other team members.

#### Installation

To install jupyter notebook first you have to download it
inside your virtualenv, by launching the following command

`pip install jupyter ipykernel`

and then, add the virtualenv kernel to jupyter, with this command

`python -m ipykernel install --user --name gooutsafe-venv"`

If you have not installed ipython, please install it, you can
use this [link](https://ipython.org/install.html).


#### Run

To run jupyter you have to execute the command `jupyter notebook`
and the browser will be opened.
Note that to keep the project organized, a notebooks folder has
been created to store all useful notebooks.

Now you have to change the kernel by going 
to Kernel tab, Kernel->Change Kernel->gooutsafe-venv.

To import the packages from `gooutsafe` you have to run a cell
with the following code

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
from gooutsafe import create_app
app = create_app()
```
