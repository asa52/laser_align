#!/usr/bin/env python

"""Contains base-level functions that are required for the others to run."""

import numpy as np


def verify_vector(vector):
    """Checks the input vector has 3 components."""
    r = np.array(vector)
    assert r.shape == (3,), "The variable 'vector' must have 3 components."
    return r


def unchanged(arg):
    """Returns the single input argument; the default function for image
    post-processing to return the input array unchanged."""
    return arg


def bake(fun, args=None, kwargs=None, position_to_pass_through=0):
    """Returns an object given by the function 'fun' with its arguments,
    known as a curried function or closure. These objects can be passed into
    other functions to be evaluated.

    :param fun: The function object without any arguments specified.
    :param args: A list of the positional arguments.
    :param kwargs: A list of keyword arguments.
    :param position_to_pass_through: See docstring for 'wrapped'.
    :return: The object containing the function with its arguments."""

    if args is None:
        args = []
    if kwargs is None:
        kwargs = {}

    def wrapped(image):
        """Parameter position_to_pass_through specifies the index of the
        parameter 'image' in the sequence of positional arguments for 'fun'."""
        return fun(*(args[:position_to_pass_through] + [image] + args[(
            position_to_pass_through+1):]), **kwargs)

    return wrapped


def positions_maker(x=np.array([0]), y=np.array([0]), z=np.array([0]),
                    initial_pos=np.array([0, 0, 0])):
    """Generator to produce N x 3 array of all possible permutations of 1D
    arrays x and y, such that N = len(x) * len(y). For example x = [1,2] and
    y = [3,4] yields [1, 3, 0], [1, 4, 0], [2, 3, 0], [2, 4, 0] respectively.
    This is added to [0, 0, 0] before being output."""
    i = 0
    while i < x .size:
        j = 0
        while j < y.size:
            k = 0
            while k < z.size:
                yield np.array([x[i], y[j], z[k]]) + initial_pos
                k += 1
            j += 1
        i += 1


def sub_dict(main_dict, subset_keys=None, extra_entries=None):
    """Slice specific keys of a dictionary, add extra entries if specified,
    and return the new dictionary.
    :param main_dict: The main dictionary to slice.
    :param subset_keys: The list of keys in main_dict to use. If None,
    all keys are used.
    :param extra_entries: A dictionary of extra entries to add to slice
    dictionary."""
    subset_dict = {}
    if subset_keys is not None:
        for key in subset_keys:
            subset_dict[key] = main_dict[key]
    elif subset_keys is None:
        subset_dict = main_dict
    else:
        raise ValueError('subset_keys is invalid.')

    if extra_entries is not None:
        for key in extra_entries:
            subset_dict[key] = extra_entries[key]

    return subset_dict
