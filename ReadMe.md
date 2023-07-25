***
***
# ReadMe for Playtime
Figuring things out, sandbox.  Some personal notes that may not apply to all systems.

Files `inc_dec.py` and `test_unittest.py` added for troubleshooting. 


## Using mamba or conda in VSCode
### Set workspace settings
Assuming virtual environment `Playtime`, created with `mamba`. Will be slightly different path with `conda`.
```json
{
    "terminal.integrated.profiles.windows": {
            "Command Prompt": {
                "path": "cmd.exe",
                "args": [
                        "/K",
                        "${env:LocalAppData}\\mambaforge\\Scripts\\activate.bat ${env:LocalAppData}\\mambaforge & mamba activate Playtime"
                ]
            }
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt"
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
C:\Python\3.10.11\python.exe -m venv env   # create virtual environment
env/Scripts/activate   # activate the virtual environment
python -m pip install --upgrade pip
python -m pip install -r requirements.txt   # install packages in virtual env
```
