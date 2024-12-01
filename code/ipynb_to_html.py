#!/usr/bin/env python3 
import subprocess

def convert_to_html (notebook, template = 'classic'):
    '''This function can turn the jupyter notebook into high quality html format'''
    # run nbconvert to convert the notebook to HTML
    html_report = subprocess.run(['jupyter','nbconvert', '--to', 'html', '--template', template, '--embed-images', notebook], check=True)
    # replace the name
    html_report = notebook.replace('.ipynb', '.html')
    print(f'html version of the notebook have been created {html_report}')
    return html_report

convert_to_html('./notebooks/CS5002_P3_200013825.ipynb')

