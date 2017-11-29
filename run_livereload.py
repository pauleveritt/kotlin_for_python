"""

Automatically re-build Sphinx docs while editing, serve docs on an
HTTP port, and also reload any browsers pointed to the docs.

"""

import glob

from livereload import Server, shell
from livereload.watcher import Watcher

sphinx = ".venv/bin/python3 .venv/bin/sphinx-build -E -b html docs docs/_build"


class CustomWatcher(Watcher):
    """ Handle recursive globs with Python 3.5+ globbing  """

    def is_glob_changed(self, path, ignore=None):
        for f in glob.glob(path, recursive=True):
            if self.is_file_changed(f, ignore):
                return True
        return False


server = Server(watcher=CustomWatcher())
server.watch('docs/**', shell(sphinx),
             ignore=lambda s: '_build' in s)
server.watch('src/kaybee/**.py', shell(sphinx))
server.serve(root='docs/_build', live_css=False)
