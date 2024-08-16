# -*- coding: utf-8 -*-
import os
import sys

import unittest

import numpy as np

# temporary solution for relative imports in case pyod is not installed
# if suod
# is installed, no need to use the following line
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sel_suod.models.base import sel_SUOD

from pyod.utils.data import generate_data
from pyod.models.lof import LOF
from pyod.models.pca import PCA
from pyod.models.hbos import HBOS
from pyod.models.lscp import LSCP
from sel_suod.models.cost_predictor import build_cost_predictor
import joblib


class TestBASE(unittest.TestCase):
	def setUp(self):
		self.n_train = 1000
		self.n_test = 500
		self.contamination = 0.1
		self.roc_floor = 0.6
		self.random_state = 42
		self.X_train, self.X_test, self.y_train, self.y_test = generate_data(
			n_train=self.n_train, n_test=self.n_test, behaviour='new',
			contamination=self.contamination, random_state=self.random_state)

		self.base_estimators = [
			LOF(n_neighbors=5, contamination=self.contamination)
		]
		self.subspaces = np.array([[1,1],[1,1],[1,1],[1,1]])
		self.model = sel_SUOD(base_estimators=self.base_estimators, subspaces=self.subspaces, 
						  n_jobs=2,
						  rp_flag_global=True, bps_flag=True,
						  contamination=self.contamination,
						  approx_flag_global=False,
						  verbose=True)

	def test_initialization(self):
		self.model.get_params()
		self.model.set_params(**{'n_jobs': 4})

	def test_fit(self):
		"""
		Test base class initialization

		:return:
		"""
		self.model.fit(self.X_train)

	def test_approximate(self):
		self.model.fit(self.X_train)
		self.model.approximate(self.X_train)

	def test_predict(self):
		self.model.fit(self.X_train)
		self.model.approximate(self.X_train)
		self.model.predict(self.X_test)

	def test_decision_function(self):
		self.model.fit(self.X_train)
		self.model.approximate(self.X_train)
		self.model.decision_function(self.X_test)

	def test_predict_proba(self):
		self.model.fit(self.X_train)
		self.model.approximate(self.X_train)
		self.model.predict_proba(self.X_test)
