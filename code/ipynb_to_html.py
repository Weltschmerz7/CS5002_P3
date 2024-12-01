import os
import subprocess

def convert_to_html (notebook):
    '''This function can turn the jupyter notebook into high quality html format'''
    # run nbconvert to convert the notebook to HTML
    subprocess.run(['jupyter','nbconvert', '--to', 'html', notebook], check=True)
    html_report = notebook.replace('.ipynb', '.html')
    print(f'html version of the notebook have been created {html_report}')



# generate high quality report
# jupyter nbconvert --to html --template classic <notebook.ipynb>
