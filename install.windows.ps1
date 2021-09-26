# To run this script directly, run this in an elevated admin PowerShell prompt:
#     Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/approvals/ApprovalTests.Python/master/install.windows.ps1 | Invoke-Expression

# This script is intended to setup a dev machine from scratch. Very useful for setting up a EC2 instance for mobbing.
#


iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/windows.ps1 | iex
# iwr -useb https://raw.githubusercontent.com/JayBazuzi/machine-setup/main/python-pycharm.ps1 | iex

iwr -useb cin.st | iex
choco feature enable --name=allowGlobalConfirmation
choco install beyondcompare
choco install python --version=3.6.7 
choco install pip
choco install pycharm

# Keyboard rotation for Dvorak
Invoke-WebRequest -UseBasicParsing https://raw.githubusercontent.com/LearnWithLlew/MobTime.keyboardswitching/main/install.windows.ps1 | Invoke-Expression

syspin "C:\Program Files (x86)\JetBrains\PyCharm 2020.3.2\bin\pycharm64.exe" "Pin to taskbar"

pip install tox

# Clone repo
& "C:\Program Files\Git\cmd\git.exe" clone https://github.com/approvals/EmptyFiles.Python.git C:\Code\EmptyFiles.Python
cd C:\Code\EmptyFiles.Python

tox -e dev
tox -e lint

# Done
cls
echo "Done!"
