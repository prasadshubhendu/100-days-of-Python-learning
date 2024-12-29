Here’s a step-by-step tutorial that covers signing up for GitHub, installing the GitHub CLI, creating a repository using GitHub CLI, and working with files/folders, pulling, and pushing changes to a repository.
----------------------------------------------------------------


1. GitHub Sign-Up

Step 1: Create a GitHub Account

Open your browser and go to GitHub.
Click on the Sign Up button in the top right.
Fill in your details:
Username: Choose a unique username.
Email Address: Use your email.
Password: Create a strong password.
Follow the instructions to complete the sign-up process 	(e.g., email verification).
Once verified, log in to your GitHub account.

2. Install GitHub CLI (Command Line Interface)

Step 1: Install GitHub CLI

Visit the GitHub CLI installation page and download the installer for your operating system (Windows, macOS, or Linux).
Windows: Use the .msi installer.
Run the installer and follow the prompts.
macOS: Use Homebrew:
	brew install gh
Linux: Follow the instructions for your specific distribution. For example:
	Debian/Ubuntu:
		sudo apt install gh

Step 2: Authenticate with GitHub CLI
After installation, open your terminal/command prompt and authenticate with GitHub:
	gh auth login
Follow the prompts:
Select GitHub.com.
Authenticate via web browser or by providing a token.


3. Create a GitHub Repository Using GitHub CLI

Step 1: Create a New Repository
To create a new repository, run the following command:
	gh repo create <repository-name>
Replace <repository-name> with the name you want for your repository.

You’ll be prompted with a few options:
	Choose whether the repo is public or private.
	Optionally, add a README file or initialize with a 	template.
For example, to create a private repository:
		gh repo create my-new-repo --private

Step 2: Clone the Repository Locally
Once the repository is created, clone it to your local machine:
	gh repo clone <repository-name>
Example:
	gh repo clone my-new-repo
This creates a local copy of the repository in your current directory.

4. Daily File/Folder Creation and Managing Changes

Step 1: Create New Files/Folders
In your local repository, create a new folder or file. For example:

To create a folder:
	mkdir <foldername>
To create a new file inside the folder:
		touch day2/newfile.txt

Step 2: Stage the Changes
Once you’ve created or modified files, you need to stage them to be tracked by Git. Use the following command:
	git add .
This stages all changes in the current directory. You can also specify specific files/folders:
		git add day2

Step 3: Commit the Changes
Next, commit the changes with a meaningful message:
		git commit -m "Added new folder and file for day2"

Step 4: Push the Changes to GitHub
Push your local changes to the GitHub repository:
	git push origin main
This uploads your changes to the main branch on GitHub.


5. Pulling and Pushing Changes to GitHub

Step 1: Pull Changes (If Any)
Before making changes, it’s good practice to pull the latest version of the repository from GitHub. This ensures you’re working with the most recent changes:
	git pull origin main

Step 2: Push New Changes
After committing your changes locally, you can push them to GitHub as shown earlier:
	git push origin main

6. Managing the Repository Over Time

Create New Files/Folders Daily
You can repeat the steps to create new files or folders daily. For example, each day, you can create a new folder for the day (like day3, day4, etc.) and commit and push them to the repository.

Track Changes with Git
Always remember to:
Stage changes (git add .)
Commit changes (git commit -m "message")
Push to GitHub (git push origin main)

Summary of Commands

GitHub CLI Setup:
	gh auth login: Authenticate with GitHub CLI.
	gh repo create <repo-name>: Create a repository.
	gh repo clone <repo-name>: Clone the repository 	locally.

Daily Workflow:
	mkdir <folder-name>: Create a new folder.
	touch <file-name>: Create a new file.
	git add .: Stage all changes.
	git commit -m "message": Commit changes.
	git push origin main: Push changes to GitHub.

Updating Your Local Repo:
	git pull origin main: Pull the latest changes from 	GitHub.

This should help you manage your repository daily using GitHub CLI. 