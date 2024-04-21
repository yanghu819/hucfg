
## get the hucfg in use
import os, re, json; hucfg = json.load(open(os.path.dirname(os.getcwd()) + '/hucfg.json', 'r'))[re.search(r'##(.*)', os.getcwd()).group(1)]
loss = float(hucfg['lr']) + float(hucfg['wd']) ## in use

## write logs\
log_exp = 'haha'
import os, re, json; hucfg = json.load(open(os.path.dirname(os.getcwd()) + '/hucfg.json', 'r'))[re.search(r'##(.*)', os.getcwd()).group(1)]
log_str = str(re.search(r'##(.*)', os.getcwd()).group(1)) + ',' + str(hucfg)+ ',' + log_exp
with open(os.path.dirname(os.getcwd()) + '/logs.txt', 'a+', encoding="utf-8") as f: print(log_str, file=f)


