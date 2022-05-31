def determine_type(mode):
    method = '' #Just to avoid unbound local
    
    if (mode == 1):
        method = lambda x: x.get_name().upper()
    elif (mode == 2):
        method = lambda x: x.get_packname().upper()
    elif (mode == 3):
        method = lambda x: x.get_paxnum()
    elif (mode == 4):
        method = lambda x: x.get_packcost()
    
    return method
