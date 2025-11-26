import subprocess

files_to_run = ['step1.py','step2.py','step3.py']
for file in files_to_run:
    subprocess.run(['python', file])