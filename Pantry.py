__author__ = 'Dorbian'
import pantry
import sys
import os


def get_rundir():
    return os.path.abspath(__file__)[:-10]

# Set the rundir
rundir = get_rundir()
print rundir

# Include paths
sys.path.insert(0, rundir)
sys.path.insert(0, os.path.join(os.path.join(rundir, 'pantry'), 'lib'))

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()