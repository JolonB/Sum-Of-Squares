#!/usr/bin/python3

import argparse
import copy
import math

previously_computed = {}


def compute(num, remaining_depth):
    # Stop iterating if we've gone too deep
    if remaining_depth == 0:
        return None
    # Return 1 if the num is 1
    if num == 1:
        return [[1]]
    # Anything less than 4 will have a int(sqrt(x)) of 1, so cannot be broken down further
    if num < 4:
        return None

    # Get the root of the number
    unrounded_sqrt_of_num = math.sqrt(num)
    max_sqrt_of_num = int(unrounded_sqrt_of_num)

    # If num is a square number, return the root
    if max_sqrt_of_num == unrounded_sqrt_of_num:
        return [[max_sqrt_of_num]]

    # Use memoized result, if available
    if num in previously_computed:
        previous_result = previously_computed[num]
        # If the depth would be too high, skip it
        if remaining_depth > 0 and len(previous_result) >= remaining_depth - 1:
            return None
        return copy.deepcopy(previous_result)

    results = []
    # Don't go below half otherwise we will get duplicates
    for sqrt_of_summand in reversed(range(max_sqrt_of_num // 2, max_sqrt_of_num)):
        summand = sqrt_of_summand * sqrt_of_summand
        difference = num - summand
        square_roots_of_summands = compute(difference, remaining_depth - 1)
        if not square_roots_of_summands:
            continue

        # print(square_roots_of_summands)
        for root in square_roots_of_summands:
            root.append(sqrt_of_summand)
            root.sort()
            if root not in results:
                results.append(root)

    previously_computed[num] = results
    return copy.deepcopy(results)


def main(num, max_depth=-1, only_smallest=False, verify=False):
    results = compute(num, max_depth)

    if only_smallest:
        min_results = []
        min_length = float("inf")
        for result in results:
            result_len = len(result)
            if result_len < min_length:
                min_length = result_len
                min_results = []
            if result_len == min_length:
                min_results.append(result)
        results = min_results

    if verify:
        for result in results:
            squared_values = [value**2 for value in result]
            summation = "+".join(str(value) for value in squared_values)
            summed_values = sum(squared_values)
            if summed_values != num:
                print("ERROR --> ", end="")
            print("{} -> {} = {}".format(result, summation, summed_values))

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="minsum",
        description="Calculate the sets of numbers which, when squared and summed, equal the desired number.",
    )

    parser.add_argument("number", type=int)
    parser.add_argument("-d", "--max-depth", default=-1, type=int)
    parser.add_argument("--only-smallest", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    print(
        main(
            args.number,
            max_depth=args.max_depth,
            only_smallest=args.only_smallest,
            verify=args.verify,
        )
    )
