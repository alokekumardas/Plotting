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

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )


parser.add_option("--tight_fourTemplate", dest="tight_fourTemplate", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0_fourTemplate", dest="looseCRge2ge0_fourTemplate", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

parser.add_option("--looseCRge2e0_fourTemplate", dest="looseCRge2e0_fourTemplate", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

parser.add_option("--LooseCRe2e0_fourTemplate","--looseCRe2e0_fourTemplate", dest="looseCRe2e0_fourTemplate", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1_fourTemplate","--looseCRe2e1_fourTemplate", dest="looseCRe2e1_fourTemplate", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0_fourTemplate","--looseCRe3e0_fourTemplate", dest="looseCRe3e0_fourTemplate", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0_fourTemplate","--looseCRge4e0_fourTemplate", dest="looseCRge4e0_fourTemplate", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRe3e1_fourTemplate","--looseCRe3e1_fourTemplate", dest="looseCRe3e1_fourTemplate", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2_fourTemplate","--looseCRe2e2_fourTemplate", dest="looseCRe2e2_fourTemplate", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2_fourTemplate","--looseCRe3ge2_fourTemplate", dest="looseCRe3ge2_fourTemplate", default=False,action="store_true",
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

tight_fourTemplate = options.tight_fourTemplate
looseCRge2ge0_fourTemplate=options.looseCRge2ge0_fourTemplate
looseCRge2e0_fourTemplate =options.looseCRge2e0_fourTemplate
looseCRe2e0_fourTemplate  =options.looseCRe2e0_fourTemplate
looseCRe2e1_fourTemplate  =options.looseCRe2e1_fourTemplate
looseCRe3e0_fourTemplate  =options.looseCRe3e0_fourTemplate
looseCRge4e0_fourTemplate =options.looseCRge4e0_fourTemplate
looseCRe3e1_fourTemplate  =options.looseCRe3e1_fourTemplate
looseCRe2e2_fourTemplate  =options.looseCRe2e2_fourTemplate
looseCRe3ge2_fourTemplate =options.looseCRe3ge2_fourTemplate
useQCDMC = options.useQCDMC
useQCDCR = options.useQCDCR

gROOT.SetBatch(True)

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"

rebin = 2

if tight_fourTemplate:      #SR8    
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "fourTemplate_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2ge0_fourTemplate:  #AR
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"

if looseCRge2e0_fourTemplate:  #CR1+CR2+CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"
###
if looseCRe2e0_fourTemplate:  #CR1
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe3e0_fourTemplate:  #CR2
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0_fourTemplate:  #CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe2e1_fourTemplate:  #CR4
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	
if looseCRe3e1_fourTemplate:  #CR5
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2_fourTemplate:  #CR6
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2_fourTemplate:  #CR7
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "fourTemplate_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"

###
if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gROOT.SetBatch(True)
gStyle.SetOptStat(0)

sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
# template_category = {"myWGamma":kRed, "myZGamma":kOrange, "myBackground":kBlue, "myTotal":kGreen+1 }
template_category = {"MisIDEle":kRed, "ZgammaBkgPhoton":kOrange, "WgammaBkgPhoton":kBlue, "OtherSampleBkgPhoton":kGreen+1,"Total":kGray+3 }
hist_category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
file = {}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

from Style import *

if useQCDMC:
	if channel=="mu":	sampleList[-1] = "QCDMu"
	if channel=="ele":	sampleList[-1] = "QCDEle"
elif useQCDCR:
	sampleList[-1] = "QCD_DD"
	stackList.remove("GJets") 
else:
	print "use --useQCDMC or --useQCDCR!"
	sys.exit()

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

for sample in sampleList:
	item = "MisIDEle"
	tempHist = file[sample].Get(histName%(item,sample))
	if templateHist[item] is None:
		templateHist[item] = tempHist.Clone(item)
		templateHist[item].SetDirectory(0)
	else:
		templateHist[item].Add(tempHist)

############ from photon hist_category
intermediateHist ={}
for sample in sampleList:
	intermediateHist[sample] = None
	for item in ["GenuinePhoton","HadronicPhoton","HadronicFake"]:
		tempHist = file[sample].Get(histName%(item,sample))
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

binning = numpy.arange(60,140.1,rebin)

templateHist["Total"] = templateHist["MisIDEle"].Clone("Total")
templateHist["Total"].Add(templateHist["ZgammaBkgPhoton"])
templateHist["Total"].Add(templateHist["WgammaBkgPhoton"])
templateHist["Total"].Add(templateHist["OtherSampleBkgPhoton"])

rebinnedTotal = templateHist["Total"].Rebin(len(binning)-1,"",binning)

for ih in templateHist:
	templateHist[ih].Rebin(rebin)
	templateHist[ih].SetLineColor(template_category[ih])
	templateHist[ih].SetFillColor(template_category[ih])


rebinnedHist ={} 
myfile = TFile(plotDirectory+"fourTemplate_Prefit.root","recreate")
for ih in templateHist:
	rebinnedHist[ih] = templateHist[ih].Rebin(len(binning)-1,"",binning)
	rebinnedHist[ih].SetLineColor(template_category[ih])
	rebinnedHist[ih].SetFillColor(template_category[ih])
	rebinnedHist[ih].Write()

myData = dataHist.Clone("myData")
rebinnedData = myData.Rebin(len(binning)-1,"",binning)
rebinnedTotal.Write()
rebinnedData.Write()
myfile.Close()

