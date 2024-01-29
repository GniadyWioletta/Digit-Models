import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

def draw_ellipse(position, covariance, ax=None, **kwargs):
    """Draw an ellipse with a given position and covariance"""
    ax = ax or plt.gca()

    # Convert covariance to principal axes
    if covariance.shape == (2, 2):
        U, s, Vt = np.linalg.svd(covariance)
        angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
        width, height = 2 * np.sqrt(s)
    else:
        angle = 0
        width, height = 2 * np.sqrt(covariance)

    # Draw the Ellipse
    for nsig in range(1, 4):
        ax.add_patch(Ellipse(position, nsig * width, nsig * height,
                             angle, **kwargs))


def plot_gmm(gmm, X, Y, All_coefs, label=True, ax=None):
    ax = ax or plt.gca()
    labels = gmm.fit(All_coefs).predict(All_coefs)
    if label:
        ax.scatter(X, Y, c=labels, s=40, cmap='viridis', zorder=2)
    else:
        ax.scatter(X, Y, s=40, zorder=2)

    plt.subplots_adjust(hspace=0.5)

    w_factor = 0.2 / gmm.weights_.max()
    for pos, covar, w in zip(gmm.means_, gmm.covars_, gmm.weights_):
        draw_ellipse(pos, covar, alpha=w * w_factor)

