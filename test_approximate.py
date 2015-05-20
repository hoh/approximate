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

from approximate import ApproximateFloat, epsilon


def test_epsilon():
    assert epsilon > 0


def test_eq():
    assert ApproximateFloat(0.125) == 0.125

    a = ApproximateFloat(10/9.)
    b = 10/9. + 0.0000001
    assert a == b


def test_ne():
    assert ApproximateFloat(0.125) != 0.500

    a = ApproximateFloat(10/9.)
    b = 10/9. + 0.00001
    assert a != b


def test_ge():
    assert ApproximateFloat(0.500) >= 0.125

    a = ApproximateFloat(10/9.)
    b = 10/9. + 0.0000001
    assert a >= b

    a = ApproximateFloat(10/9.)
    b = 10/9. + (epsilon * 10.)
    assert not(a >= b)


def test_le():
    assert ApproximateFloat(0.125) <= 0.500

    a = ApproximateFloat(10/9.)
    b = 10/9. - 0.0000001
    assert a <= b

    a = ApproximateFloat(10/9.)
    b = 10/9. - 0.00001
    assert not(a <= b)
