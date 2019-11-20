
# coding: utf-8

# In[1]:


import pyxrootd
import uproot
import numpy as np
import coffea


# In[2]:


mylist_16_mu = ['/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/DYjetsM10to50_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/DYjetsM50_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_b_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_c_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_d_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_e_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_f_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_g_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/Data_SingleMu_h_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/GJets_HT-100To200_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/GJets_HT-200To400_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/GJets_HT-400To600_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/GJets_HT-40To100_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/GJets_HT-600ToInf_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt1000toInf_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt600to800_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt800to1000_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ST_s-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ST_t-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ST_tW-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ST_tbar-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ST_tbarW-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TGJets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTGamma_Dilepton_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTGamma_Hadronic_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTGamma_SingleLept_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTWtoLNu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTWtoQQ_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTZtoLL_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTbarPowheg_Dilepton_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTbarPowheg_Hadronic_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/TTbarPowheg_Semilept_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/W1jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/W2jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/W3jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/W4jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/WGamma_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/WW_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/WZ_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ZGamma_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/muons/ZZ_2016_AnalysisNtuple.root']


# In[3]:


mylist_16_ele =['/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/DYjetsM10to50_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/DYjetsM50_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_b_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_c_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_d_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_e_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_f_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_g_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/Data_SingleEle_h_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/GJets_HT-100To200_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/GJets_HT-200To400_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/GJets_HT-400To600_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/GJets_HT-40To100_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/GJets_HT-600ToInf_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ST_s-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ST_t-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ST_tW-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ST_tbar-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ST_tbarW-channel_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TGJets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTGamma_Dilepton_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTGamma_Hadronic_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTGamma_SingleLept_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTWtoLNu_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTWtoQQ_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTZtoLL_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Dilepton_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Hadronic_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Semilept_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/W1jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/W2jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/W3jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/W4jets_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/WGamma_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/WW_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/WZ_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ZGamma_2016_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_16/13TeV_AnalysisNtuples/electrons/ZZ_2016_AnalysisNtuple.root']


# In[4]:


mylist_17_mu =['/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/DYjetsM10to50_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/DYjetsM50_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/Data_SingleMu_b_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/Data_SingleMu_c_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/Data_SingleMu_d_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/Data_SingleMu_e_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/Data_SingleMu_f_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/GJets_HT-100To200_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/GJets_HT-200To400_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/GJets_HT-400To600_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/GJets_HT-40To100_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/GJets_HT-600ToInf_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ST_s-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ST_t-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ST_tW-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ST_tbar-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ST_tbarW-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TGJets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTGamma_Dilepton_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTGamma_Hadronic_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTGamma_Hadronic_2017_AnalysisNtuple_oldSF.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTGamma_SingleLept_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTWtoLNu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTWtoQQ_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTZtoLL_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTbarPowheg_Dilepton_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTbarPowheg_Hadronic_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/TTbarPowheg_Semilept_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/W1jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/W2jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/W3jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/W4jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/WGamma_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/WW_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/WZ_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ZGamma_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/muons/ZZ_2017_AnalysisNtuple.root']


# In[5]:


mylist_17_ele =['/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/DYjetsM10to50_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/DYjetsM50_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/Data_SingleEle_b_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/Data_SingleEle_c_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/Data_SingleEle_d_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/Data_SingleEle_e_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/Data_SingleEle_f_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/GJets_HT-100To200_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/GJets_HT-200To400_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/GJets_HT-400To600_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/GJets_HT-40To100_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/GJets_HT-600ToInf_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt120to170_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt300toInf_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt30to50_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/QCD_Pt80to120_Ele_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ST_s-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ST_t-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ST_tW-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ST_tbar-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ST_tbarW-channel_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TGJets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTGamma_Dilepton_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTGamma_Hadronic_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTGamma_SingleLept_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTWtoLNu_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTWtoQQ_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTZtoLL_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Dilepton_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Hadronic_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Semilept_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/W1jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/W2jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/W3jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/W4jets_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/WGamma_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/WW_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/WZ_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ZGamma_2017_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_17/13TeV_AnalysisNtuples/electrons/ZZ_2017_AnalysisNtuple.root']


# In[6]:


mylist_18_mu = ['/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/DYjetsM10to50_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/DYjetsM50_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/Data_SingleMu_a_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/Data_SingleMu_b_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/Data_SingleMu_c_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/Data_SingleMu_d_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/GJets_HT-100To200_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/GJets_HT-200To400_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/GJets_HT-400To600_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/GJets_HT-40To100_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/GJets_HT-600ToInf_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt1000toInf_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt120to170_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt170to300_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt20to30_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt300to470_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt30to50_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt470to600_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt50to80_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt600to800_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt800to1000_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/QCD_Pt80to120_Mu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ST_s-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ST_t-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ST_tW-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ST_tbar-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ST_tbarW-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TGJets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTGamma_Dilepton_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTGamma_Hadronic_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTGamma_SingleLept_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTWtoLNu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTWtoQQ_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTZtoLL_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTbarPowheg_Dilepton_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTbarPowheg_Hadronic_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/TTbarPowheg_Semilept_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/W1jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/W2jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/W3jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/W4jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/WGamma_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/WW_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/WZ_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ZGamma_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/muons/ZZ_2018_AnalysisNtuple.root']


# In[7]:


mylist_18_ele =['/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/DYjetsM10to50_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/DYjetsM50_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/Data_SingleEle_a_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/Data_SingleEle_b_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/Data_SingleEle_c_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/Data_SingleEle_d_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/GJets_HT-100To200_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/GJets_HT-200To400_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/GJets_HT-400To600_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/GJets_HT-40To100_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/GJets_HT-600ToInf_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt120to170_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt170to300_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt20to30_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt300toInf_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt30to50_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt50to80_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/QCD_Pt80to120_Ele_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ST_s-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ST_t-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ST_tW-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ST_tbar-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ST_tbarW-channel_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TGJets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTGamma_Dilepton_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTGamma_Hadronic_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTGamma_SingleLept_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTWtoLNu_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTWtoQQ_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTZtoLL_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Dilepton_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Hadronic_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/TTbarPowheg_Semilept_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/W1jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/W2jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/W3jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/W4jets_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/WGamma_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/WW_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/WZ_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ZGamma_2018_AnalysisNtuple.root',
'/store/user/aldas/NanoAOD/TTGamma_18/13TeV_AnalysisNtuples/electrons/ZZ_2018_AnalysisNtuple.root']


# In[8]:


for f in mylist_16_mu:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:63]+' --> '+ f[65:-25])
    


# In[9]:


for f in mylist_16_ele:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:68]+' --> '+ f[69:-25])


# In[10]:


for f in mylist_17_mu:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:63]+' --> '+ f[65:-25])


# In[11]:


for f in mylist_17_ele:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:68]+' --> '+ f[69:-25])


# In[12]:


for f in mylist_18_mu:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:63]+' --> '+ f[65:-25])


# In[13]:


for f in mylist_18_ele:
    mytree = uproot.open('root://cmseos.fnal.gov/'+ f)['AnalysisTree']
    eventWeight = mytree.array('evtWeight')
    print (eventWeight[0], "\t\t", np.mean(eventWeight), "\t", '20'+f[34:36]+' -> '+f[59:68]+' --> '+ f[69:-25])

