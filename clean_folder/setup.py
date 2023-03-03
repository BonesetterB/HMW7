from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    description='Very clean code',
    author='Illy',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:path_1']}
)
