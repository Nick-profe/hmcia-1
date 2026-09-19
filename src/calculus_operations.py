import numpy as np


# BASIC FUNCTIONS

def linear_function(x):
    return 2*x + 1


def quadratic(x):
    return x**2


# DERIVATIVES

def quadratic_derivative(x):
    return 2*x


def numerical_derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def central_difference(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)


# PARTIAL DERIVATIVES AND GRADIENTS

def function_2d(x, y):
    return x**2 + y**2


def gradient_quadratic(x, y):
    return np.array([
        2*x,
        2*y
    ])


# LOSS FUNCTIONS

def mse_loss(y_true, y_pred):
    return np.mean(
        (y_true - y_pred)**2
    )


# LINEAR REGRESSION GRADIENTS

def linear_regression_gradients(
    x,
    y,
    w,
    b
):

    n = len(x)

    y_pred = w*x + b

    dw = (-2/n) * np.sum(
        x * (y - y_pred)
    )

    db = (-2/n) * np.sum(
        y - y_pred
    )

    return dw, db


# GRADIENT DESCENT

def gradient_descent_step(
    x,
    y,
    w,
    b,
    learning_rate
):

    dw, db = linear_regression_gradients(
        x,
        y,
        w,
        b
    )

    w -= learning_rate * dw
    b -= learning_rate * db

    return w, b