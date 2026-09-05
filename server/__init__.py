import os
import site
from pathlib import Path

# Optional task-local dependencies keep this installation out of global Python.
local_packages=Path(os.environ.get('KCL_PYTHON_PACKAGES',str(Path.home()/'Desktop'/'KCL'/'study-runtime'/'python')))
if local_packages.is_dir(): site.addsitedir(str(local_packages))
