import os, shutil

# i/o paths
mess_dir = '/home/zhouyj/software/MESS'
data_dir = '/data1/Example_data'
time_range = '20190704-20190707'
sta_file = 'input/example_pal.sta'
temp_root = 'output/Example_templates'
temp_pha = 'input/eg_pal.temp'
out_root = 'output/eg_cpu'
out_ctlg = os.path.join(out_root, 'catalog_{}.dat'.format(time_range))
out_pha = os.path.join(out_root, 'phase_{}.dat'.format(time_range))

# run MESS (gpu ver)
shutil.copyfile('config_eg.py', os.path.join(mess_dir, 'config.py'))
os.system("python {}/run_mess.py \
    --data_dir={}  --time_range={} --sta_file={} \
    --temp_root={} --temp_pha={} \
    --out_ctlg={} --out_pha={}"\
    .format(mess_dir, data_dir, time_range, sta_file, temp_root, temp_pha, out_ctlg, out_pha))
