# Hands-On 0 (HO0)

This assignment is intended to introduce you to the workflow we will use for the Hands-On assignments in CSE 40.

Specifically, this workflow requires you to:
 - Obtain your homework assignments (comprising iPython notebooks, tests, and supplementary files) by cloning private git repositories.
 - Open and edit the provided `assignment.ipynb` iPython notebook while backing up your work with git and running local tests.
 - Submit your work to a server, which will run a private set of tests to grade your submission.

By using this workflow, you will:
 - Gain exposure to `git`, the most popular tool to track changes, backup work, and collaborate with others.
 - Become familiar with using iPython notebooks, a common tool for interactively working with Python.
 - Develop strong software engineer habits like testing code, maintaining consistent style, and using source control.

Note that HO0 is significantly easier than the following assignments, but follows the same workflow.
Use this as an opportunity to setup your development environment and familiarize yourself with the tools we will be using in this course.

## Preparation

First, we will cover the tools we recommend you use in this course.
If you prefer other tools you may use them,
but the TAs may not be able to help you if you encounter difficulties.

### Supported Setups

Below are the supported setups for this course.
This means that these setups are the ones that the course assistants will be able to help you with.
Other setups can work, but the course assistants are not required to help debug those setups.
See respective sections "Command Line" and "Python" for more detailed information.

Python 3.10 or 3.11 is required for this course.
Instructions on how to install Python can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download).
We also recommend you to use [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)) to install Python packages.

For [Linux](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
and [Mac](https://support.apple.com/guide/terminal/execute-commands-and-run-tools-apdb66b5242-0d18-49fc-9c47-a2498b7c91d5/mac),
we recommend using the built-in command lines interfaces, see the links for further information.

For Windows, we recommend using [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/).
Note that this is different than the built-in cmd.exe or PowerShell.

### Command Line

Throughout this course, we will be giving you directions on how to perform various tasks.
The easiest way for us to communicate those instructions and most universally applicable way to do this is by using a command line.
Different command line interfaces are available on all operating systems, and we will go over some recommendations below.
For this class, we specifically recommend POSIX-style command lines which excludes Window's CMD and Powershell.

For Linux and Mac, command line interfaces (e.g. terminals) are available without additional steps.
Guides on getting started can be found [here for Linux](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
and [here for Mac](https://support.apple.com/guide/terminal/execute-commands-and-run-tools-apdb66b5242-0d18-49fc-9c47-a2498b7c91d5/mac)
(as well as all over the internet).

For Windows, we recommend you use Windows Subsystem for Linux (WSL).
WSL is natively built into Windows and is available for free, but requires some additional steps [described here](https://learn.microsoft.com/en-us/windows/wsl/).
The setup for WSL is dependent on your version of Windows and your machine settings,
so make sure to consult the [FAQ](https://learn.microsoft.com/en-us/windows/wsl/faq)
or [troubleshooting guide](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting) if you are having issues getting WSL working.

### Python

We will be using Python (versions 3.10 or 3.11) in this course.
(Most other version >= 3.8 are likely to work, but not officially supported.)
If you don't already have Python installed,
instructions for your OS can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download).
If you are new to Python environments,
We recommend that you try to only have one version of Python installed on your machine at a time
(it is possible to have multiple version, but that can get pretty confusing).

To check your already installed Python version, use:
```sh
python3 -V
```

If you want a refresher on Python, we recommend one of the following resources:
 - [Text Tutorial](https://overiq.com/python-101/)
 - [Video Tutorial](https://www.youtube.com/watch?v=eWRfhZUzrAc)

Note that we will typically use the `python3` command.
Because of the breaking changes between Python 2 and 3,
when you install Python on your machine an additional executable called `python2` or `python3`
(depending on the version of Python you installed)
will also be installed on your machine.
Since this course only uses Python 3,
any use of the `python` command refers to `python3`.
This also applies to the `pip` and `pip3` commands.

### Virtual Environments and Python Packages

In Python, code that is not your own or apart of the [Python standard library](https://docs.python.org/3/library/index.html)
is considered a third-party package (sometimes just shortened to "Python packages" or just "packages").
Each package can be associated with different versions and require specific versions of other packages as dependencies.
Since it can be hard (or maybe even impossible) to get a set of packages that satisfy the versions of every package needed,
we use a tool called [virtual environments](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment), or "venvs" for short.
Virtual environments lets you create as many environments as you want and install a different set of packages (or package versions) to each venv (you can even use different versions of Python).
For example, maybe you are working on this class which uses a new version of the pandas package,
but you are also maintaining an old piece of code you wrote 5 years ago that uses an older version of pandas.
You can just create a venv for each project and have both versions of pandas installed on your machine at the same time.

In this course, we will be using the [standard venv tool](https://docs.python.org/3/library/venv.html) distributed with Python.
(You can use others, but the TAs cannot officially help you with them.)
[This guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
covers how to create an use venvs,
we will reiterate the steps here.
(For Windows, some of the commands are different from the ones listed here, but the general steps are the same.
Refer to the linked guide for the exact commands.)
Before using a venv, you must create it:
```sh
python3 -m venv cse40_venv

# Or to use a specific version of Python.
python3.10 -m venv cse40_venv
```

(In this document, we will assume that your venv is called `cse40_venv` and it is located in the same directory you are running commands in.)
Once created, a venv will be a normal directory that holds all of its information and packages.
To use your newly created venv, you will need to [activate](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment) it:
```sh
source cse40_venv/bin/activate
```

Now you may notice that your shell prompt has changed, this is a sign that the venv is working.
With your venv activated, any packages you install will automatically be installed to the venv,
and any packages used/imported will come from the venv.
If you want to stop using the venv, you can just deactivate it at any time:
```sh
deactivate
```

Note that your shell prompt should have changed back.
Your venv can be re-activated at any time in the same way as before.

Now that we have our virtual environment sorted out, we need to install the packages for this course.
For this course, we only have a single direct Python dependency:
the [ucsc-cse40](https://github.com/ucsc-cse-40/ucsc-cse40) package.
This is a package that we created for this course that contains tools that you will use through this term.
Additionally, it specifies all the other dependencies you will need for this course (like Jupyter and Pandas),
so you can just install this one package and your Python package manager will also install all those dependencies.

In this course we recommend you use [pip](https://pip.pypa.io/en/stable/) to install packages.
You are free to choose whatever system works best for you (like [Conda](https://docs.conda.io/en/latest/)),
but the TAs may not be able to help you if you are using a different setup.
Make sure you have activated your venv before running any pip commands.
To install the ucsc-cse40 package with pip, you can use:
```sh
pip3 install ucsc-cse40
```

For each assignment, you may use the Python standard library, ucsc-cse40,
and any package that [ucsc-cse40 directly specifies](https://github.com/ucsc-cse-40/ucsc-cse40/blob/main/setup.py#L38).
Unless specified, you are to use no other packages.
Use of other packages in assignments may be considered cheating.

### Jupyter Lab

In this course most your assignments will be distributed in the form of iPython notebooks,
and we encourage you to work with them through [Jupyter Lab](https://jupyter.org/).
iPython notebooks, "notebooks" for short, let you write Python code in an interactive environment that
can display visual elements like images and graphs.

Unfortunately, notebooks are not intended to be edited directly like most source code files.
So, we will be using Jupyter Lab to work with our notebooks.
When we run Jupyter Lab, it will open a session in a web browser that allows us to edit and view our notebooks.

For a tutorial on iPython notebooks with Jupyter Lab, see:
 - [Text Tutorial](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
 - [Video Tutorial](https://www.youtube.com/watch?v=HW29067qVWk)

### Git

Source control lets you keep track of different versions of your code,
back it up to remote servers,
and easily share it with people you are working with.
Although you will generally be doing this course's assignments alone,
you will still be using source control to keep track of the changes to your own code and to back it up.
Additionally, we will be distributing your assignments to you via source control.

In this course, we will be using [Git](https://git-scm.com/) for source control.
Git is by far the most popular source control system, with over 96% of
[professional developers preferring Git](https://survey.stackoverflow.co/2022/#version-control-version-control-system).

For hosting our Git repositories, we will be using [GitHub](https://github.com/).
It is free to use and allows you to make unlimited private repositories.
Make sure to sign up if you don't already have an account.

If you want a primer in Git, we recommend one of the following resources:
 - [Text Tutorial](https://nulab.com/learn/software-development/git-tutorial/git-basics/)
 - [Video Tutorial](https://www.youtube.com/watch?v=RGOj5yH7evk)
 - [Official Online Book](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)

#### SSH Keys

When using git, the easiest way to authenticate (login) from the command-line is to use [SSH keys](https://wiki.archlinux.org/title/SSH_keys).
SSH keys are a pair of keys (a private key and a public key) that you can generate to let other people/programs/servers know who you are.
You want to make sure to always keep your private key **private** and never give it to anyone else.
You can share your public key with anyone who wants to authenticate you (like Github).
Github essentially requires that you use SSH keys when working with private repositories
(you can technically use [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic),
but those are not recommended for this course).

By default, SSH keys live in your `~/.ssh` directory (where `~` means your [home directory](https://en.wikipedia.org/wiki/Home_directory).
You can look in there for any existing SSH keys that you have (and skip the next step if you want).
By default, keys start with the `id_` prefix.
Public keys will have the `.pub` suffix, while private keys will have no suffix.

To generate SSH keys, we use the `ssh-keygen` command.
There are various options that you can use to change the security on the key generated,
but the default settings are good enough for this class.
`ssh-keygen` will ask you two questions:
 - Where you want the new key to be placed.
   - If this is your first key, then the default location is fine.
     If this is not your first key, then you should choose some other name that you can remember (in this example, we will use `id_github`).
 - If you want to use a password for your key.
   - This is an additional level of security that you can have, so that every time you use the key it asks for a password.
     A good rule of thumb is that if you are using a machine that is secure and only you use, then you don't need a password.

Here is an example of running `ssh-keygen`:
```
eriq@horsea:~$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/eriq/.ssh/id_rsa): /home/eriq/.ssh/id_github
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/eriq/.ssh/id_github
Your public key has been saved in /home/eriq/.ssh/id_github.pub
The key fingerprint is:
SHA256:FXYWHE2Iu8e7SjSzqwexdKC8EV/4kpdrYM1mkofm4NU eriq@horsea
The key's randomart image is:
+---[RSA 3072]----+
|         .oo=*.  |
|      . o.o+o .  |
|     . + @.o     |
|      = #.E      |
|     . XS%++     |
|      o +.++o    |
|         oo. .   |
|         ....    |
|        .oo...   |
+----[SHA256]-----+
eriq@horsea:~$
```

Note that `ssh-keygen` now created the public and private keys in my `~/.ssh` directory:
```
eriq@horsea:~$ ls -lh ~/.ssh/id_github*
-rw------- 1 eriq eriq 2.6K Oct  2 13:43 /home/eriq/.ssh/id_github
-rw-r----- 1 eriq eriq  565 Oct  2 13:43 /home/eriq/.ssh/id_github.pub
eriq@horsea:~$
```

Now that you have your keys (whether you just generated them or you already have them),
you need to give Github a copy of your **public** key.
So, copy the contents of your `.pub` file.
(If you don't have a fancy way to directly copy a file into your clipboard,
then you can just `cat` the file and use your mouse to copy it).
In our example, we would do:
```
eriq@horsea:~$ cat ~/.ssh/id_github.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDeRxnqHb/XPJ3PhO6Ez5QPNdse1ANoMgQPkjN1+bp50hBrfLwB5lI6SQwvmn6zMr+NwpEg9UjVmniINN9qqehgSVugzQbr0jZz22qssWRuxeE8JFrpaqt0jYjItGJUynmDpuBYeC9Rv05gjg8cGKoBhLbjfFeftRk/pc03MfpfSUCNNMMABtOzfnKnerteGg15YAZ2y58KKNEmAjYRCM3khTcSxVzhL/TfHdO6xky2921Zg190GQtZv/EQIHeQMQG63cI23fd+Bm3p+H8I/WFdLYvTX9eTIxfbdX6wGAgx3FjuKdiamkKDaDniJQMwswXnyEcJ17Y+MYVvFX/8Pq/wbnCj3PWIGLJ9Fx57ORK++wTj7K3uQ33lA0EpjYZjMZXVXFIVHwre9D0XPgbLwb5+26JAxRu1o+mnrqGb/a8fFUO0JyPpuiAWvGiaGSty21sZ1TVPwqJ3N9A0vmxASgLcyfl7AmhIwdwI9DMxyyYQ62HYJJ+EnT9MPQvYv+/WG4U= eriq@horsea
eriq@horsea:~$
```
Note that they keys typically start with `ssh-` and end with a name or email.

Now go into the "SSH and GPG keys" section of your Github settings: https://github.com/settings/keys .
Click the green "New SSH key" button.
Give your key a name and paste the contents of your key into the "Key" section.
Click the "Add SSH key" button and you should be all set!
Now you can use Github in the terminal without needing a password.

If you have a non-standard setup, then there are more complete (but more complicated) instructions all over the internet:
 - [Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
 - [ArchLinux Wiki](https://wiki.archlinux.org/title/SSH_keys) (good for general Linux setups)
 - [MacWorld](https://www.macworld.com/article/671164/how-to-generate-ssh-keys.html)
 - [GitLab](https://docs.gitlab.com/ee/user/ssh.html)
 - [WSL (Ubuntu)](https://ubuntu.com/tutorials/ssh-keygen-on-windows#1-overview)

### Additional Resources

We anticipate that students in this course will have a variety of preparation and prior exposure to tools such as
the command-line, powerful text-editors (such as vim), version control software (such as git), etc.
While we have included links to resources and documentation for some of the tools we expect you to use in this course,
a more comprehensive introductory source is provided by MIT under the course title
["The Missing Semester of your CS Education"](https://missing.csail.mit.edu/).

While this material is not required,
setting up and learning to use proper tools can save you hundreds of hours of work over the course of your undergraduate education,
and having experience with these tools will serve you well in the job market.
Even experienced students are likely to benefit from the linked content!

## Assignment Workflow

0. **Verify GitHub Access**

    First, ensure that you have your GitHub authentication setup so you can work with your own private repositories.
    We recommend using [SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh), since they are widely used, secure, and convenient.
    Generating and using SSH keys was covered in a previous section.
    However if you can't use SSH keys for some reason, then [Personal Access Tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic) are also an option.

    Our instructions will always assume you are using ssh keys.
    If you don't then the commands should be the same, but repository URLs will be different (and you may be asked for a password).

1. **Create a Private Repository Using Our Template**

    The assignment repositories that we provide are GitHub templates,
    so you can create your own private repository from it.

    Starting from this [assignment's GitHub page](https://github.com/ucsc-cse-40/HO0), click on "Use this template" -> "Create a new repository".

    Give this repository a name and an optional description,
    and **make sure your repository is private (the "private" option is selected).**
    Assignments in this class are intended to be completed individually,
    sharing code may result in a violation of academic integrity.

    Now click "Create repository from template" to create your own private version of the assignment repository.

2. **Clone Your Repository**

    Clone your newly created private repository.
    (If you are new to git, "cloning" a repository is when you make a local copy of the repository on your machine.)

    ```sh
    git clone git@github.com:<username>/<repo name>.git
    ```

    For example, Sammy Slug (sslug) would clone HO0 like:
    ```sh
    git clone git@github.com:sslug/HO0.git
    ```

    Now move into the newly created directory:
    ```sh
    cd HO0
    ```

    You may verify the contents of this new "local" repository by running
    ```sh
    ls
    ```

    This should list the following files inside your repository
    (without the comments ("#")).
    ```
    assignment.ipynb    # This is your assignment notebook.
    config.json         # Your course, user, and password (emailed to you) must be set here.
    README.md           # The file you are reading now!
    local_grader.py     # Tests that you can run on your own code before submitting.
    ```

3. **Edit config.json**

    Open up `config.json` and put your information in there:
     - `course` -- The current course you are enrolled in (your instructor / TA will tell you).
     - `assignment` -- The current assignment you are working on (already set).
     - `server` -- The autograding server to submit assignment to (already set).
     - `user` -- Your username (email) for the autograder.
     - `pass` -- The password that was emailed to you in the beginning of this course.
                     If you didn't get the password, forgot it, etc; talk to a TA.

    For example, Sammy Slug would have a `config.json` for HO0 that looks like:
    ```json
    {
        "course": "CSE40",
        "assignment": "HO0",
        "server": "http://lighthouse.soe.ucsc.edu",
        "user": "sslug@ucsc.edu",
        "pass": "1234567890"
    }
    ```

4. **Save Your Changes in Git**

    Now would be a good time to save your changes in git.
    In general, you want to save your changes anytime you
    finish implementing a feature (something new that your code does)
    or fix a bug.
    However, if you are new to coding it can be hard to decide when is the best time to save your code.
    So our general advice is err on the side of caution and save more often,
    and especially make sure to save when you leave your computer.

    "Saving" with git is a two-step process: commit and push.

    The first step is to "commit" your changes,
    this bundles up all the changes you have done since your last commit and adds it to your repo's history.

    First check the status of your repository:
    ```sh
    git status
    ```

    You should see something like:
    ```
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   config.json

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

    You can also see all your exact changes with a diff:
    ```sh
    git diff
    ```

    Which will show something like:
    ```
    diff --git a/config.json b/config.json
    index 13f4424..5ac423f 100644
    --- a/config.json
    +++ b/config.json
    @@ -1,4 +1,4 @@
    {
    -    "user": "sslug",
    -    "pass": "1234567890",
    +    "user": "cse40TA",
    +    "pass": "TAsAreCool",
    }
    ```
    Where lines that start with a "-" are the old code and lines that start with a "+" are your new code.

    Now, we can add the files we want to include in this commit with `git add`.
    (If git has already included this file before and you are just making changes,
    you can also use `git commit -a` and skip the `git add` step.)
    ```sh
    git add config.json
    ```

    Now `git status` will show the file ready to be committed:
    ```
    On branch master
    Your branch is up to date with 'origin/master'.

    Changes to be committed:
    (use "git restore --staged <file>..." to unstage)
        modified:   config.json
    ```

    Finally, you can commit your changes with `git commit`.
    Make sure to always include a commit message with the "-m" argument so you know what you did in this commit:
    ```sh
    git commit -m "Added my credentials to the config.json file."
    ```

    The next part of "saving" your changes with git is to send your changes to GitHub
    (or wherever you are saving your code).
    This is done using a `git push`.
    If you are working with others make sure to get new changes (`git pull` before pushing),
    but otherwise pushing is very simple.

    Do a `git status`, and git will show you that your repo has newer commits than GitHub:
    ```
    On branch master
    Your branch is ahead of 'origin/master' by 1 commit.
    (use "git push" to publish your local commits)

    nothing to commit, working tree clean
    ```
    In this output "origin/master" refers to GitHub, and git says that our local copy is 1 commit ahead of GitHub's version.

    Now we can just push:
    ```sh
    git push
    ```

    Now you should be able to see your local changes online in GitHub.

5. **Work on the Assignment**

    Now, you can start Jupyter Lab and start your assignment!
    ```sh
    jupyter lab
    ```
    This should open up Jupyter Lab in a web browser.
    If not, directions should be printed in the terminal.

    If you are having trouble launching Jupyter Lab,
    consult their [installation documentation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html#pip).
    Make sure your venv is activated.

    If you are getting an error like "bash: jupyter: command not found",
    and running the following fixed it (as per the documentation):
    ```sh
    export PATH="$HOME/.local/bin:$PATH"
    ```
    Then you can put the above in your `~/.bashrc` and you won't have to repeat the comment every time you want to launch Jupyter.

    With Jupyter Lab open in the browser, you can work on your assignment:
     - Open `assignment.ipynb` as listed on the left side of the page.
     - Read the instructions for the assignment, and complete the required task(s).
     - **Make sure to save your work by clicking on the `save` button in the interface!**
    This should be done before testing or submitting.

6. **Test Your Assignment**

    All assignments include a `local_grader.py` script that allows you to see how your code is performing so far.
    It will grade you in the same way that the autograder will grade you and give you similar output.

    **Note that the score your get from the local tests is NOT official.**

    In the command line, you can run the local tests with:
    ```sh
    ./local_grader.py assignment.ipynb
    ```

    If all goes well, you should see something like the following:
    ```
    Autograder transcript for project: Practice Grading for Hands-On 0.
    Grading started at <omitted> and ended at <omitted>.
    Question Q0: 100 / 100
    Question Style: 0 / 0
        Style is clean!

    Total: 100 / 100
    ```

    If not, you will instead see something like the following:
    ```
    Autograder transcript for project: Practice Grading for Hands-On 0.
    Grading started at <omitted> and ended at <omitted>.
    Question Q0: 0 / 100
        Function must return a boolean value.
    Question Style: 0 / 0
        Style is clean!

    Total: 0 / 100
    ```

    We encourage you to expand your copy of `local_grader.py` with your own tests.

    In general, you should develop the habit of frequently running the local tests.
    You have little chance of getting a good score with the real grader if you cannot pass the local tests.
    In particular, you should not spam submissions in lieu of testing!

7. **Submit Your Assignment**

    Once you have passed the local tests and are ready to submit,
    you can do so using the command:
    ```sh
    python3 -m autograder.run.submit assignment.ipynb
    ```

    This will take your `config.json` and `assignment.ipynb` from your current directory
    and send them to the autograding server.
    The autograder will get your code and run a bunch of secret tests on it to assign you a grade.
    It will return output formatted about the same as the local tests.

    The autograder records all your submissions (the code, time, and score).
    The score you received on your most recent submission is your current grade for the assignment
    (not counting late assignments and manually graded components).

    You can make as many attempts as you want.
    However if we find you abusing the autograder (e.g. repeatedly failing tests that would have been caught by testing locally),
    then you can lose points.
    Any attempt to willingly circumvent the autograder (e.g. "hacking" it)
    may result in an immediate F in this class and a referral for academic integrity.

## Extra

Throughout the course, there may come a time when a mistake is found in an assignment and the TAs need to get you a new version of the assignment.
In these cases, you will be able to update your repository by pulling changes from the template assignment repository.
The TAs will always inform you of the exact command you will have to use, but it will look something like:
```sh
git pull --allow-unrelated-histories --strategy recursive --strategy-option theirs git@github.com:ucsc-cse-40/HO0.git
```

Components of the command:
 - `git pull` -- We are pulling in new changes.
 - `--allow-unrelated-histories` -- Ignore the different histories that your private repo and the template repo have.
 - `--strategy recursive --strategy-option theirs` -- Prefer changes made by the TAs ("theirs") over your own changes.
 - `git@github.com:ucsc-cse-40/HO0.git` -- The git URL of the template assignment repo.

If things get too confusing, you can always just start from step 1, make a new repo, and copy over your changes.
