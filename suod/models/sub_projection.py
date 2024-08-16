import numpy as np
from sklearn.utils import check_array
import math


def sub_transform(X, subspace):
    """Use the given subspace to project the data. Follows the original structure of SUOD

    Parameters
    ----------
    X : numpy array of shape (n_samples, n_features)
        The input samples.

    subspace : numpy array of shape (n_samples)
        The subspace to project X

    Returns
    -------
    X_transformed : numpy array of shape (n_samples, np.trim_zeros(subspace).shape[0])
    """
    X = check_array(X)

    # no need for transformation
    if np.array_equal(subspace, np.ones([X.shape[1]])):
        return X

    if X.shape[1] != subspace.shape[0]:
        ValueError("The data and the subspace have different dimensions.")
    return X[:,subspace]