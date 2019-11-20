
# coding: utf-8

# In[1]:


import pyxrootd
import numpy as np
import ROOT


# In[21]:




Ele_16=[ 
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/DYjetsM10to50_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/DYjetsM50_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/GJets_HT-100To200_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/GJets_HT-200To400_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/GJets_HT-400To600_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/GJets_HT-40To100_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/GJets_HT-600ToInf_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ST_s-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ST_t-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ST_tW-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ST_tbar-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ST_tbarW-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TGJets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTGamma_Dilepton_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTGamma_Hadronic_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTGamma_SingleLept_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTWtoLNu_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTWtoQQ_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTZtoLL_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTbarPowheg_Dilepton_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTbarPowheg_Hadronic_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/TTbarPowheg_Semilept_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/W1jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/W2jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/W3jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/W4jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/WGamma_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/WW_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/WZ_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ZGamma_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/ZZ_skim.root',
]
Mu_16=[  
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/DYjetsM10to50_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/DYjetsM50_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/GJets_HT-100To200_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/GJets_HT-200To400_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/GJets_HT-400To600_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/GJets_HT-40To100_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/GJets_HT-600ToInf_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ST_s-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ST_t-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ST_tW-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ST_tbar-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ST_tbarW-channel_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TGJets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTGamma_Dilepton_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTGamma_Hadronic_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTGamma_SingleLept_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTWtoLNu_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTWtoQQ_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTZtoLL_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTbarPowheg_Dilepton_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTbarPowheg_Hadronic_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/TTbarPowheg_Semilept_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/W1jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/W2jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/W3jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/W4jets_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/WGamma_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/WW_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/WZ_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ZGamma_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/ZZ_skim.root',
]


# In[36]:


nevents_ele =[]
for f in Ele_16:
    fileName = '/eos/uscms/'+ f
    myfile = ROOT.TFile(fileName,'read')
    if myfile.IsZombie(): 
        print ("corrupted file",f)
        continue
    myhist = myfile.Get("hEvents")
    if myhist == None:
        print ("corrupted file",f)
        continue
#     print ("# of Events:  ",int(myhist.Integral(-1,-1)) )
    nevents_ele.append(int(myhist.Integral(-1,-1)))
    myfile.Close()
nevents_mu =[]  
for f in Mu_16:
    fileName = '/eos/uscms/'+ f
    myfile = ROOT.TFile(fileName,'read')
    if myfile.IsZombie(): 
        print ("corrupted file",f)
        continue
    myhist = myfile.Get("hEvents")
    if myhist == None:
        print ("corrupted file",f)
        continue
#     print ("# of Events:  ",int(myhist.Integral(-1,-1)) )
    nevents_mu.append(int(myhist.Integral(-1,-1)))
    myfile.Close()
print (nevents_ele ) 
print ('\n**********\n')
print (nevents_mu )
print ('\n**********\n')
print ([sum(x) for x in zip(nevents_ele, nevents_mu)])


# In[ ]:


'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_b_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_c_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_d_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_e_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_f_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_g_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/Data_SingleEle_h_skim.root',

'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_b_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_c_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_d_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_e_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_f_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_g_skim.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/Data_SingleMu_h_skim.root',

