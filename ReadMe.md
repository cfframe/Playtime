# ReadMe for Playtime
Figuring things out, sandbox.  Some personal notes that may not apply to all systems.

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
```
mamba install --file requirements.txt
```
