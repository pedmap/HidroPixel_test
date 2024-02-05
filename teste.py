import numpy as np
lin = 1701
col = 2722
num_pix = lin * col

num_pix_bac = 2527422
num_pix_non_bac = 2102700
num_cabe = 524361
num_non_cabe = 2003061
num_cabe_py = 499736
pix_total_cabe = num_cabe + num_non_cabe
pix_non_pix_py = num_pix_bac - num_cabe_py

erro_f_py = np.abs(num_non_cabe - pix_non_pix_py)
A = False
