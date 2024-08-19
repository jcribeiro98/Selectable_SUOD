
*Fork of*: SUOD: Accelerating Large-scare Unsupervised Heterogeneous Outlier Detection
===========================================================================

---
### *NEW*: Now available in PyPi! 

```
pip install sel-suod
```
---

Please refer to the [original package](https://github.com/yzhao062/SUOD) for more information about the base functionalities.
This fork forces SUOD to use pre-selected axis-parallel subspaces, such as those obtained after Feature Bagging or Feature Selection. These subspaces must be declared as a `np.array`, and can take any structure such that the operation `X[:, subspace]` yields the desired projected dataset. 
It uses the same class declaration as base SUOD, only adding a new variable: `subspaces`, and changing the class name to sel_SUOD.
This fork additionally contains a number of QOL additions, like:

   - During initialization, if base_estimators is an array of length 1, it will sklearn.clone() the estimator once per each subspace.
   - During initialization, it will automatically check whether the number of detectors and estimators coincide. 
   - It will, by default, not run approximation on any method unless the global flag for approximation is manually turned to true.

There should be no conflict between SUOD and sel_SUOD.
Take a look at the following code for a practical example: 

```
base_estimators = [LOF()] #The class sel_SUOD automatically initizializes itself with subspaces.shape[0] clones of this array if len < 2.

#Creating exemplary subspaces
subspaces = [True]*20
subspaces.append(False)
subspaces = np.array([subspaces, subspaces])
subspaces[1][4] = False

model = sel_SUOD(base_estimators=base_estimators, subspaces=subspaces,
                 n_jobs=6, bps_flag=True,
                 contamination=contamination, approx_flag_global=True)
model.fit(X_train)  # fit all models with X
predicted_scores = model.decision_function(X_test)  # predict scores
```
