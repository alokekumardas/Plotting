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

parser.add_option("--tight_ZJets", dest="tight_ZJets", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0_ZJets", dest="looseCRge2ge0_ZJets", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

parser.add_option("--looseCRge2e0_ZJets", dest="looseCRge2e0_ZJets", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

parser.add_option("--LooseCRe2e0_ZJets","--looseCRe2e0_ZJets", dest="looseCRe2e0_ZJets", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1_ZJets","--looseCRe2e1_ZJets", dest="looseCRe2e1_ZJets", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0_ZJets","--looseCRe3e0_ZJets", dest="looseCRe3e0_ZJets", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0_ZJets","--looseCRge4e0_ZJets", dest="looseCRge4e0_ZJets", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRe3e1_ZJets","--looseCRe3e1_ZJets", dest="looseCRe3e1_ZJets", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2_ZJets","--looseCRe2e2_ZJets", dest="looseCRe2e2_ZJets", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2_ZJets","--looseCRe3ge2_ZJets", dest="looseCRe3ge2_ZJets", default=False,action="store_true",
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
tight_ZJets = options.tight_ZJets
looseCRge2ge0_ZJets=options.looseCRge2ge0_ZJets
looseCRge2e0_ZJets =options.looseCRge2e0_ZJets
looseCRe2e0_ZJets  =options.looseCRe2e0_ZJets
looseCRe2e1_ZJets  =options.looseCRe2e1_ZJets
looseCRe3e0_ZJets  =options.looseCRe3e0_ZJets
looseCRge4e0_ZJets =options.looseCRge4e0_ZJets
looseCRe3e1_ZJets  =options.looseCRe3e1_ZJets
looseCRe2e2_ZJets  =options.looseCRe2e2_ZJets
looseCRe3ge2_ZJets =options.looseCRe3ge2_ZJets
useQCDMC = options.useQCDMC
useQCDCR = options.useQCDCR

gROOT.SetBatch(True)
#print "Caution: To plot postfit pass the argument --postfitPlots!!!"
if finalState=='DiMu':
	channel = 'mu'
	channelText = "#mu#mu+jets"
if finalState=='DiEle':
	channel = 'ele'
	channelText = "ee+jets"

rebin = 1
#######

########
if tight_ZJets:      #SR8 
	isSelection = "tight"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_tight/"%(selYear, channel)
	plotDirectory = "ZJets_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2ge0_ZJets:  #AR
	isSelection = "looseCRge2ge0"
	if selYear  =='2016': ZJetSF = 1; #getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = 1; #getZJetsSF(selYear,isSelection);
	else                : ZJetSF = 1; #getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0_ZJets:  #CR1+CR2+CR3
	isSelection = "looseCRge2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"
###
if looseCRe2e0_ZJets:  #CR1
	isSelection = "looseCRe2e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection); 
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0_ZJets:  #CR2
	isSelection = "looseCRe3e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0_ZJets:  #CR3
	isSelection = "looseCRge4e0"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1_ZJets:  #CR4
	isSelection = "looseCRe2e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1_ZJets:  #CR5
	isSelection = "looseCRe3e1"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection); 
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2_ZJets:  #CR6
	isSelection = "looseCRe2e2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2_ZJets:  #CR7
	isSelection = "looseCRe3ge2"
	if selYear  =='2016': ZJetSF = getZJetsSF(selYear,isSelection);
	elif selYear=='2017': ZJetSF = getZJetsSF(selYear,isSelection);
	else                : ZJetSF = getZJetsSF(selYear,isSelection);
	fileDir  = "histograms_%s/%s/Dilep_hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "ZJets_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"

###
if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

from Style import *

gROOT.ForceStyle()

sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
template_category = {"myZJets":kGreen+1, "myBackground":kRed, "myTotal":kBlue }
# template_category = {"MisIDEle":kRed, "ZgammaBkgPhoton":kOrange, "WgammaBkgPhoton":kBlue, "OtherSampleBkgPhoton":kGreen+1,"Total":kGray+3 }
# hist_category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
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

histName    = "presel_DilepMass_%s"
histNameData= "presel_DilepMass_%s"

if finalState=='DiEle':
    sample = "DataEle"
    file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
    dataHist = file[sample].Get(histNameData%(sample))
    dataHist.SetLineColor(kBlack)
    dataHist.SetMarkerStyle(8)


elif finalState=='DiMu':
	sample = "DataMu"
	file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)


else:
	print "Select the channel !!!"
	sys.exit()	

myhist ={}
summedHist ={}

for sample in sampleList:
	if finalState == 'DiMu'  and sample == 'QCD': sample = 'QCDMu'
	if finalState == 'DiEle'  and sample == 'QCD': sample = 'QCDEle'

	file[sample] = TFile('%s%s.root'%(fileDir,sample),'read')
	myhist[sample]= file[sample].Get(histName%(sample))

data_obs = dataHist.Clone("data_obs")

summedHist['myZJets'] = myhist['ZJets'].Clone('myZJets')

summedHist['myBackground'] = myhist['TTGamma'].Clone('myBackground')
summedHist['myBackground'].Add(myhist['TTbar'])
summedHist['myBackground'].Add(myhist['TGJets'])
summedHist['myBackground'].Add(myhist['WJets'])
summedHist['myBackground'].Add(myhist['SingleTop'])
summedHist['myBackground'].Add(myhist['WGamma'])
summedHist['myBackground'].Add(myhist['ZGamma'])
summedHist['myBackground'].Add(myhist['Diboson'])
summedHist['myBackground'].Add(myhist['TTV'])
summedHist['myBackground'].Add(myhist['GJets'])
if finalState == "DiMu": summedHist['myBackground'].Add(myhist['QCDMu'])
else: summedHist['myBackground'].Add(myhist['QCDEle'])

summedHist['myTotal'] = summedHist['myBackground'].Clone('myTotal')
summedHist['myTotal'].Add(summedHist['myZJets'])

binning = numpy.arange(80,100.1,rebin)

rebinnedHist ={} 
myfile = TFile(plotDirectory+"myZJets_Prefit.root","recreate")
for ih in summedHist:
	rebinnedHist[ih] = summedHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	rebinnedHist[ih].Write()

rebinnedData = data_obs.Rebin(len(binning)-1,"",binning)

rebinnedData.Write()


if postfitPlots:
	rebinnedHist['myZJets'].Scale(ZJetSF)

stack = THStack()
stack.Add(rebinnedHist['myBackground'])
stack.Add(rebinnedHist['myZJets'])


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
legend.AddEntry(rebinnedHist['myZJets'],'myZJets','f')
legend.AddEntry(rebinnedHist['myBackground'],'myBackground','f')
#legend.AddEntry(rebinnedHist['myTotal'],'myTotal','f')
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
stack.SetTitle(';;Events/%i GeV '%rebin)

CMS_lumi.channelText = channelText
CMS_lumi.channelText = regionText
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

ratio.GetYaxis().SetRangeUser(0.7,1.3)
ratio.GetYaxis().SetNdivisions(504)
if finalState == "DiMu": ratio.GetXaxis().SetTitle('m_{#mu^{+},#mu^{-}}')
else: ratio.GetXaxis().SetTitle('m_{e^{+},e^{-}}')

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
	canvasRatio.SaveAs("%s%s_massDilep_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massDilep_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
else:
	canvasRatio.SaveAs("%s%s_massDilep.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massDilep.pdf" %(plotDirectory,plotDirectory[:-1]))
canvasRatio.Close()

myfile.Close()
    
