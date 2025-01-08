import numpy as np

from distort_points import distort_points


def project_points(points_3d: np.ndarray,
                   K: np.ndarray,
                   D: np.ndarray) -> np.ndarray:
    """
    Projects 3d points to the image plane, given the camera matrix,
    and distortion coefficients.

    Args:
        points_3d: 3d points (Nx3)
        K: camera matrix (3x3)
        D: distortion coefficients (4x1)

    Returns:
        projected_points: 2d points (2xN)
    """

    # [TODO] get image coordinates
    x_normalized = points_3d[:, :2] / points_3d[:, 2:3]
    
    ox, oy = K[0, 2], K[1, 2]
    fx, fy = K[0, 0], K[1, 1]
    
    x = np.zeros_like(x_normalized)
    x[:, 0] = fx * x_normalized[:, 0] + ox
    x[:, 1] = fy * x_normalized[:, 1] + oy

    # [TODO] apply distortion
    projected_points = distort_points(x, D, K)

    return projected_points
