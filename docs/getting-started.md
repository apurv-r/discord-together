# Getting Started

Discord Together is a python package that allows bots to create invite links to Discord's BETA feature, popularly known as VC Party Games or Voice Activities. This feature is only available by default on a small amount of hand picked servers. However, this package allows you to create invite links to such activities in your own servers! This package also has no dependencies other than [`aiohttp`]('https://pypi.org/project/aiohttp/'), meaning it can be used with any fork of discord.py. 

This project is open source, you can find the source code [here]('https://github.com/apurv-r/discord-together').

!!! info
    
    As of the latest release, this BETA feature is only supported on web and updated PC app versions of Discord and is not supported on mobile.

## Installation

### with pip <small>recommended</small> { #with-pip data-toc-label="with pip" }
```
pip install discord-together
```
This will automatically install compatible versions of [`aiohttp`]('https://pypi.org/project/aiohttp/') which is a dependency. If you're using any fork of discord.py, you will already be having this package.
!!! failure "Installation Error"
    If you receive an error like `No matching distribution found for discord-together when installing`, try updating the python version! (It must be 3.6 or higher)

### with git

Discord Together can be directly used from [GitHub]('https://github.com/apurv-r/discord-together') by cloning the
repository into a subfolder of your project root which might be useful if you
want to use the very latest version:

```
git clone https://github.com/apurv-r/discord-together.git
```