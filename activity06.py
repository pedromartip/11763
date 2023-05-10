import math

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import least_squares

import activity05


def translation_then_axialrotation(point: tuple[float, float, float], parameters: tuple[float, ...]):
    """ Apply to `point` a translation followed by an axial rotation, both defined by `parameters`. """
    x, y, z = point
    t1, t2, t3, angle_in_rads, v1, v2, v3 = parameters
    # Normalize axis of rotation to avoid restrictions on optimizer
    v_norm = math.sqrt(sum([coord ** 2 for coord in [v1, v2, v3]]))
    v1, v2, v3 = v1/v_norm, v2/v_norm, v3/v_norm
    # Your code here:
    #   ...


def isometry(point: tuple[float, float, float], parameters: tuple[float, ...]):
    """ Apply to `point` the screw displacement defined by `parameters`. """
    x, y, z = point
    v1, v2, v3, angle_in_rads, displacement = parameters
    # Normalize axis of rotation to avoid restrictions on optimizer
    v_norm = math.sqrt(sum([coord ** 2 for coord in [v1, v2, v3]]))
    v1, v2, v3 = v1/v_norm, v2/v_norm, v3/v_norm
    # Your code here:
    #   ...


def vector_of_residuals(ref_points: np.ndarray, inp_points: np.ndarray) -> np.ndarray:
    """ Given arrays of 3D points with shape (point_idx, 3), compute vector of residuals as their respective distance """
    # Your code here:
    #   ...


def coregister_landmarks(ref_landmarks: np.ndarray, inp_landmarks: np.ndarray):
    """ Coregister two sets of landmarks using a rigid transformation. """
    initial_parameters = [
        0, 0, 0,    # Translation vector
        0,          # Angle in rads
        1, 0, 0,    # Axis of rotation
    ]
    # Find better initial parameters
    centroid_ref = np.mean(ref_landmarks, axis=0)
    centroid_inp = np.mean(inp_landmarks, axis=0)
    # Your code here:
    #   ...

    def function_to_minimize(parameters):
        """ Transform input landmarks, then compare with reference landmarks."""
        # Your code here:
        #   ...


    # Apply least squares optimization
    result = least_squares(
        function_to_minimize,
        x0=initial_parameters,
        verbose=1)
    return result


if __name__ == '__main__':
    # Translation then axial rotation:
    point = (4, 5, 6)
    translation_vector = (0, 1, -2)
    alpha_rads = math.radians(45)
    axis_of_rotation = (1, 0, 0)
    parameters = translation_vector + (alpha_rads,) + axis_of_rotation
    print(f'Starting from {point}, translate along {translation_vector}, then rotate {alpha_rads} rads around {axis_of_rotation}:')
    print(f'  >> Result: {translation_then_axialrotation(point, parameters)}.')
    print(f'  >> Expected: (4, 6, 4).')

    # Isometry:
    point = (4, 5, 6)
    screw_axis = (0, 3/5, -4/5)
    displacement = 2
    alpha_rads = math.radians(45)
    parameters = screw_axis + (alpha_rads, displacement)
    print(f'Starting from {point}, translate {displacement}px along {screw_axis}, then rotate {alpha_rads} rads around same axis:')
    print(f'  >> Result: {isometry(point, parameters)}.')
    print(f'  >> Expected: (4, 6, 4).')

    # Quadratic residues:
    ref_landmarks = np.asarray([(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)])
    inp_landmarks = np.asarray([(0.05, 3.22, 0.94), (0.59, 3.56, 1.71), (0.39, 3.45, 0.37), (-0.52, 3.79, 1.23), (0.16, 4.88, 1.22)])
    print(f'Residual vector of distances between each pair of landmark points (ref vs. input):')
    print(f'  >> Result: {vector_of_residuals(ref_landmarks, inp_landmarks)}.')
    print(f'  >> Expected: (4, 6, 4).')
    
    # Quadratic residues visualization
    fig = plt.figure()
    axs = np.asarray([fig.add_subplot(121, projection='3d'), fig.add_subplot(122, projection='3d')])
    axs[0].scatter(ref_landmarks[..., 0], ref_landmarks[..., 1], ref_landmarks[..., 2], c=ref_landmarks, marker='o')
    axs[0].set_title('Reference landmarks')
    axs[1].scatter(inp_landmarks[..., 0], inp_landmarks[..., 1], inp_landmarks[..., 2], c=ref_landmarks, marker='^')
    axs[1].set_title('Input landmarks')
    # Uniform axis scaling
    all_points = np.concatenate([ref_landmarks, inp_landmarks], axis=0)
    range_x = np.asarray([np.min(all_points[..., 0]), np.max(all_points[..., 0])])
    range_y = np.asarray([np.min(all_points[..., 1]), np.max(all_points[..., 1])])
    range_z = np.asarray([np.min(all_points[..., 2]), np.max(all_points[..., 2])])
    max_midrange = max(range_x[1]-range_x[0], range_y[1]-range_y[0], range_z[1]-range_z[0]) / 2
    for ax in axs.flatten():
        ax.set_xlim3d(range_x[0]/2 + range_x[1]/2 - max_midrange, range_x[0]/2 + range_x[1]/2 + max_midrange)
        ax.set_ylim3d(range_y[0]/2 + range_y[1]/2 - max_midrange, range_y[0]/2 + range_y[1]/2 + max_midrange)
        ax.set_zlim3d(range_z[0]/2 + range_z[1]/2 - max_midrange, range_z[0]/2 + range_z[1]/2 + max_midrange)
    fig.show()

    # Coregister landmarks
    result = coregister_landmarks(ref_landmarks, inp_landmarks)
    solution_found = result.x

    t1, t2, t3, angle_in_rads, v1, v2, v3 = result.x
    print(f'Best parameters:')
    print(f'  >> Translation: ({t1}, {t2}, {t3}).')
    print(f'  >> Rotation: {angle_in_rads} rads around axis ({v1}, {v2}, {v3}).')

    inp_landmarks_transf = np.asarray([translation_then_axialrotation(point, result.x) for point in inp_landmarks])

    # Optimization visualization
    fig = plt.figure()
    fig.suptitle('Reference (circle) and input (triangle) landmarks')
    axs = np.asarray([fig.add_subplot(121, projection='3d'), fig.add_subplot(122, projection='3d')])
    axs[0].scatter(ref_landmarks[..., 0], ref_landmarks[..., 1], ref_landmarks[..., 2], c=ref_landmarks, marker='o')
    axs[0].scatter(inp_landmarks[..., 0], inp_landmarks[..., 1], inp_landmarks[..., 2], c=ref_landmarks, marker='^')
    axs[0].set_title('Before')
    axs[1].scatter(ref_landmarks[..., 0], ref_landmarks[..., 1], ref_landmarks[..., 2], c=ref_landmarks, marker='o')
    axs[1].scatter(inp_landmarks_transf[..., 0], inp_landmarks_transf[..., 1], inp_landmarks_transf[..., 2], c=ref_landmarks, marker='^')
    axs[1].set_title('After')
    # Uniform axis scaling
    all_points = np.concatenate([ref_landmarks, inp_landmarks], axis=0)
    range_x = np.asarray([np.min(all_points[..., 0]), np.max(all_points[..., 0])])
    range_y = np.asarray([np.min(all_points[..., 1]), np.max(all_points[..., 1])])
    range_z = np.asarray([np.min(all_points[..., 2]), np.max(all_points[..., 2])])
    max_midrange = max(range_x[1] - range_x[0], range_y[1] - range_y[0], range_z[1] - range_z[0]) / 2
    for ax in axs.flatten():
        ax.set_xlim3d(range_x[0] / 2 + range_x[1] / 2 - max_midrange, range_x[0] / 2 + range_x[1] / 2 + max_midrange)
        ax.set_ylim3d(range_y[0] / 2 + range_y[1] / 2 - max_midrange, range_y[0] / 2 + range_y[1] / 2 + max_midrange)
        ax.set_zlim3d(range_z[0] / 2 + range_z[1] / 2 - max_midrange, range_z[0] / 2 + range_z[1] / 2 + max_midrange)
    fig.show()
