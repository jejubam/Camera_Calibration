import numpy as np

def compute_relative_extrinsics(R_wc1, t_wc1, R_wc2, t_wc2):
    """
    Compute the relative rotation (R) and translation (t) between two cameras.
    
    Parameters:
        R_wc1: np.ndarray
            Rotation matrix (3x3) of the first camera (world to camera).
        t_wc1: np.ndarray
            Translation vector (3x1) of the first camera (world to camera).
        R_wc2: np.ndarray
            Rotation matrix (3x3) of the second camera (world to camera).
        t_wc2: np.ndarray
            Translation vector (3x1) of the second camera (world to camera).
    
    Returns:
        R_12: np.ndarray
            Relative rotation matrix (3x3) from camera 1 to camera 2.
        t_12: np.ndarray
            Relative translation vector (3x1) from camera 1 to camera 2.
    """
    # Compute the relative rotation
    R_12 = R_wc2 @ R_wc1.T  # R_c2 * R_c1^T
    
    # Compute the relative translation
    t_12 = t_wc2 - R_12 @ t_wc1  # t_c2 - R_12 * t_c1
    
    return R_12, t_12