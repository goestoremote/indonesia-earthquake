@echo off
redir dist /s /q
py -m build
py -m twine upload --repository pypi dist/*