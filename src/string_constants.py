import os
import pathlib

### categories ###
# -------------- #

# root - in - data
# root - out - histograms
# root - out - figures (histograms)

# *********************************************************** #
#                           IN/OUT DATA                       #
# *********************************************************** #

# root - in - data(polynomials cut outputs with 'sel' columns per quantile)
# => directory structure: qr_run_x/env_run_Y/poly_run_Z
root_in_data_basedir = '/eos/user/k/kiwoznia/data/QR_results/events'

def get_root_in_data_dir(params):
    data_dir = os.path.join(root_in_data_basedir,'qr_run_'+str(int(params.qr_run_n)),'env_run_'+str(int(params.env_run_n)),'poly_run_'+str(int(params.poly_run_n)))
    return data_dir

# output directory for root histograms constructed from event selection values

root_out_hist_basedir = 'results/hist'
# => directory structure: qr_run_x/env_run_Y/poly_run_Z
def get_root_out_hist_dir(params):
	data_dir = os.path.join(root_out_hist_basedir,'qr_run_'+str(int(params.qr_run_n)),'env_run_'+str(int(params.env_run_n)),'poly_run_'+str(int(params.poly_run_n)))
	pathlib.Path(data_dir).mkdir(parents=True, exist_ok=True)
	return data_dir

# *********************************************************** #
#                           OUT FIGURES                       #
# *********************************************************** #


