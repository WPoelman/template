# Package management

I highly recommend using [`uv`](https://docs.astral.sh/uv/getting-started/) to manage your dependencies and environments, both locally and on the cluster.

1. Install it and run `uv init <package-name>`.
2. Choose a [license](https://choosealicense.com/) and paste it into `LICENSE`.
3. Check if the pre-commit hooks make sense (e.g., check bash files if there are any, etc.)
   [see here](https://pre-commit.com/hooks.html) and check `.pre-commit-config.yaml`.
4. Run the following commands:

   ```zsh
   uv sync
   pre-commit install # associate with git repo
   pre-commit autoupdate # update pre-commit hooks
   pre-commit run --all-files
   ```

5. Everything should be ready for development!

## Optional

* Additional documentation are stored in `docs`.
* Tests are put in `tests` and require development dependencies, which are listed under `dev` in `pyproject.toml`. These are installed using `pip install <package_name>[dev]`.
* For usage of [`hydra`](https://github.com/facebookresearch/hydra) and [`submitit`](https://github.com/facebookincubator/submitit) in combination with the VSC, I've added configs that work for requesting single GPUs in `config/slurm`. The names of the files correspond to cluster and the GPUs available there, for more details see [Mindwell](https://docs.vscentrum.be/leuven/tier2_mindwell.html) and [wICE](https://docs.vscentrum.be/leuven/tier2_wice.html). Make sure to fill in your own `project` (provided by the VSC), `mail_user` and `slurm_time` (note that `debug` partitions have a 30 minute maximum).

## Next steps

Read the [docs/quickstart-guide.md].

## License
