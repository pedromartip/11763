import math

import numpy as np
from matplotlib import pyplot as plt

from utils import str_quaternion, str_floats


def multiply_quaternions(
        q1: tuple[float, float, float, float],
        q2: tuple[float, float, float, float]
        ) -> tuple[float, float, float, float]:
    """ Multiply two quaternions, expressed as (1, i, j, k). """
    # Your code here:
    #   ...
    return (
        q1[0] * q2[0] - q1[1] * q2[1] - q1[2] * q2[2] - q1[3] * q2[3],
        q1[0] * q2[1] + q1[1] * q2[0] + q1[2] * q2[3] - q1[3] * q2[2],
        q1[0] * q2[2] - q1[1] * q2[3] + q1[2] * q2[0] + q1[3] * q2[1],
        q1[0] * q2[3] + q1[1] * q2[2] - q1[2] * q2[1] + q1[3] * q2[0]
    )


def conjugate_quaternion(
        q: tuple[float, float, float, float]
        ) -> tuple[float, float, float, float]:
    """ Multiply two quaternions, expressed as (1, i, j, k). """
    # Your code here:
    #   ...
    return (
        q[0], -q[1], -q[2], -q[3]
    )


def translation(
        point: tuple[float, float, float],
        translation_vector: tuple[float, float, float]
        ) -> tuple[float, float, float]:
    """ Perform translation of `point` by `translation_vector`. """
    x, y, z = point
    v1, v2, v3 = translation_vector
    # Your code here
    # ...
    return (x+v1, y+v2, z+v3)

def axial_rotation(
        point: tuple[float, float, float],
        angle_in_rads: float,
        axis_of_rotation: tuple[float, float, float]) -> tuple[float, float, float]:
    """ Perform axial rotation of `point` around `axis_of_rotation` by `angle_in_rads`. """
    x, y, z = point
    v1, v2, v3 = axis_of_rotation
    # Normalize axis of rotation to avoid restrictions on optimizer
    v_norm = math.sqrt(sum([coord ** 2 for coord in [v1, v2, v3]]))
    v1, v2, v3 = v1 / v_norm, v2 / v_norm, v3 / v_norm
    # Your code here:
    #   ...
    #   Quaternion associated to point.
    p = (0, x, y, z)
    #   Quaternion associated to axial rotation.
    cos, sin = math.cos(angle_in_rads / 2), math.sin(angle_in_rads / 2)
    q = (cos, sin * v1, sin * v2, sin * v3)
    #   Quaternion associated to image point
    q_star = conjugate_quaternion(q)
    p_prime = multiply_quaternions(q, multiply_quaternions(p, q_star))
    #   Interpret as 3D point (i.e. drop first coordinate)
    return p_prime[1], p_prime[2], p_prime[3]


if __name__ == '__main__':
    # Multiply quaternions
    q1 = (1, 2, 3, 4)
    q2 = (5, 6, 7, 8)
    print(f'Multiplying quaternions ({str_quaternion(q1)}) * ({str_quaternion(q2)}):')
    print(f'  >> Result: {str_quaternion(multiply_quaternions(q1, q2))}.')
    print(f'  >> Expected: -60 + 12i + 30j + 24k.')

    # Conjugate quaternion
    print(f'Conjugate quaternion {str_quaternion(q1)}:')
    print(f'  >> Result: {str_quaternion(conjugate_quaternion(q1))}.')
    print(f'  >> Expected: 1 + -2i + -3j + -4k.')

    # Translation
    point = (4, 5, 6)
    translation_vector = (0, 1, -2)
    print(f'Translation of {point} along vector {translation_vector}:')
    print(f'  >> Result: {str_floats(translation(point, translation_vector))}.')
    print(f'  >> Expected: (4.00, 6.00, 4.00).')

    # Axial rotation
    point = (5, 5, 5)
    axis_of_rotation = (1, 0, 0)
    alpha_rads = math.radians(45)
    print(f'Axial rotation of {point}, {alpha_rads:0.02f} rads around axis {axis_of_rotation}:')
    print(f'  >> Result: {str_floats(axial_rotation(point, alpha_rads, axis_of_rotation))}.')
    print(f'  >> Expected: (5.00, 0.00, 7.07).')

    # Visualization of translation and axial rotation
    translation_vector = (0, 1, 0)
    alpha_degrees = 90
    alpha_rads = math.radians(alpha_degrees)
    axis_of_rotation = (1, 0, -1)
    points = np.stack([np.linspace(-2, 2, 100), np.linspace(0, 1, 100)**2, np.linspace(0, 1, 100)**3], axis=-1)
    colors = np.stack([np.linspace(0, 1, 100), np.zeros(100), np.linspace(1, 0, 100)], axis=-1)
    translated_points = np.stack([translation(point, translation_vector) for point in points], axis=0)
    rotated_points = np.stack([axial_rotation(point, alpha_rads, axis_of_rotation) for point in points], axis=0)
    translated_and_rotated_points = np.stack([axial_rotation(translation(point, translation_vector), alpha_rads, axis_of_rotation) for point in points], axis=0)
    fig = plt.figure()
    axs = np.asarray([
        [fig.add_subplot(221, projection='3d'), fig.add_subplot(222, projection='3d')],
        [fig.add_subplot(223, projection='3d'), fig.add_subplot(224, projection='3d')]
    ])
    axs[0, 0].scatter(points[..., 0], points[..., 1], points[..., 2], c=colors)
    axs[0, 0].set_title('Original points')
    axs[0, 1].scatter(translated_points[..., 0], translated_points[..., 1], translated_points[..., 2], c=colors)
    axs[0, 1].set_title(f'Translated by {translation_vector}')
    axs[1, 0].scatter(rotated_points[..., 0], rotated_points[..., 1], rotated_points[..., 2], c=colors)
    axs[1, 0].set_title(f'Rotated {alpha_degrees}º around {axis_of_rotation}')
    axs[1, 1].scatter(translated_and_rotated_points[..., 0], translated_and_rotated_points[..., 1], translated_and_rotated_points[..., 2], c=colors)
    axs[1, 1].set_title('Translated then rotated')
    for ax in axs.flatten():
        # Show axis
        v1, v2, v3 = axis_of_rotation
        ax.plot([-2*v1, 2*v1], [-2*v2, 2*v2], [-2*v3, 2*v3], color='black')
        # Uniform axis scaling
        ax.set_xlim3d(-2, 2)
        ax.set_ylim3d(-2, 2)
        ax.set_zlim3d(-2, 2)
    fig.show()
