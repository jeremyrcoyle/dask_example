#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import textwrap
import versioneer

version = "0.2.5"

if __name__ == "__main__":
  setuptools.setup(
      name="dask_utils",
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description="Utilities for dask on EC2",
      author="Jeremy Coyle",
      url="https://github.com/jeremyrcoyle/dask_utils",
      long_description=textwrap.dedent("""\
      Utilities for dask on EC2
      """),
      packages=["dask_utils"],
      entry_points="""
        [console_scripts]
        dask_utils=dask_utils.cli.main:start
      """,
      install_requires=["click","dask_ec2"]
  )
  
  