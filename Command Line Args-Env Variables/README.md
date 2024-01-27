# Command Line Arguments
- In Python, command-line arguments are values that are passed to a script or program when it is executed from the command line. These arguments provide a way to customize the behavior of the script or provide input data to the program. Python provides the `sys` module to access command-line arguments through the `sys.argv` list.

- Here's a basic overview of how command-line arguments work in Python:

`sys.argv`:

- `sys.argv` is a list in the `sys` module that contains the command-line arguments passed to the script.
- `sys.argv[0]` is the script name itself, and the rest of the elements in the list represent the arguments provided by the user.

# Environment Variables
Environment variables in Python serve as a way to configure and control the behavior of programs and scripts. They are variables outside the program that can be accessed by the program at runtime. These variables are set in the operating system environment and can be read by the Python script or program to adapt its behavior accordingly.In Python, the `os` module is commonly used to access environment variables. Environment variables are often used for the following purposes:

**1. Configuration:**
 - Environment variables are commonly used to store configuration parameters for a program.
 - Instead of hardcoding values like file paths, API keys, database connection strings, or other configuration settings directly in the code, developers can use environment variables to make the program more flexible and configurable without modifying the code.

**2. Security:**
- Sensitive information like passwords, API keys, and other secrets should not be hard-coded in the source code for security reasons.
- By using environment variables, developers can keep sensitive information separate from the codebase and control access to these variables through the environment.

**3. Portability:**
- Environment variables enhance the portability of code across different environments.
- A script or program can be developed and tested in one environment with specific configurations, and then deployed to another environment by adjusting the environment variables without modifying the code.

**4. Dynamic Configuration:**
- Environment variables allow for dynamic configuration changes without restarting the program.
- If a program reads configuration settings from environment variables, changes can be made to the environment variables without stopping and restarting the application.

**5. Compatibility:**
- Environment variables provide a standardized way for different programs and services to communicate and share configuration information.
- Many libraries and frameworks in Python provide support for reading configuration from environment variables, making it easy to integrate different components.

- N.B: To set environment variables externally, it depends on the operating system. For example, on Unix-based systems, you might use the `export` command, while on Windows, you can use the `set` command.


