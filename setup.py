from setuptools import setup

readme = ''
with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()


setup(name='discordTogether',
      packages = ['discordTogether'],
      author='Apurv R',
      url='https://github.com/apurv-r/discordTogether',
      project_urls={
        "Issue tracker": "https://github.com/apurv-r/discordTogether/issues",
      },
      download_url="https://github.com/apurv-r/discordTogether/archive/refs/tags/1.0.3.tar.gz",
      version='1.0.3',
      license='MIT',
      description='Utilize the BETA Discord Party Games feature!',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=[
        "requests", 
      ],
      keywords = ['discordpy','discord.py','discord together','discord party games','party games','discord activities','discord','discord ext','discord modules'],
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ],
)
