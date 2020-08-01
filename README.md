# Average cubic weight of air conditioners

This is a python 3.7 script.

## Setup
Install required packages by running 
`pip install -r requirements.txt`


## Run 
The main entry point is ./main.py in the root directory.
To run the program, execute:
`python main.py`


## Test
You can run the tests by running `python -m unittest`


## NOTE
For the sake of code clarity, we're fetching all the products first
into memory and then calculating the cubic weights. If needed, 
we can reduce the memory footprint by calculating the cubic weights
as the products are being fetch.

## TODO
The test for products uses `assertEqual()` for `float`s. This should be changed to `assertAlmostEqual()`
with a reasonable tolerance.
