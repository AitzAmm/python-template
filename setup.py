from setuptools import setup, find_packages

setup(
    name='mytool',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Description of your tool',
    long_description='Long description of your tool',
    url='https://github.com/AitzAmm/mytool',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mytool = src.mytool:main',
        ],
    },
)
