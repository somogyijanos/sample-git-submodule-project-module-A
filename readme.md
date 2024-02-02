# Module: `mymodule`
This is a sample module (git submodule) which is used in [this](https://github.com/somogyijanos/sample-git-submodule-project-super) repository as an example submodule repository.

## Features
- repository with docker compose environment
- just a silly tool to count files and folders in an input path using Python 3.12

## Usage

### Run from command line
```bash
cd sample-git-submodule-project-module-A
docker compose up -d
docker compose exec dev python src/tools/contents.py <path-in-container>
```

### Develop from VS Code
```bash
cd sample-git-submodule-project-module-A
docker compose up -d
```
Now open VS Code and reopen repository folder in devcontainer. Happy coding!

To test, in the container command line run:
```
python src/tools/contents.py <path-in-container>
```