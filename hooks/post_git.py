import os
import subprocess

# Create and initialize repository
subprocess.Popen(['git', 'init'])
subprocess.Popen(['git', 'commit', '-a'])

# Create and clean docs branch
subprocess.Popen(['git', 'checkout', '-b', 'docs'])
dir = '.'
for entry in os.listdir(dir):
    if entry != '.github':
        os.remove(os.path.join(dir, entry))
subprocess.Popen(['git', 'commit', '-a'])

# Checkout back to the main branch
subprocess.Popen(['git', 'checkout', '-b', 'main'])
