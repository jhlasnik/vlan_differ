import yaml, sys

with open(r'vlan_vars.yml') as var_file:
    vlan_vars = yaml.load(var_file, Loader=yaml.FullLoader)

def Diff(li1, li2): 
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1)))) 

def flatten_vlan_list(vlans):
    vlan_list=[]
    for vlan_item in vlans:
        temp_list=[]
        vlan_line = vlan_item.split(',')
        for vlan_item in vlan_line:
            if isinstance(vlan_item, str) and '-' in vlan_item:
                range_index = vlan_item.split('-')
                for vlan_range in range(int(range_index[0]),int(range_index[1])+1):
                    vlan_list.append (str(vlan_range))
            else:
                vlan_list.append (vlan_item)
    return vlan_list

def main():
    dict_key = list(vlan_vars.keys())
    if len(dict_key) > 2:
        sys.exit('Error! Too many keys detected for VLAN mask diff')
    
    list1 = flatten_vlan_list(vlan_vars[dict_key[0]])
    list2 = flatten_vlan_list((vlan_vars[dict_key[1]]))   
    vlan_diff = Diff(list1, list2)
    if len(vlan_diff) > 0:
        print('Below is the differences between the VLAN lists:')
        for vlan in vlan_diff:
            print(vlan)
    else:
        print('No differences found between VLAN lists')


if __name__ == "__main__":
    main()