# Python-based Research Projects

This is a collection of guides and tips for research projects in Python. They are intended to show you some (*subjective*) best practices and making you aware of the existence of certain tools that will make working in complex environments hopefully more frictionless.

## Flemish Super Computer (VSC)

For running experiments, you very likely need computing power in the form of GPUs. As a KU Leuven student, you have access to the [VSC](https://www.vscentrum.be/) and get some free compute credits that are generally enough to do a master thesis project. To sign up, follow the steps described in the documentation [here](https://docs.vscentrum.be/access/vsc_account.html#generic-access-procedure). When asked for "ZAP personnel as a supervisor", you can fill in Miryam de Lhoneux.

## Source control

Git is the backbone of tracking all software development. I recommend you get familiar with *at least*:

* A hosting provider, such as GitHub (or GitLab, BitBucket)
* Repositories
* Pull requests (or merge requests if you're in the GitLab world)
* Branches
* Merging branches
* Descriptive commit messages

There are countless resources and basic tutorials that go into this, like [this](https://www.freecodecamp.org/news/git-and-github-for-beginners/) one.

## Useful software

### Parameters

If a project is small enough, it's probably fine to use [`argparse`](https://docs.python.org/3/library/argparse.html) or [`click`](https://click.palletsprojects.com/en/stable/) for passing parameters and arguments. If your setup gets bigger, something like [`hydra`](https://github.com/facebookresearch/hydra) is useful. This library allows you to specify configurations in `yaml` files instead of having to pass many arguments. It's very good at allowing you to write reproducible pipelines, as you can overwrite one variable on the command line, while keeping the rest of your config(s) the same.

### Working with slurm

Most compute clusters run on [`slurm`](https://slurm.schedmd.com/overview.html), a workload manager. You submit 'jobs' (something to compute) that are put in a queue and picked up and ran once there's enough compute available for what you requested. If you've provided your email, you can be notified if the job has started, completed successfully, failed, etc.
Most [tutorials](https://docs.vscentrum.be/jobs/job_submission.html) show how to make `sbatch` scripts by hand, these are bash-like scripts that describe what to do in your job and what's required for them to run. This is fine for one-off jobs, but for larger scale setups, this becomes cumbersome. This is where a package like [`submitit`](https://github.com/facebookincubator/submitit) comes in handy. It allows you to programmatically (i.e., from within Python) submit and monitor jobs. It will automatically create `sbatch` scripts for you and submit the job. Combined with `hydra`, you can, for instance, create configs for different clusters and just swap out the config, while the rest stays the same. I've added specific hydra configs for `submitit` that correspond to the partitions available on the VSC.

### Weights and Biases

To keep track of machine learning experiments, [`wandb`](https://wandb.ai/site/) has become a standard tool. If you intend to run experiments on the VSC, I recommend to make a free `wandb` account, and use it to log some common statistics like training losses and performance metrics (train and validation). This helps a lot in knowing what's happening (and if there's something happening), to catch training errors early and to keep track of what you've tried.

## Environment

### Local

If possible, a Unix-based environment (MacOS, Linux) is *highly* recommended, as virtually all super computers and compute clusters are Unix-based and the switch between Windows and another environment can bring unneeded headaches. If you want to use Windows, install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) or a [Virtual Machine](https://www.virtualbox.org/) with a Long Term Support version of Linux, such as [Ubuntu](https://ubuntu.com/download/desktop). All instructions here are intended for a Unix-based environment, native Windows *might* work, but there are no guarantees or promises as I've not tested it!

To avoid versioning and dependency problems, make sure to isolate different projects. I recommend to install [`pyenv`](https://github.com/pyenv/pyenv) and [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) as they are easy to set up and fast. Conda is a popular alternative, and it's recommended to use it if you intend to run jobs on the VSC, but it's quite heavy and slow. It's personal preference, but I like to use `pyenv` locally. Using Conda everywhere is a sane alternative as well.

To make your life easier, I generally recommend to use an automation framework like `pre-commit` (or shell scripts or  `make` if you want to roll your own). These types of frameworks can take care of checking your code for common mistakes and fix many things automatically. They also help to prevent common git errors from happening, such as adding private keys or accidentally committing enormous files.

### VSC

On the VSC, it's best to use Conda as it includes a lot of things out of the box. For a good reference on Conda, check the VSC documentation [here](https://docs.vscentrum.be/software/python_package_management.html#install-python-packages-using-conda).

## Starting a project

I recommend to use this template repository: <https://github.com/WPoelman/template>. It includes the following:

* A package structure for a Python project.
* Instructions for `pyenv` and how to automatically select the correct env for your project.
* A skeleton setup of `pre-commit` with some common checks.

To get started, click `Use this template` and create a new repository. Clone this repository onto your local machine and follow the instructions listed in the `README.md` of the template.

To get started on the VSC, you need to do the following steps (just once):

1. Get access, as described above.
2. SSH into the VSC.
3. Set up Conda and create an environment for your project.
4. Clone your git repository.
5. Install your dependencies and package.

Once you have this up and running, the general workflow will be:

1. Develop software on your local machine.
2. Make sure it works.
3. Push commits to your git repository.
4. Once you're ready to run experiments:
   1. SSH into the VSC.
   2. Pull the latest changes from your repository onto the VSC and re-install your package (or install it in [`editable mode`](https://stackoverflow.com/questions/35064426/when-would-the-e-editable-option-be-useful-with-pip-install)).
   3. Submit a test job to one of the `debug` partitions on the VSC (for [Genius](https://docs.vscentrum.be/leuven/genius_quick_start.html#running-debug-jobs) or [wICE](https://docs.vscentrum.be/leuven/genius_quick_start.html#running-debug-jobs)). These partitions are intended to quickly test if your job runs at all.
   4. If the debug job works, you can submit the full version of your job(s) to the 'real' partitions and run your experiments.
5. Check progress in `wandb` and, once the jobs successfully completes, process the outputs (CSVs with results, graphs, logs, models, etc.)

Naturally, you can deviate from this workflow, but I recommend to first get this up and running before trying more complex things like working remotely on the VSC or interactive jobs.

## Miscellaneous

* Always *over*estimate how long a job will take by ~25% (or adding a couple hours for longer jobs). You never know what will happen (timeouts, retries, etc.); better safe than sorry. If your job finishes early, the 'extra' time requested will not be deducted from your credits, so apart from longer queue times, there's not really a downside to doing this.
* If you run into storage issues, switch the huggingface cache folder location to `$VSC_SCRATCH` instead of `$VSC_HOME`. For more information, check the [documentation](https://docs.vscentrum.be/data/storage_locations.html).
