#!/usr/bin/python

import sys
import subprocess
from distutils.util import convert_path
from distutils.core import setup
from distutils.extension import Extension
from distutils.sysconfig import get_python_inc, get_config_var
import os.path
import numpy


include_dirs = []
cflags=[]
ldflags=[]
define_macros=[]
cmd_class = {}
cmd_options = {}


# If numpy include file isn't in the standard Python include path, 
# add it manually.
if not os.path.exists(os.path.join(get_python_inc(), "numpy", "arrayobject.h")):
    include_dirs += [numpy.get_include()]


################################################################################

ext_modules = []

_trep = Extension('trep._trep',
                  include_dirs=include_dirs,
                  define_macros=define_macros,
                  extra_compile_args=cflags,
                  extra_link_args=ldflags,
                  sources = [
                      'src/_trep/midpointvi.c',
                      'src/_trep/system.c',
                      'src/_trep/math-code.c',
                      'src/_trep/frame.c',
                      'src/_trep/_trep.c',
                      'src/_trep/config.c',
                      'src/_trep/potential.c',
                      'src/_trep/force.c',
                      'src/_trep/input.c',
                      'src/_trep/constraint.c',
                      'src/_trep/frametransform.c',
                      'src/_trep/spline.c',
                      'src/_trep/tapemeasure.c',
                      
                      # Constraints
                      'src/_trep/constraints/distance.c',
                      'src/_trep/constraints/point.c',
                      
                      # Potentials
                      'src/_trep/potentials/gravity.c',
                      'src/_trep/potentials/linearspring.c',
                      'src/_trep/potentials/configspring.c',
                      'src/_trep/potentials/nonlinear_config_spring.c',
                      
                      # Forces
                      'src/_trep/forces/damping.c',
                      'src/_trep/forces/configforce.c',
                      'src/_trep/forces/bodywrench.c',
                      'src/_trep/forces/hybridwrench.c', 
                      'src/_trep/forces/spatialwrench.c',
                      'src/_trep/forces/pistonexample.c',
                      ],
                  depends=[
                      'src/_trep/trep.h',
                      'src/_trep/c_api.h'
                      ])

ext_modules += [_trep]

_polyobject = Extension('trep.visual._polyobject',
                        extra_compile_args=[],
                        extra_link_args=['-lGL'],
                        sources = ['src/visual/_polyobject.c'])
ext_modules += [_polyobject]


setup (name = 'trep',
       version = '0.93.1',
       description = 'trep is used to simulate mechanical systems.',
       long_description="Trep is a Python module for modeling articulated rigid body mechanical systems in \
generalized coordinates. Trep supports basic simulation but it is primarily designed to serve as a \
calculation engine for analysis and optimal control algorithms that require 1st and 2nd derivatives \
of the system's dynamics.",
       author = 'Elliot Johnson',
       author_email = 'elliot.r.johnson@gmail.com',
       url = 'http://nxr.northwestern.edu/trep',
       license='GPLv3',
       platforms='Linux, Mac, Windows',
       package_dir = {'' : 'src', 'trep': 'src'},
       packages=['trep',
                 'trep.constraints',
                 'trep.potentials',
                 'trep.forces',
                 'trep.visual',
                 'trep.puppets',
                 'trep.discopt',
                 'trep.ros'
                 ],
       package_data={
           'trep.visual' : ['icons/*.svg']
           },
       ext_modules=ext_modules,
       cmdclass=cmd_class,
       command_options=cmd_options,
       install_requires=[
           'numpy',
           'scipy',
       ],
       headers=[
           'src/_trep/trep.h',
           'src/_trep/c_api.h'
           ])
