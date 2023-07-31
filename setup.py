from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
    install_requires=[
    ],
    author='viktor',
    author_email='viktor.email@example.com',
    description='A package to sort and clean folders by file type',
    url='https://github.com/viktor/clean_folder',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
