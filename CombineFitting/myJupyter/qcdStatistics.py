
# coding: utf-8

# In[1]:


import pyxrootd
import numpy as np
import ROOT


# In[2]:


qcdEle_16=[ 
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt20to30_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt30to50_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt50to80_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt80to120_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt120to170_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt170to300_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/electrons/QCD_Pt300toInf_Ele_skim.root'
]

qcdMu_16=[  
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt20to30_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt30to50_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt50to80_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt80to120_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt120to170_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt170to300_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt300to470_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt470to600_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt600to800_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt800to1000_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_skims/muons/QCD_Pt1000toInf_Mu_skim.root']


# In[3]:


qcdEle_17=[ 
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt20to30_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt30to50_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt50to80_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt80to120_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt120to170_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt170to300_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/electrons/QCD_Pt300toInf_Ele_skim.root']


qcdMu_17=[  
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt20to30_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt30to50_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt50to80_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt80to120_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt120to170_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt170to300_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt300to470_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt470to600_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt600to800_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt800to1000_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_skims/muons/QCD_Pt1000toInf_Mu_skim.root']


# In[4]:


qcdEle_18=[ 
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt20to30_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt30to50_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt50to80_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt80to120_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt120to170_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt170to300_Ele_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/electrons/QCD_Pt300toInf_Ele_skim.root'
]

qcdMu_18=[  
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt20to30_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt30to50_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt50to80_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt80to120_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt120to170_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt170to300_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt300to470_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt470to600_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt600to800_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt800to1000_Mu_skim.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_skims/muons/QCD_Pt1000toInf_Mu_skim.root']


# In[8]:


allSkimList = qcdEle_18 + qcdMu_18 
for f in allSkimList:
    fileName = '/eos/uscms/'+ f
    myfile = ROOT.TFile(fileName,'read')
    if myfile.IsZombie(): 
        print ("corrupted file:", "skim",'20'+f[34:36]+''+f[59:-10])
        continue
    myhist = myfile.Get("hEvents")
    if myhist == None:
        print ("corrupted file:", "         skim",'20'+f[34:36]+''+f[59:-10])
        continue
    print ("# of Events:  ",int(myhist.Integral(-1,-1)), "\t", "skim",'20'+f[34:36]+' '+f[59:-10] )
    myfile.Close()

    


# In[ ]:


allNtupleList = ['/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt30to50_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt80to120_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt120to170_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt170to300_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt300toInf_Ele_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt600to800_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt800to1000_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt1000toInf_Mu_2016_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt30to50_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt80to120_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt120to170_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt170to300_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt300toInf_Ele_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt600to800_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt800to1000_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt1000toInf_Mu_2017_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt30to50_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt80to120_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt120to170_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt170to300_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt300toInf_Ele_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt600to800_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt800to1000_Mu_2018_AnalysisNtuple.root',
            '/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt1000toInf_Mu_2018_AnalysisNtuple.root']

