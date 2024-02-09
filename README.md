# Bitcoin-Script-Runtime
Implementation of BTC script in Python for CS 263, Winter '24

Creating a README file for setting up a virtual environment (venv) for a Python project is a great way to ensure that contributors or users of your project have clear instructions on how to get started. Below is a template you can use or modify according to your project's specific needs. This example assumes you're using PyPy as the Python interpreter and focuses on Unix-like operating systems (macOS and Linux). For Windows, the activation commands differ slightly, as noted in the previous messages.

---

## Prerequisites

Before you begin, ensure you have met the following requirements:

- PyPy 3.x installed on your system.
- Basic knowledge of Python virtual environments.

## Setting Up a Virtual Environment

Follow these steps to set up a virtual environment for the project. A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages.

### Creating the Virtual Environment

1. Open your terminal.
2. Navigate to the project directory:

    ```sh
    cd /path/to/your/project
    ```

3. Create a virtual environment using PyPy. Replace `myvenv` with the name of your virtual environment:

    ```sh
    pypy3 -m venv myvenv
    ```

    This command creates a new directory `myvenv` in your project directory, containing the virtual environment.

### Activating the Virtual Environment

Before you can start installing packages or running Python code, you need to activate the virtual environment. Activation adjusts your `PATH` so that the PyPy interpreter and scripts in the virtual environment are used by default.

- **On macOS and Linux:**

    ```sh
    source myvenv/bin/activate
    ```

    Your shell prompt will change to show the name of the activated environment.

### Installing Dependencies

With the virtual environment activated, you can now install project dependencies using `pip`:

```sh
pip install -r requirements.txt
```

Replace `requirements.txt` with the path to a file containing a list of items to be installed using `pip install`. If your project does not have a `requirements.txt` file, you can install dependencies as needed using `pip install package_name`.

### Running the Project

```sh
pypy3 main.py \<YOUR SCRIPT FILE\>
```

### Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment to revert to your global Python environment:

```sh
deactivate
```