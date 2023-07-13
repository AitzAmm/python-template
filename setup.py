from setuptools import setup, find_packages

setup(
    name='mytool',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Description of your tool',
    long_description='Long description of your tool',
    url='https://github.com/yourusername/mytool',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mytool = src.mytool:main',
        ],
    },
    data_files=[
        ('share/man/man6', ['doc/mytool.6']),
    ],
)
