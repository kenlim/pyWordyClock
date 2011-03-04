from setuptools import setup, find_packages;

setup(
    name = 'PyWordyClock',
    version = '0.1',

    packages = find_packages('src'),
    package_dir = {'':'src'},

    entry_points = {
        'console_scripts' : [
            'pyWordyClock = pyWordyClock.WordyClock:main',
            'pyWordyClockFace = pyWordyClock.WordyClock:otherMain'
        ]
    }
)