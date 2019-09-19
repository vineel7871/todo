from setuptools import setup

setup(
    name="todo",
    py_modules="main",
    install_requires=['click'],
    entry_points="""
        [console_scripts]
        todo=main:grp
    """
)
