#!bin/bash
# Install all the dependencies
pip install -r requirements.txt --user || pip3 install -r requirements.txt --user # If user doesn't have pip and only pip3
if python -c 'import pkgutil; exit(not pkgutil.find_loader("tkinter"))'; then
    echo 'tkinter found!'
else
    echo 'Finding a workaround....'
    pip install python3-tk --user || pip3 install python3-tk || pip install python-tk --user # For python 2.7 user, hope no one need this :)
fi

# Execute the Program and wala!
python Simulation.py || python3 Simulation.py
