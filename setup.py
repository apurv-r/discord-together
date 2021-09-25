from setuptools import setup

readme = ''
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()


setup(name='discord-together',
      packages = ['discordTogether'],
      author='Apurv R',
      url='https://github.com/apurv-r/discord-together',
      project_urls={
        "Issue tracker": "https://github.com/apurv-r/discord-together/issues",
      },
      download_url="https://github.com/apurv-r/discord-together/archive/refs/tags/1.1.2.tar.gz",
      version='1.1.2',
      license='MIT',
      description='Utilize the BETA Discord VC Party Games feature!',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=[
        "discord.py>=1.5",
      ],
      keywords = ['discord.py','discord together','youtube together','voice activities','discord activities','discord games'],
      python_requires='>=3.6.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ],
)
