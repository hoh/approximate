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

"""
Use ApproximateFloat to compare float variables with slightly
different values.
"""

# Default value for the allowed difference is one over a million
epsilon = 0.000001


class ApproximateFloat(float):
    """Extension of 'float' with comparison operators that handle approximate
    values.
    """
    def __eq__(self, other):
        return abs(self.real - other) < epsilon

    def __ne__(self, other):
        return not self.__eq__(other)

    def __ge__(self, other):
        return self.real + epsilon > other

    def __le__(self, other):
        return self.real - epsilon < other
