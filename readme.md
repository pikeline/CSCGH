# Github

## Download Git

If you have not yet downloaded git, do so at https://git-scm.com/downloads

## Github

Hello!

This is a simple tutorial about working with **github**. To get here, you should have made a folder, used the `cd` command to set your terminal to that folder, than run the command `git clone https://github.com/pikeline/CSCGH` to pull a copy of the code (including its git history) to your own machine. If you are interested in how it is done, check out `How this was made` below.

This code contains a program for the game fizzbuzz, which you can learn about in 'fizzbuzz.py'. It is a pretty simple code that currently contains a bug. Fizzbuzz is meant to be done from 1 to 100, but this implementation only works for 0 to 99! We could just edit this and be done with it, but we might accidentally delete something important in the process. What if I wanted it to be from 0 to 99?

To preserve the history of our code, we use git. Git is a powerful tool for controlling our code as it grows and evolves. In order to fix our bug, we should create a new branch to hold our bug fix.

`git checkout -b bugfix`

`checkout` is a versatile command, and I wager that 50% of your time in git will be using checkout. `checkout` is, essentially, telling git to change my view to the branch `bugfix`, with `-b` telling git to create the branch, then swap my view to it. This could also be done using `git branch` and `git switch`.

`git branch` will also show all of the branches that currently exist.

Now that we are in a new branch, we can make changes to our code. Let's change the `range` in `fizzbuzz.py` from `0,100` to `1,101`. Our changes aren't actually saved yet. We haven't told git to track these modifications. We can do this with 

`git add fizzbuzz.py`

`git commit -m "Fixed a bug involving incorrect intervals"'

These commands will save our changes inside the bugfix branch. Now, if we use `git checkout main` to go back to the main branch, we should not see our bugfix.

This is the most important feature of git, as it allows multiple developers to develop in tandem without constantly getting in the way of each other.

### Tangent

Let's look into the past to figure out when this bug was introduced. For now, we will simply look manually to figure it out. We can do this using `git log` and `git checkout`. Ignore the commits with messages stating they updated readme, I made this exercise using git to keep track of my changes!

(To go back to the present, use `git checkout main`)

`git log`

`git checkout ddc1cef914c7c3989ab01507b26364313a4698bd`

We can checkout each commit's id number to view the code at that particular state of time. Looks like that bug was there since the beginning. Oops!

### Applying the bugfix

Let's actually apply our bugfix, and update our repository. We should currently be in the main branch. If not, check it out with `git checkout main`. To apply it, we can simply merge it into main with `git merge bugfix`. This will move all the changes made in `bugfix` to `main`. At this point, if there are any conflicts, you should be prompted to resolve them, but that is a topic for another day (Ex: one developer deletes a line, but another developer modifies it). All that is left to do is to clean up after ourselves by deleting the `bugfix` branch with `git branch -d bugfix`.

### Or is it?

We have only updated this change for ourselves. It would not be reflected for anyone else who `clone`s the repository. We need to update github.

At this point, we could run `git push origin main` to create a fork on github and run through that process, but instead, we will create and update our own repository.

Go to github, and log in to your own account. From there, create a repository. In the quick set up, copy and paste the link that ends with `.git`. Now, enter

`git remote set-url origin <copy pasted url>`

into the terminal. Then, we can `push` our changes to the repository with

`git push origin main`

And, now, if you refresh the page, we can see the changes reflected in your own personal repository!


## How this was made

If you are curious to see how this was made, read this section.

First, I created an empty folder to put my project in. Then, I opened up my terminal, and used `cd` + the filepath to change my terminal's location to the folder's directory. I used `git init` to initialize a git history. I made this `readme.md` and `fizzbuzz.py` files, tracked them in git using `git add`, and made a commit with `git commit -m 'Initial commit'`. As a reminder, you can see which files are tracked and untracked with `git status`.

Then, I opened up github and created a repository. They provide some instructions on setting up a connection quickly. I added the repository as a remote repository named `origin` with `git remote add origin https://github.com/pikeline/CSCGH.git`. Then, I pushed my files to github with `git push origin main`

Next, I made a new branch with `git checkout -b fizzbuzz_class`. This created a new branch on git, allowing me to work on modifying `fizzbuzz.py` in a separate environment while keeping the current version of the files intact. This created a new branch (`-b`) named `fizzbuzz_class` and moved my git location to the new branch. Now, any changes I make will be on this branch. But first, I have to add them using `git add` and `git commit`. Also, you can see what branches are present at any time using `git branch`.

To make the changes I made be reflected in `main`, you need to merge this. This is pretty simple. Swap which branch you are in to `main` with `git checkout main`. Then, use `git merge fizzbuzz_class` to update main with the branch's history. After this, we can delete `fizzbuzz_class` with `git branch -d 'fizzbuzz_class`.