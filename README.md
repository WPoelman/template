# package_name

Template repo for Python software and / or research projects.

1. Find and replace `package_name` with the name of the package and `**description**` with a brief description. Also change the author information in `pyproject.toml` and this readme where needed.
2. Specify dependencies and minimal Python version.
3. Choose a [license](https://choosealicense.com/) and paste it into `LICENSE`.
4. Check if the pre-commit hooks make sense (e.g., check bash files if there are any, etc.)
   [see here](https://pre-commit.com/hooks.html) and check `.pre-commit-config.yaml`.
5. Run the following commands:

   ```zsh
   pyenv virtualenv <python_version> <package_name> # Create a `pyenv` virtual env
   pyenv activate <package_name>
   pyenv local <package_name> # And make it local so it's always active in this folder
   pip install -e ".[dev]"
   pre-commit install # associate with git repo
   pre-commit autoupdate # update pre-commit hooks
   pre-commit run --all-files
   ```

6. Everything should be ready for development!

## Optional

* Additional documentation are stored in `docs`.
* Tests are put in `tests` and require development dependencies, which are listed under `dev` in `pyproject.toml`. These are installed using `pip install <package_name>[dev]`.
* For usage of [`hydra`](https://github.com/facebookresearch/hydra) and [`submitit`](https://github.com/facebookincubator/submitit) in combination with the VSC, I've added configs that work for requesting single GPUs in `config/slurm`. The names of the files correspond to cluster and the GPUs available there, for more details see [Genius](https://docs.vscentrum.be/leuven/tier2_genius.html) and [wICE](https://docs.vscentrum.be/leuven/tier2_wice.html). Make sure to fill in your own `project` (provided by the VSC), `mail_user` and `slurm_time` (note that `debug` partitions have a 30 minute maximum).

## Usage

```zsh
pip install git+https://github.com/WPoelman/package_name
```

## License
