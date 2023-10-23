## Github

Hello!

This is a simple tutorial about working with **github**. To get here, you should have made a folder, used the `cd` command to set your terminal to that folder, than run the command `git clone https://github.com/pikeline/CSCGH` to pull a copy of the code (including its git history) to your own machine.


## How this was made

If you are curious to see how this was made, read this section.

First, I created an empty folder to put my project in. Then, I opened up my terminal, and used `cd` + the filepath to change my terminal's location to the folder's directory. I used `git init` to initialize a git history. I made this `readme.md` and `fizzbuzz.py` files, tracked them in git using `git add`, and made a commit with `git commit -m 'Initial commit'`. As a reminder, you can see which files are tracked and untracked with `git status`.

Then, I opened up github and created a repository. They provide some instructions on setting up a connection quickly. I added the repository as a remote repository named `origin` with `git remote add origin https://github.com/pikeline/CSCGH.git`. Then, I pushed my files to github with `git push origin main`