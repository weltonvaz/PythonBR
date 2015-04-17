from timeit import timeit

import numpy as np
import numpy.random as npr

sz = (2048)
a32 = npr.randint(1, 5001, sz).astype(np.int32)
b32 = npr.randint(1, 5001, sz).astype(np.int32)
a64 = a32.astype(np.int64)
b64 = b32.astype(np.int64)

print ('Mul32', timeit('d = a32 * b32', 'from __main__ import a32, b32'))
print ('Div32', timeit('d = a32 / b32', 'from __main__ import a32, b32'))
print ('Mul64', timeit('d = a64 * b64', 'from __main__ import a64, b64'))
print ('Div64', timeit('d = a64 / b64', 'from __main__ import a64, b64'))
