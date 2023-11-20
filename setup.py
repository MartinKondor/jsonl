from setuptools import setup, find_packages


setup(
    name='jsonl',
    version='1.0',
    py_modules=['jsonl'],
    entry_points={
        'console_scripts': [
            'jsonl_script=jsonl:main',
        ],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
