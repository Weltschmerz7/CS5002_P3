This is an instruction to run the scripts. 

To create an virtual environment: python -m venv <your_virtual_environment_name>

To activate an virtual environment: source venv/bin/activate

Download all required packages: pip install -r requirements.txt

To add the git log into gitlog.txt: **git log --graph --decorate --all --pretty=format:"%h %ad | %s%d [%an]" --date=local > gitlog.txt**  This formatting includes more detail and a timestamp for the gitlog.txt

I have added a post-commit file in .git/hooks to automatically update the gitlog.txt after each commit using the following step:
1. go to hidden directory .git/hooks
2. use nano to create a post-commit file
3. Write a sheban line inside the file and add the line to update log there
4. Use chmod +x post-commit to make it executable

To clear the gitlog.txt: **> gitlog.txt** to overwrite the file with nothing

First run the **data_mining.py** in the terminal to clean the data and verify that the data is of correct format.