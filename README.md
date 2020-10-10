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
 - 2-7,9,11,16,20,22,23,25,27,30,31,34,37-41,47
 - 49-51,55,58,67-69,71,74,76,77,80,84,88,89,93
 - 3748,3749,3754,3758,3761-3763,3778,3779,3792
 - 3986-3992
 - 4040,4044,4045,4066,4078,4084,4087s
  
```


### Usage

Once you have built your variable file.
```bash
python3 vlan_differ.py 
```

#### Results

```bash
$ python3 vlan_differ.py 
Below is the differences between the VLAN lists:
3948
3907
3960
3983
3958
3965
3970
```
