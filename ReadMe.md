***
***
# ReadMe for Playtime
Figuring things out, sandbox.  Some personal notes that may not apply to all systems.

Files `inc_dec.py` and `test_unittest.py` added for troubleshooting. 


## Using conda or mamba in VSCode
### Set workspace settings
```json
{
    "python.pythonPath":"C:/Users/[USERNAME]/AppData/Local/mambaforge/envs/Playtime/python.exe",
    "python.terminal.activateEnvironment": true
}
```
For the above, a *new* cmd terminal will activate the environment.

### Install from requirements.txt
```bash
mamba install --file requirements.txt
```
## The pip alternative
Alternatively, if you have a version of python installed, can use something like:
```bash
C:\Python\3.10.6\python.exe -m venv env   # create virtual environment
env/Scripts/activate   # activate the virtual environment
python -m pip install --upgrade pip
python -m pip install -r requirements.txt   # install packages in virtual env
```
