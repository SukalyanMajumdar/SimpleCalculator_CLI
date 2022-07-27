# SimpleCalculator_CLI
A Simple CLI based Python Calculator in .exe, version controlled in Github, tested and built in Azure DevOps

## Release / Download Link :
https://devsa3.blob.core.windows.net/simplecalculatorrelease/SimpleCalculator_CLI.zip

Azure Devops configuration : https://dev.azure.com/KAMZcorp/SimpleCalculator_CLI/_build

## Changelog :
### Version : 1.0.3
* Fixed bug : Negative Integer inputs fixed
* Fixed typo : ui.py

## Functionality :
This CLI based Python app performs the four basic operations between 2 integers
* Addition
* Subtraction
* Multiplication
* Division

## Procedure :
1. Welcome message is displayed
2. User is provided with four basic operations
3. Upon user input, the input is validated
4. Upon invalid input, the code returns to Step 2
5. Upon valid input, the user is requested to provide the first integer value
6. Post validation of the first integer, The user is requested to provide the second integer value
7. Post validation of the second integer, chosen operation is performed and result is displayed, 'Zero Division Error' is carefully handled
8. The user is requested to input if the calculator should be re-run from beginning
9. Upon affirmative confirmation, the code returns to Step 2
10. Upon negative confirmation, exit message is shown
11. Code terminates

## Structure :
1. The Core Code is written in 3 main modules i.e. ui.py, calc.py, test_calc.py
2. ui.py : Used for every input/display aspect of the project
3. calc.py : Used for the for basic operations and validation of inputs, in backend
4. test_calc.py : Used for validating the calc.py file with built-in python module Unittest

## Implementation :
1. (Development) A successful python environment setup is to be done (requirement.txt provided)
2. (Lint Test) After any modificaion, the .py files are validated for linting with flake8
3. (Unit Test) After linting errors are corrected, the same test_calc.py is called to validate the calc.py file
4. (Build) After successful unittest the pyinstaller module is called and a .exe for ui.py is built
5. (Release) After successful build, the .\dist folder is shipped to a Azure Storage Account
6. The Entire process is version controlled in Github and automated using CI/CD pipelines by Azure DevOps

requirements:
* altgraph==0.17
* flake8==3.9.2
* future==0.18.2
* Jinja2==3.0.1
* MarkupSafe==2.0.1
* mccabe==0.6.1
* packaging==21.0
* pefile==2021.5.24
* pycodestyle==2.7.0
* pyflakes==2.3.1
* pyinstaller==4.5.1
* pyinstaller-hooks-contrib==2021.2
* pyinstaller-versionfile==2.0.0
* pyparsing==2.4.7
* pywin32-ctypes==0.2.0
* PyYAML==5.4.1
