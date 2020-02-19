# Onboarding

1. How easily can you build the project? Briefly describe if everything works as documented or not

    * `Did you have to install a lot of additional tools to build the software?`

    Since it is a Python project, Python3 obviously had to be installed to run the project. Additionally, the following Python dependencies had to be installed (via pip):

    ```
    - flake8
    - python-coveralls
    - coverage
    - nose
    - pytest
    - tox
    - black
    ```

    *  `Were those tools  well documented?`

    The author takes for granted that the user knows how to install Python dependencies, e.g. via `pip`. The requirements were found in the test_requirement.txt file. However, it was not documented in the README file.

    *  `Were other components installed automatically by the build script?`

    It was simple to run the script, although no build script was included, since it was written in Python. With an example provided by the author, we could confirm that it was working.

    *  `Did the build conclude automatically without errors?`

    Both the build and the tests ran without any errors.

    *  `How well do examples and tests run on your system(s)?`

    The examples and tests run without any issues on all of our systems.

2. Do you plan to continue or choose another project?

Yes. We will continue with this project.
