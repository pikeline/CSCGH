## Github

Hello!

This is a simple tutorial about working with **github**. To get here, you should have made a folder, used the `cd` command to set your terminal to that folder, than run the command `git clone https://github.com/pikeline/CSCGH` to pull a copy of the code (including its git history) to your own machine. If you are interested in how it is done


## How this was made

If you are curious to see how this was made, read this section.

First, I created an empty folder to put my project in. Then, I opened up my terminal, and used `cd` + the filepath to change my terminal's location to the folder's directory. I used `git init` to initialize a git history. I made this `readme.md` and `fizzbuzz.py` files, tracked them in git using `git add`, and made a commit with `git commit -m 'Initial commit'`. As a reminder, you can see which files are tracked and untracked with `git status`.

Then, I opened up github and created a repository. They provide some instructions on setting up a connection quickly. I added the repository as a remote repository named `origin` with `git remote add origin https://github.com/pikeline/CSCGH.git`. Then, I pushed my files to github with `git push origin main`

Next, I made a new branch with `git checkout -b fizzbuzz_class`. This created a new branch on git, allowing me to work on modifying `fizzbuzz.py` in a separate environment while keeping the current version of the files intact. This created a new branch (`-b`) named `fizzbuzz_class` and moved my git location to the new branch. Now, any changes I make will be on this branch. But first, I have to add them using `git add` and `git commit`. Also, you can see what branches are present at any time using `git branch`.

To make the changes I made be reflected in `main`, you need to merge this. This is pretty simple. Swap which branch you are in to `main` with `git checkout main`. Then, use `git merge fizzbuzz_class` to update main with the branch's history. After this, we can delete `fizzbuzz_class` with `git branch -d 'fizzbuzz_class`.