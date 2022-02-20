import tempfile
import venv
import subprocess
import sys

if __name__ == "__main__":

    with tempfile.TemporaryDirectory() as tmpdirname:
        venv.create(tmpdirname, with_pip=True)
        pip_args = [tmpdirname + "/bin/pip", "--disable-pip-version-check", 
                "install", "pyfiglet"]
        subprocess.run(pip_args, stdout=subprocess.DEVNULL) 
        python_args = [tmpdirname + "/bin/python3", "-m", "figdate"] + sys.argv[1:]
        subprocess.run(python_args)
