from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np
import sys

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

extra_compile_args = ['-Wno-cpp', '-Wno-unused-function', '-std=c99']
if sys.platform == 'win32':
    extra_compile_args = []

ext_modules = [
    Extension(
        'coco_analyze._mask',
        sources=['./coco_analyze/headers/maskApi.c', 'coco_analyze/_mask.pyx'],
        include_dirs = [np.get_include(), './coco_analyze/headers'],
        extra_compile_args=extra_compile_args,
    )
]

setup(name='coco_analyze',
      packages=['coco_analyze'],
      package_dir = {'coco_analyze': 'coco_analyze'},
      version='2.0',
      ext_modules=
          cythonize(ext_modules)
      )
