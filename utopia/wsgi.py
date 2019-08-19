import os
from run import configure

app, _ = configure(os.environ["UTOPIA_CONFIG_PATH"])
