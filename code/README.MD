This is an instruction to run the scripts. 

To create an virtual environment: python -m venv <your_virtual_environment_name>

To activate an virtual environment: source venv/bin/activate

Download all required packages: pip install -r requirements.txt

To add the git log into gitlog.txt: **git log --graph --decorate --all --pretty=format:"%h %ad | %s%d [%an]" --date=local > gitlog.txt**  This formatting includes more detail and a timestamp for the gitlog.txt

To clear the gitlog.txt: **> gitlog.txt** to overwrite the file with nothing

First run the **data_mining.py** in the terminal to clean the data and verify that the data is of correct format.