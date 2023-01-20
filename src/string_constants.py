import os
import pathlib

### categories ###
# -------------- #

# root - in - data
# root - out - data (histograms)
# root - out - figures (histograms)

# *********************************************************** #
#                           IN/OUT DATA                       #
# *********************************************************** #

# root - in - data(polynomials cut outputs with 'sel' columns per quantile)
# => directory structure: qr_run_x/env_run_Y/poly_run_Z
qr_results_in_data_basedir = '/eos/user/k/kiwoznia/data/QR_results/events'

def get_qr_results_in_data_dir(params):
    data_dir = os.path.join(qr_results_in_data_basedir,'qr_run_'+str(int(params.qr_run_n)),'env_run_'+str(int(params.env_run_n)),'poly_run_'+str(int(params.poly_run_n)))
    return data_dir

# output directory for root histograms constructed from event selection values

results_data_basedir = 'results/hist'
# => directory structure: qr_run_x/env_run_Y/poly_run_Z
def get_sel_histograms_out_data_dir(params):
	data_dir = os.path.join(results_data_basedir, 'qr_run_'+str(int(params.qr_run_n)), 'env_run_'+str(int(params.env_run_n)), 'poly_run_'+str(int(params.poly_run_n)))
	pathlib.Path(data_dir).mkdir(parents=True, exist_ok=True)
	return data_dir

# *********************************************************** #
#                           OUT FIGURES                       #
# *********************************************************** #

results_fig_basedir = 'results/fig'

# => directory structure: qr_run_x/env_run_Y/poly_run_Z
def get_sel_histograms_out_fig_dir(params):
	results_selection_hists_subsir = 'quantile_sel_hists'
	data_dir = os.path.join(results_fig_basedir,'qr_run_'+str(int(params.qr_run_n)),'env_run_'+str(int(params.env_run_n)),'poly_run_'+str(int(params.poly_run_n)), results_selection_hists_subsir)
	pathlib.Path(data_dir).mkdir(parents=True, exist_ok=True)
	return data_dir

def get_stats_test_fig_dir(params):
	results_stats_test_subdir = 'stats_tests'
	data_dir = os.path.join(results_fig_basedir,'qr_run_'+str(int(params.qr_run_n)),'env_run_'+str(int(params.env_run_n)),'poly_run_'+str(int(params.poly_run_n)), results_stats_test_subdir)
	pathlib.Path(data_dir).mkdir(parents=True, exist_ok=True)
	return data_dir


# *********************************************************** #
#                  EVENT SAMPLE NUMBERS                       #
# *********************************************************** #

gen_events_number_dir = {
	
	'qcdSide' : 134366091,
	'qcdSig' : 199435365,
	'qcdSideExt' : 90490645,
	'qcdSigExt' : 134264102,
	'GtoWW15na' : 979422,
	'GtoWW15br' : 978558,
	'GtoWW25na' : 983609,
	'GtoWW25br' : 982588,
	'GtoWW35na' : 982038,
	'GtoWW35br' : 972050,
	'GtoWW45na' : 976979,
	'GtoWW45br' : 969741,
	'AtoHZ15' : 99935,
	'AtoHZ25' : 99977,
	'AtoHZ35' : 99979,
	'AtoHZ45' : 99954,
}

gen_events_number_dir['qcdAll'] = gen_events_number_dir['qcdSide']+gen_events_number_dir['qcdSig']+gen_events_number_dir['qcdSideExt']+gen_events_number_dir['qcdSigExt']
