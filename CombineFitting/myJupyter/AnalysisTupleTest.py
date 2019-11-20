
# coding: utf-8

# In[79]:


import pyxrootd
import numpy, sys
import uproot
import matplotlib.pyplot as plt
from scipy.signal import find_peaks_cwt


# In[87]:


fileName = '/eos/uscms/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/W4jets_2016_AnalysisNtuple.root'
mytree = uproot.open('root://cmseos.fnal.gov/'+ fileName)['AnalysisTree']
# mytree.show()
# mytree.name, mytree.numentries


# In[88]:


lepCut  = (mytree.array('nEle')==1) # gives T or F
jetCut  = (mytree.array('nJet')==2) & lepCut
bjetCut = (mytree.array('nBJet')==0) & jetCut
pfMet  = numpy.array(mytree.array('pfMET')[bjetCut])
print (pfMet.size, '',numpy.mean(pfMet))
plt.hist(pfMet,bins=100,range=(0,500))
# plt.yscale('log')
plt.show()

