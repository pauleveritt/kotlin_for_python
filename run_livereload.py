from livereload import Server, shell

sphinx = ".venv/bin/python3 .venv/bin/sphinx-build -E -b html docs docs/_build"

if __name__ == '__main__':
    server = Server()
    server.watch('docs/conf.py', shell(sphinx))
    server.watch('docs/*.rst', shell(sphinx))
    server.watch('docs/*/*.rst', shell(sphinx))
    server.serve(root='docs/_build', live_css=False)
