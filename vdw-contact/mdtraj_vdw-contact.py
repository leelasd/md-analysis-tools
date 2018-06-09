import mdtraj as md
import pandas as pd
import numpy as np
def GetContacts(traj,sel,cutoff):
    res = md.compute_neighbors(traj,cutoff*0.1,lig)
    contacts = [len(np.setdiff1d(res[i], lig)) for i in range(len(res))]
    return contacts
traj = md.load('plig_cutoff.h5')
top = traj.topology
lig = top.select('chainid 2 and mass>2')
conts = GetContacts(traj,sel=lig,cutoff=3)
import matplotlib.pyplot as plt
plt.plot(conts)
plt.show()
