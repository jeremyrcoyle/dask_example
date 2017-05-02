#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import textwrap

version = "0.2.5"

if __name__ == "__main__":
  setuptools.setup(
      name="dask_utils",
      version=version,
      description="Utilities for dask on EC2",
      author="Jeremy Coyle",
      url="https://github.com/jeremyrcoyle/dask_utils",
      long_description=textwrap.dedent("""\
      Utilities for dask on EC2
      """),
      packages=["dask_utils"],
  )
