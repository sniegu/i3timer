from setuptools import setup

## afdg

setup(
    name='i3timer',
    version='0.1',
    packages=['i3timer'],
    entry_points = {
        'console_scripts': [
            'i3timer = i3timer.cli:run',
        ],
    },
    zip_safe=True,
)
