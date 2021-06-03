from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Utilize Discord party games with discord.py!'

# Setting up
setup(
    name="discord-together",
    version=VERSION,
    author="Apurv Rane",
    author_email="apurv.r11@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['discord python', 'discord.py', 'discord activities', 'party games', 'youtube together', 'discord together', 'discord party games', 'discord poker'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)