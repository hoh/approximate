# -*- coding:Utf-8 -*-

# Copyright (c) 2015 "Hugo Herter"
#
# This file is part of Python Approximate.

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup

setup(name='Approximate',
      version='0.1',
      description='Python lib for approximate float comparison',
      author='Hugo Herter',
      author_email='@hugoherter.com',
      url='https://github.com/hoh/approximate',
      py_modules=['approximate'],
      license='AGPLv3',
      keywords="float comparison approximate epsilon difference",
      classifiers=['Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: Apache Software License',
                   'Topic :: Scientific/Engineering :: Mathematics',
                   ],
      )
