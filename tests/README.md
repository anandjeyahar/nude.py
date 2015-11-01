#trial.py#
This script tests the true positive and false positive numbers based on some trained sets you give it. Within the samples directory there is a nude and not_nude directory. Put your jpgs in the correct folder and run trial.py.

Add the `-r` option if you want the pictures to be resized before being tested.

==============
Some results  after using random uniform sampling of 50% vs 100%:
==============
At 50%
==============
test6.jpg
examples/images/test6.jpg   False

real    0m2.124s
user    0m2.094s
sys 0m0.033s

===============
At 100%
===============
test6.jpg
examples/images/test6.jpg   False

real    0m2.163s
user    0m2.146s
sys 0m0.019s


