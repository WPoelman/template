# package_name

Template repo for Python software and / or research projects.

1. Find and replace `package_name` with the name of the package and `**description**` with a brief description.
2. Specify dependencies and minimal Python version.
3. Choose a license and paste it into `LICENSE`
4. Check if the pre-commit hooks make sense (e.g., check bash files if there are any, etc.)
   [see here](https://pre-commit.com/hooks.html) and check `.pre-commit-config.yaml`
5. Run the following commands:

   ```zsh
   # Create a `pyenv` virtual env:
   pyenv virtualenv <python_version> <package_name>
   pyenv activate <package_name>
   pyenv local <package_name> # And make it local so it's always active in this folder
   pip install -e ".[dev]"
   pre-commit install # associate with git repo
   pre-commit autoupdate # update pre-commit hooks
   pre-commit run --all-files
   ```

6. Everything should be ready for development!

## Usage

```zsh
pip install git+https://github.com/WPoelman/package_name
```

## License
