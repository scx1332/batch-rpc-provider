#!/usr/bin/env python

import os
from setuptools import setup
import re
VERSION_FILE = "batch_rpc_provider/_version.py"
ver_str_line = open(VERSION_FILE, "rt").read()
VS_RE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VS_RE, ver_str_line, re.M)
if mo:
    ver_str = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSION_FILE,))

github_version = os.environ.get('GITHUB_RELEASE_VER')
if github_version == "v" + ver_str:
    print("Version in _version.py matches the tag name")
else:
    raise RuntimeError(f"Version in _version.py does not match the tag name (v{ver_str} != {github_version})")

setup(name='batch_rpc_provider',
      version=ver_str,
      # list folders, not files
      packages=['batch_rpc_provider'],
      scripts=['batch_rpc_provider/batch_rpc_provider.py', 'batch_rpc_provider/__init__.py'],
      author='Sieciech Czajka',
      author_email='sieciech.czajka@golem.network',
      url='https://github.com/scx1332/batch-rpc-provider',
      download_url='https://github.com/scx1332/batch-rpc-provider/archive/refs/tags/{github_version}.tar.gz',
      keywords=['MultiCall', 'json-rpc', 'web3'],
      install_requires=[
          'aiohttp',
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Intended Audience :: Developers',  # Define that your audience are developers
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',  # Again, pick a license
          'Programming Language :: Python :: 3.10',
      ],
      )
