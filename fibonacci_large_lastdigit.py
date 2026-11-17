import sys


def matrix_multiply(
    A: tuple[tuple[int, int], tuple[int, int]],
    B: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Multiplies two 2x2 matrices A and B."""
    return (
        (A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
        (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]),
    )


def matrix_power(
    matrix: tuple[tuple[int, int], tuple[int, int]], n: int
) -> tuple[tuple[int, int], tuple[int, int]]:
    """Raises the matrix to the power of n using exponentiation by squaring."""
    result = ((1, 0), (0, 1))  # Identity matrix
    base = matrix
    while n:
        if n % 2 == 1:
            result = matrix_multiply(base, result)
        base = matrix_multiply(base, base)
        n //= 2
    return result


def fibonacci_matrixexp(n: int) -> int:
    """Returns the nth Fibonacci number using matrix exponentiation."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    base_matrix = ((1, 1), (1, 0))
    result_matrix = matrix_power(base_matrix, n)
    return result_matrix[0][1]




if __name__ == "__main__":
    n = int(
        input()
    )
    result = fibonacci_matrixexp(n)
    sys.set_int_max_str_digits(1000000)
    result = str(result)[-1]  # Get the last digit of the Fibonacci number
    print(result)
