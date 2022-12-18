# Sum Of Squares

A simple Python (and soon, C++) script to calculate the values which, when squared, sum up to your desired number.

For example, if your number is 10 the results are `(1, 1, 2, 2)` and `(1, 3)` because `1^2 + 1^2 + 2^2 + 2^2 = 10` and `1^2 + 3^3 = 10`.

## Usage

Make sure you have Python3.

You can run this with

```shell
./sqrsum.py number
```

where `number` is the number you want to find the square sum for (in the example above, this would be `10`).

The full usage instructions are shown below, and can be found by running `./sqrsum.py --help`.

```
usage: minsum [-h] [-d MAX_DEPTH] [--only-smallest] [--verify] number

Calculate the sets of numbers which, when squared and summed, equal the desired number.

positional arguments:
  number

optional arguments:
  -h, --help            show this help message and exit
  -d MAX_DEPTH, --max-depth MAX_DEPTH
  --only-smallest
  --verify
```

### Optional Arguments

- `--max-depth MAX_DEPTH`: Set the maximum depth of the results. In the example above, if you had `--max-depth 2` or `3` you would only get `(1, 3)` as the result because the other result is too long.
- `--only-smallest`: Only return the smallest result(s). In the example above, this would return only `(1, 3)` because it had the smallest length. If there are multiple of the same length, they will all be returned.
- `--verify`: Print out information to confirm that the results are correct.
