from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication,kGray
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
if tight:      #SR8 
	isSelectionDir = "tight"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
	
if looseCRge2ge0:  #AR
	isSelectionDir = "looseCRge2ge0"
	if selYear  =='2016': ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = 1; MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0:  #CR1+CR2+CR3
	isSelectionDir = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"

###
if looseCRe2e0:  #CR1
	isSelectionDir = "looseCRe2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);			
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0:  #CR2
	isSelectionDir = "looseCRe3e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0:  #CR3
	isSelectionDir = "looseCRge4e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1:  #CR4
	isSelectionDir = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = getFullYearMisIDEleSF(selYear,isSelectionDir);
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1:  #CR5
	isSelectionDir = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2:  #CR6
	isSelectionDir = "looseCRe2e2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2:  #CR7
	isSelectionDir = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	else :                ZJetSF = getZJetsSF(selYear,isSelectionDir); MisIDEleSF,ZGammaSF,WGammaSF = (1,1,1);
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "fourTemplate_Zjets_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
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
data_obs = dataHist.Clone("data_obs")
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
    binning = binning = numpy.arange(40,200.1,rebinLeftRight) #20 start

#if channel =='ele':
#    binningLeft   = list(numpy.arange(40,80.1,rebinLeftRight)) # 40, 20 start
#    binningCenter = list(numpy.arange(84,100.1,rebinCenter))
#    binningRight  = list(numpy.arange(120,160.1,rebinLeftRight))
#    binning = numpy.array(binningLeft + binningCenter + binningRight)
#else:
#    binning = binning = numpy.arange(10,210.1,rebinLeftRight) #20 start
    
    
      
rebinnedTotal = templateHist["Total"].Rebin(len(binning)-1,"",binning)
rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)
rebinnedHist ={} 
## input to combine 
myfile = TFile(plotDirectory+"fourTemplate_%s_Prefit.root"%(channel),"recreate")
for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	rebinnedHist[ih].Write()

rebinnedData.Write()
rebinnedTotal.Write()

## purpose for plotting 
rebinnedData.Scale(1.,"width")

for ih in rebinnedHist:
	rebinnedHist[ih].Scale(1.,"width")

if postfitPlots:
	rebinnedHist['WgammaBkgPhoton'].Scale(WGammaSF)
	rebinnedHist['ZgammaBkgPhoton'].Scale(ZGammaSF)
	rebinnedHist['MisIDEle'].Scale(MisIDEleSF)

stack = THStack()
stack.Add(rebinnedHist['OtherSampleBkgPhoton'])
stack.Add(rebinnedHist['WgammaBkgPhoton'])
stack.Add(rebinnedHist['ZgammaBkgPhoton'])
stack.Add(rebinnedHist['MisIDEle'])


if postfitPlots:
	rebinnedMC = stack.GetStack().Last().Clone("rebinnedMC")
	x = rebinnedData.Chi2Test(rebinnedMC,"UW CHI2/NDF") 
	chi2Text = "#chi^{2}/NDF=%.2f"%x

	
canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
canvasRatio.SetFillColor(0)
canvasRatio.SetBorderMode(0)
canvasRatio.SetFrameFillStyle(0)
canvasRatio.SetFrameBorderMode(0)
canvasRatio.SetLeftMargin( L/W )
canvasRatio.SetRightMargin( R/W )
canvasRatio.SetTopMargin( T/H )
canvasRatio.SetBottomMargin( B/H )
canvasRatio.SetTickx(0)
canvasRatio.SetTicky(0)
canvasRatio.Draw()
canvasRatio.cd()

pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
pad1.SetLeftMargin( L/W )
pad1.SetRightMargin( R/W )
pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetFrameFillStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetTickx(0)
pad1.SetTicky(0)

pad2.SetLeftMargin( L/W )
pad2.SetRightMargin( R/W )
pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )
pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetBorderMode(0)
pad2.SetFrameFillStyle(0)
pad2.SetFrameBorderMode(0)
pad2.SetTickx(0)
pad2.SetTicky(0)

pad1.Draw()
pad2.Draw()

noData = False

oneLine = TF1("oneline","1",-9e9,9e9)
oneLine.SetLineColor(kBlack)
oneLine.SetLineWidth(1)
oneLine.SetLineStyle(2)

maxVal = stack.GetMaximum()
if not noData: 
    maxVal = max(rebinnedData.GetMaximum(),maxVal)

minVal = 0
# minVal = max(stack.GetStack()[0].GetMinimum(),1)
stack.SetMaximum(1.25*maxVal)
stack.SetMinimum(minVal)

errorband=stack.GetStack().Last().Clone("error")
errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)

legend.AddEntry(rebinnedData,"Data", 'pe')
legend.AddEntry(rebinnedHist['MisIDEle'],'MisIDEle','f')
legend.AddEntry(rebinnedHist['ZgammaBkgPhoton'],'ZgammaBkgPhoton','f')
legend.AddEntry(rebinnedHist['WgammaBkgPhoton'],'WgammaBkgPhoton','f')
legend.AddEntry(rebinnedHist['OtherSampleBkgPhoton'],'OtherSampleBkgPhoton','f')
legend.AddEntry(errorband,"Uncertainty","f")

pad1.cd()

stack.Draw('HIST')
rebinnedData.Draw('E,X0,SAME')
legend.Draw("same")
stack.GetXaxis().SetTitle('')
stack.GetXaxis().SetLabelSize(0)
stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
stack.SetTitle(';;<Events/GeV>')# '%rebin)

#CMS_lumi.channelText = (channelText+"\\n"+regionText)
#if postfitPlots: CMS_lumi.channelText =channelText+"\\n "+regionText+"\\n "+chi2Text

CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText,regionText)
if postfitPlots: CMS_lumi.channelText =  "#splitline{%s}{%s}"%(channelText+";"+regionText,chi2Text)

CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
CMS_lumi.CMS_lumi(pad1, 4, 11)

if not noData:
	ratio = rebinnedData.Clone("temp")
	temp = stack.GetStack().Last().Clone("temp")
	for i_bin in range(1,temp.GetNbinsX()+1):
		temp.SetBinError(i_bin,0.)
	ratio.Divide(temp)
else:
	ratio = rebinnedData.Clone("temp")
	temp = stack.GetStack().Last().Clone("temp")
    
ratio.SetTitle('')
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap-padGap))

maxRatio = ratio.GetMaximum()
minRatio = ratio.GetMinimum()

for i_bin in range(1,ratio.GetNbinsX()):
	if ratio.GetBinError(i_bin)<1:
		if ratio.GetBinContent(i_bin)>maxRatio:
			maxRatio = ratio.GetBinContent(i_bin)
		if ratio.GetBinContent(i_bin)<minRatio:
			minRatio = ratio.GetBinContent(i_bin)

if maxRatio > 1.8:
	ratio.GetYaxis().SetRangeUser(0,round(0.5+maxRatio))
elif maxRatio < 1:
	ratio.GetYaxis().SetRangeUser(0,1.2)
elif maxRatio-1 < 1-minRatio:
	ratio.GetYaxis().SetRangeUser((1-(1-minRatio)*1.2),1.1*maxRatio)		
else:
	ratio.GetYaxis().SetRangeUser(2-1.1*maxRatio,1.1*maxRatio)

ratio.GetYaxis().SetRangeUser(0.6,1.4)
ratio.GetYaxis().SetNdivisions(504)
if channel == 'ele': ratio.GetXaxis().SetTitle('m_{e,#gamma} GeV')
else: ratio.GetXaxis().SetTitle('m_{#mu,#gamma} GeV')
ratio.GetYaxis().SetTitle("Data/MC")
pad2.cd()
CMS_lumi.CMS_lumi(pad2, 4, 11)

ratio.SetMarkerStyle(rebinnedData.GetMarkerStyle())
ratio.SetMarkerSize(rebinnedData.GetMarkerSize())
ratio.SetLineColor(rebinnedData.GetLineColor())
ratio.SetLineWidth(rebinnedData.GetLineWidth())
ratio.Draw('e,x0')
errorbandRatio = errorband.Clone("errorRatio")
errorbandRatio.Divide(temp)
errorbandRatio.Draw('e2,same')
oneLine.Draw("same")

canvasRatio.Update()
canvasRatio.RedrawAxis()
if postfitPlots:
	canvasRatio.SaveAs("%s%s_massEG_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massEG_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
else:
	canvasRatio.SaveAs("%s%s_massEG.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massEG.pdf" %(plotDirectory,plotDirectory[:-1]))
canvasRatio.Close()

myfile.Close()
    
