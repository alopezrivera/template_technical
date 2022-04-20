import os

################
# Replacements #
################
replace = lambda string, replacement: os.system(f"find . \( ! -regex '.*/\..*' \) -type f | xargs sed -i 's/{string}/{replacement}/g'")

replace('~REPLACE-BY-CODENAME~',     '{{cookiecutter.codename}}')
replace('~REPLACE-BY-PROJECT-NAME~', '{{cookiecutter.project}}')

##############
# Repository #
##############

# Create and initialize repository
os.system('git init')
os.system('git add -A')
os.system('git commit -m "Repository initialized"')

# Create and clean docs branch
os.system('git checkout -b docs')
os.system('git rm -r .')
os.system('git add -A')
os.system('git commit -m "Docs branch created, cleaned up"')

# Checkout back to the main branch
os.system('git checkout master')
