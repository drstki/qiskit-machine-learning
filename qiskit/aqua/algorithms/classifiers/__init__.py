# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

""" Classifiers Package """

from .vqc import VQC
from .qsvm import QSVM
from .classical_svm import ClassicalSVM, SVM_Classical

__all__ = [
    'VQC',
    'QSVM',
    'ClassicalSVM',
    'SVM_Classical']
