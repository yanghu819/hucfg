####### rm -rf copy-*; 
base_dir="/sunrui/torus/hucfg" ## generate the params & copy the exp folders
python run0.py
cd ${base_dir}/copy-exp##0,1; python main.py;
cd ${base_dir}/copy-exp##0,2; python main.py;
