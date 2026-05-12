def bojanje(cstate, crijec,):
    obojano=''
    for j in range(len(cstate)):
        if cstate[j] == 1:
            obojano += "\033[93m{}\033[00m".format(crijec[j].upper())
        elif cstate[j] == 2:
            obojano += "\033[92m{}\033[00m".format(crijec[j].upper())
        else:
            obojano += "\033[97m{}\033[00m".format(crijec[j].upper())
    return(obojano)