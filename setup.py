from setuptools import setup


setup(
    name="screen_capture",
    version="0.1",
    py_modules=["screen_capture"],
    install_requires=[
        "Click",
        "selenium"
    ],
    entry_points="""
        [console_scripts]
        screen=screen_capture:cli
    """
)