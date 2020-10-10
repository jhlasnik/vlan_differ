# VLAN Diff Tool
A simple tool to quickly determine the VLAN differences between two interfaces.

### Requirements

Python3
PyYAML

### Prerequisites  / Prepwork

A YAML file named vlan_vars.yml is required in the active directory where the script will be run, an example has been included in the repository.
Example file vlan_vars.yml

```yaml
list1:
 - 2-7,9,11,16,20,22,23,25,27,30,31,34,37-41,47
 - 49-51,55,58,67-69,71,74,76,77,80,84,88,89,93
 - 3748,3749,3754,3758,3761-3763,3778,3779,3792
 - 3907,3948,3958,3960,3965,3970,3983,3986-3992
 - 4040,4044,4045,4066,4078,4084,4087

list2:
 - 2-7,9,11,16,17,20,22,23,25,27,30,31,34,37-41,43
 - 44,46,49-51,55,58,67,68,74,77,80,84,88,89,91
 - 92,95-98,100,102-104,106,108-114,117,119,120
 - 124-129,131-134,136,137,140-147,149-152,154
 - 156,157,159,160,168,169,172,173,176,180,187
 - 189,190,192,196-198,201,203,204,206,207,211
 - 214-216,220,222,227,228,230-232,234,235,237
  
```


### Usage

Once you have built your variable file.
```bash
python3 vlan_differ.py 
```

#### Results

```bash
EXP11223:vlan_differ joseph.hlasnik$ python3 vlan_differ.py 
Below is the differences between the VLAN lists:
3948
3907
3960
3983
3958
3965
3970
```
