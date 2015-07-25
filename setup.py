import os
from setuptools import setup
from setuptools import find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)
for dirpath, dirnames, filenames in os.walk('foodtracker'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "admin_tools/" or "admin_tools\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))
            
setup(
    name = "Command line food tracker",
    version = "0.0.7",
    author = "Roko Bobic",
    author_email = "roko.bobic@gmail.com",
    description = ("Command line tool that allows you to easy keep track of food that you are eatingevery day."),
    license = "BSD",
    keywords = "food tracker logger fitness nutrition log proteins carbohydrates fats",
    url = "http://packages.python.org/foodtracker",
    package_dir={'foodtracker': 'foodtracker'},
    packages=packages,
    package_data={'foodtracker': data_files},
    long_description=read('README.md'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)