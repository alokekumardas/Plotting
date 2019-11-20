from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray,gSystem,gDirectory
#from ROOT import *
import os

import numpy
import sys
from optparse import OptionParser
from sampleInformation import sampleList
import sampleInformation
from numpy import log10
from array import array

from getFullYearMisIDEleSF import getFullYearMisIDEleSF
from getZJetsSF import getZJetsSF

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--postfitPlots", dest="postfitPlots", default=False,action="store_true",
					help="post fit plots" )

parser.add_option("--syst", "--systematics", dest="systematics", default="",type='str',
					help="Specify which systematic plots" )

parser.add_option("--level", dest="level", default="",type='str',
					help="Specify which level Up or Down" )
								
parser.add_option("--tight", dest="tight", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0", dest="looseCRge2ge0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

parser.add_option("--looseCRge2e0", dest="looseCRge2e0", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

parser.add_option("--LooseCRe2e0","--looseCRe2e0", dest="looseCRe2e0", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1","--looseCRe2e1", dest="looseCRe2e1", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0","--looseCRe3e0", dest="looseCRe3e0", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0","--looseCRge4e0", dest="looseCRge4e0", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRe3e1","--looseCRe3e1", dest="looseCRe3e1", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2","--looseCRe2e2", dest="looseCRe2e2", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2","--looseCRe3ge2", dest="looseCRe3ge2", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )  

parser.add_option("--useQCDMC","--qcdMC",dest="useQCDMC", default=False, action="store_true",
		  			 help="")

parser.add_option("--useQCDCR",dest="useQCDCR", default=False, action="store_true",
                     help="to make plots in QCDCR region")

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()
	
systematics = options.systematics
level=options.level
finalState = options.channel
postfitPlots = options.postfitPlots
tight = options.tight
looseCRge2ge0=options.looseCRge2ge0
looseCRge2e0 =options.looseCRge2e0
looseCRe2e0  =options.looseCRe2e0
looseCRe2e1  =options.looseCRe2e1
looseCRe3e0  =options.looseCRe3e0
looseCRge4e0 =options.looseCRge4e0
looseCRe3e1  =options.looseCRe3e1
looseCRe2e2  =options.looseCRe2e2
looseCRe3ge2 =options.looseCRe3ge2
useQCDMC = options.useQCDMC
useQCDCR = options.useQCDCR
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
#######
########

allsystematics = ["BTagSF_b"]

if level=='up': mylevel='Up'
if level=='down': mylevel='Down'

if tight:      #SR8 
	isSelectionDir = "tight"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_tight/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_tightplots_%s/"%(selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"
	else:
		fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_tightplots_%s/"%(selYear)
		regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2ge0:  #AR
	isSelectionDir = "looseCRge2ge0"
	if selYear  =='2016': ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2ge0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge2ge0plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge2ge0plots_%s/"%(selYear)
		regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0:  #CR1+CR2+CR3
	isSelectionDir = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge2e0plots_%s/"%(selYear)		
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge2e0plots_%s/"%(selYear)
		regionText = "N_{j}#geq2, N_{b}=0"

###
if looseCRe2e0:  #CR1
	isSelectionDir = "looseCRe2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);			
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e0plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e0plots_%s/"%(selYear)
		regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	isSelectionDir = "looseCRe3e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3e0plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3e0plots_%s/"%(selYear)
		regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	isSelectionDir = "looseCRge4e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRge4e0/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRge4e0plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRge4e0plots_%s/"%(selYear)
		regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	isSelectionDir = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e1/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e1plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e1plots_%s/"%(selYear)
		regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1:  #CR5
	isSelectionDir = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3e1/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3e1plots_%s/"%(selYear)
	else:	
		fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3e1plots_%s/"%(selYear)
		regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2:  #CR6
	isSelectionDir = "looseCRe2e2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe2e2/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe2e2plots_%s/"%(selYear)
	else:	
		fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe2e2plots_%s/"%(selYear)
		regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2:  #CR7
	isSelectionDir = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	if systematics in allsystematics:
		fileDir  = "histograms_%s/%s/hists_%s_%s_looseCRe3ge2/"%(selYear, channel,systematics,level)
		plotDirectory = "misIDEle_syst_looseCRe3ge2plots_%s/"%(selYear)
	else:
		fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
		plotDirectory = "misIDEle_syst_looseCRe3ge2plots_%s/"%(selYear)
		regionText = "N_{j}=3, N_{b}#geq2"

###
####
if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)
from Style import *
gROOT.ForceStyle()

sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# template_category = {"myWGamma":kRed, "myZGamma":kOrange, "myBackground":kBlue, "myTotal":kGreen+1 }
template_category = {"MisIDEle":kRed, "ZgammaBkgPhoton":kOrange, "WgammaBkgPhoton":kBlue, "OtherSampleBkgPhoton":kGreen+1,"Total":kGray+3 }
hist_category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
file = {}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

if useQCDMC:
	if channel=="mu":	sampleList[-1] = "QCDMu"
	if channel=="ele":	sampleList[-1] = "QCDEle"
elif useQCDCR:
	sampleList[-1] = "QCD_DD"
	stackList.remove("GJets") 
else:
	print "use --useQCDMC or --useQCDCR!"
	sys.exit()

H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

legendHeightPer = 0.04

legendStart = 0.6
legendEnd = 0.97-(R/W)

legend = TLegend(legendStart, 1-T/H-0.01 - legendHeightPer*(len(template_category)+4), legendEnd, 0.99-(T/H)-0.01)
legend.SetBorderSize(0)
legend.SetFillColor(0)

TGaxis.SetMaxDigits(3)
# histName    = "phosel_LeadingPhotonEt_%s_%s"
# histNameData= "phosel_LeadingPhotonEt_%s"

# histName    = "phosel_noCut_SIEIE_%s_%s"
# histNameData= "phosel_noCut_SIEIE_%s"

histName    = "phosel_MassEGamma_%s_%s"
histNameData= "phosel_MassEGamma_%s"

myfilename = "misIDEle_syst_Prefit"

templateHist ={}

for sample in sampleList:
	if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
	if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
	file[sample] = TFile('%s%s.root'%(fileDir,sample),'read')

templateHist["MisIDEle"] = None
templateHist["ZgammaBkgPhoton"] = None
templateHist["WgammaBkgPhoton"] = None
templateHist["OtherSampleBkgPhoton"] = None 
templateHist["Total"] = None 

for sample in sampleList:
	item = "MisIDEle"
	tempHist = file[sample].Get(histName%(item,sample))
	# scale the ZJetSF
	if sample=="ZJets": tempHist.Scale(ZJetSF)  #ZJetSF for misIDEle
	if templateHist[item] is None:
		templateHist[item] = tempHist.Clone(item)
		templateHist[item].SetDirectory(0)
	else:
		templateHist[item].Add(tempHist)

intermediateHist ={}
for sample in sampleList:
	intermediateHist[sample] = None
	for item in ["GenuinePhoton","HadronicPhoton","HadronicFake"]:
		tempHist = file[sample].Get(histName%(item,sample))
		if sample=="ZJets": tempHist.Scale(ZJetSF)  #ZJetSF for rest
		if intermediateHist[sample] is None:
			intermediateHist[sample] = tempHist.Clone(sample)
			intermediateHist[sample].SetDirectory(0)
		else:
				intermediateHist[sample].Add(tempHist)

for sample in sampleList:
	if   sample == "ZGamma": templateHist["ZgammaBkgPhoton"] = intermediateHist[sample].Clone("ZgammaBkgPhoton")
	elif sample == "WGamma": templateHist["WgammaBkgPhoton"] = intermediateHist[sample].Clone("WgammaBkgPhoton")
	else:
		if templateHist["OtherSampleBkgPhoton"] is None:
			templateHist["OtherSampleBkgPhoton"] = 	intermediateHist[sample].Clone("OtherSampleBkgPhoton")		
			templateHist["OtherSampleBkgPhoton"].SetDirectory(0)
		else:
			templateHist["OtherSampleBkgPhoton"].Add(intermediateHist[sample])

templateHist["Total"] = templateHist["MisIDEle"].Clone("Total")
templateHist["Total"].Add(templateHist["ZgammaBkgPhoton"])
templateHist["Total"].Add(templateHist["WgammaBkgPhoton"])
templateHist["Total"].Add(templateHist["OtherSampleBkgPhoton"])

rebinCenter = 2#2 #4
rebinLeftRight =10# 10 #20

if channel =='ele':
	binningLeft   = list(numpy.arange(40,80.1,rebinLeftRight)) # 40, 20 start
	binningCenter = list(numpy.arange(82,100.1,rebinCenter))
	binningRight  = list(numpy.arange(110,160.1,rebinLeftRight))
	binning = numpy.array(binningLeft + binningCenter + binningRight)
else:
	binning = numpy.arange(40,160.1,rebinLeftRight) #20 start

rebinnedHist ={} 
for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])

#rebinnedTotal = templateHist["Total"].Rebin(len(binning)-1,"",binning)

if systematics=='':
	if finalState=='Ele':
		sample = "DataEle"
		file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
		dataHist = file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)
			
	elif finalState=='Mu':
		sample = "DataMu"
		file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
		dataHist = file[sample].Get(histNameData%(sample))
		dataHist.SetLineColor(kBlack)
		dataHist.SetMarkerStyle(8)
	else:
		print "Select the channel !!!"
		sys.exit()	
	
	data_obs = dataHist.Clone("data_obs")
	rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)
## input to combine , open root file

myfile = TFile("%s%s.root"%(plotDirectory,myfilename),"update")

# create directory only if it does not exist
### ele channel
elChannelNominal = "elJets/nominal"
muChannelNominal = "muJets/nominal"
if channel=='ele':
	nominalDir = "elJets/nominal"
	if systematics=='':
		if myfile.GetDirectory(nominalDir):	
			gDirectory.cd(nominalDir)
			## delete 
			gDirectory.Delete("*;*")
			##
			rebinnedData.Write()
			rebinnedHist["MisIDEle"].Write()
			rebinnedHist["ZgammaBkgPhoton"].Write()
			rebinnedHist["WgammaBkgPhoton"].Write()
			rebinnedHist["OtherSampleBkgPhoton"].Write()
		else:
			myfile.mkdir(nominalDir)
			gDirectory.cd(nominalDir)
			rebinnedData.Write()
			rebinnedHist["MisIDEle"].Write()
			rebinnedHist["ZgammaBkgPhoton"].Write()
			rebinnedHist["WgammaBkgPhoton"].Write()
			rebinnedHist["OtherSampleBkgPhoton"].Write()
	else:
		systDir = "elJets/%s%s"%(systematics,mylevel)
		h_MisIDEle = rebinnedHist["MisIDEle"].Clone("MisIDEle%s"%mylevel)
		h_ZgammaBkgPhoton = rebinnedHist["ZgammaBkgPhoton"].Clone("ZgammaBkgPhoton%s"%mylevel)
		h_WgammaBkgPhoton = rebinnedHist["WgammaBkgPhoton"].Clone("WgammaBkgPhoton%s"%mylevel) 
		h_OtherSampleBkgPhoton = rebinnedHist["OtherSampleBkgPhoton"].Clone("OtherSampleBkgPhoton%s"%mylevel)
		if myfile.GetDirectory(systDir):
			gDirectory.cd(systDir)
			## delete all files here
			gDirectory.Delete("*;*")
			h_MisIDEle.Write()
			h_WgammaBkgPhoton.Write()
			h_ZgammaBkgPhoton.Write()
			h_OtherSampleBkgPhoton.Write()
		else:
			myfile.mkdir(systDir)
			gDirectory.cd(systDir)
			h_MisIDEle.Write()
			h_ZgammaBkgPhoton.Write()
			h_WgammaBkgPhoton.Write()
			h_OtherSampleBkgPhoton.Write()
### mu channel	
if channel=='mu':
	nominalDir = "muJets/nominal"
	if systematics=='':
		if myfile.GetDirectory(nominalDir):	
			gDirectory.cd(nominalDir)
			## delete 
			gDirectory.Delete("*;*")
			rebinnedData.Write()
			rebinnedHist["MisIDEle"].Write()
			rebinnedHist["ZgammaBkgPhoton"].Write()
			rebinnedHist["WgammaBkgPhoton"].Write()
			rebinnedHist["OtherSampleBkgPhoton"].Write()
		else:
			myfile.mkdir(nominalDir)
			gDirectory.cd(nominalDir)
			rebinnedData.Write()
			rebinnedHist["MisIDEle"].Write()
			rebinnedHist["ZgammaBkgPhoton"].Write()
			rebinnedHist["WgammaBkgPhoton"].Write()
			rebinnedHist["OtherSampleBkgPhoton"].Write()
	else:
		systDir = "muJets/%s%s"%(systematics,mylevel)
		h_MisIDEle = rebinnedHist["MisIDEle"].Clone("MisIDEle%s"%mylevel)
		h_ZgammaBkgPhoton = rebinnedHist["ZgammaBkgPhoton"].Clone("ZgammaBkgPhoton%s"%mylevel)
		h_WgammaBkgPhoton = rebinnedHist["WgammaBkgPhoton"].Clone("WgammaBkgPhoton%s"%mylevel) 
		h_OtherSampleBkgPhoton = rebinnedHist["OtherSampleBkgPhoton"].Clone("OtherSampleBkgPhoton%s"%mylevel)
		if myfile.GetDirectory(systDir):
			gDirectory.cd(systDir)
			gDirectory.Delete("*;*")
			## delete all files here
			h_MisIDEle.Write()
			h_ZgammaBkgPhoton.Write()
			h_WgammaBkgPhoton.Write()
			h_OtherSampleBkgPhoton.Write()
		else:
			myfile.mkdir(systDir)
			gDirectory.cd(systDir)
			h_MisIDEle.Write()
			h_ZgammaBkgPhoton.Write()
			h_WgammaBkgPhoton.Write()
			h_OtherSampleBkgPhoton.Write()

print "%s%s.root"%(plotDirectory,myfilename)

myfile.Close()


#for h in histograms:
#    outputFile.Delete("%s;*"%h.GetName())
#    if onlyAddPlots:
##        gDirectory.Delete("%s;*"%(h.GetName()))
#    h.Write()

#outputFile.Close()

#####


    
