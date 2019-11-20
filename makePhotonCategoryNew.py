from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F, gROOT, kBlack,kOrange,kRed,kGreen,kBlue,gApplication
#from ROOT import *
import os

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

parser.add_option("--postfit", dest="postfit", default=False,action="store_true",
					help="draw postfit plots" )

parser.add_option("--tight_photonCategory", dest="tight_photonCategory", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0_photonCategory", dest="looseCRge2ge0_photonCategory", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )

parser.add_option("--looseCRge2e0_photonCategory", dest="looseCRge2e0_photonCategory", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 =0" )

###
parser.add_option("--LooseCRe2e0_photonCategory","--looseCRe2e0_photonCategory", dest="looseCRe2e0_photonCategory", default=False,action="store_true",
                     help="Use ==2 jets + ==0 bjets selection" )  

parser.add_option("--LooseCRe2e1_photonCategory","--looseCRe2e1_photonCategory", dest="looseCRe2e1_photonCategory", default=False,action="store_true",
                     help="Use ==2 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe3e0_photonCategory","--looseCRe3e0_photonCategory", dest="looseCRe3e0_photonCategory", default=False,action="store_true",
                     help="Use ==3 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRge4e0_photonCategory","--looseCRge4e0_photonCategory", dest="looseCRge4e0_photonCategory", default=False,action="store_true",
                     help="Use >=4 jets + ==0 bjets selection" ) 

parser.add_option("--LooseCRe3e1_photonCategory","--looseCRe3e1_photonCategory", dest="looseCRe3e1_photonCategory", default=False,action="store_true",
                     help="Use ==3 jets + ==1 bjets selection" ) 

parser.add_option("--LooseCRe2e2_photonCategory","--looseCRe2e2_photonCategory", dest="looseCRe2e2_photonCategory", default=False,action="store_true",
                     help="Use ==2 jets + ==2 bjets selection" ) 

parser.add_option("--LooseCRe3ge2_photonCategory","--looseCRe3ge2_photonCategory", dest="looseCRe3ge2_photonCategory", default=False,action="store_true",
                     help="Use ==3 jets + >=2 bjets selection" )  
##
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
tight_photonCategory = options.tight_photonCategory
looseCRge2ge0_photonCategory=options.looseCRge2ge0_photonCategory
looseCRge2e0_photonCategory =options.looseCRge2e0_photonCategory
looseCRe2e0_photonCategory  =options.looseCRe2e0_photonCategory
looseCRe2e1_photonCategory  =options.looseCRe2e1_photonCategory
looseCRe3e0_photonCategory  =options.looseCRe3e0_photonCategory
looseCRge4e0_photonCategory =options.looseCRge4e0_photonCategory
looseCRe3e1_photonCategory  =options.looseCRe3e1_photonCategory
looseCRe2e2_photonCategory  =options.looseCRe2e2_photonCategory
looseCRe3ge2_photonCategory =options.looseCRe3ge2_photonCategory
postfit = options.postfit
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
selectionRange1=60
selectionRange2=140

if tight_photonCategory:      #SR8    
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "pho_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 1 # 6.1569
	elif selYear == '2017': MisIDEleSF = 1 #7.13875, #11.6506
	else:                   MisIDEleSF = 1 #3.53722

if looseCRge2ge0_photonCategory:  #AR
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"
	if selYear == '2016':   MisIDEleSF = 2.17335 
	elif selYear == '2017': MisIDEleSF = 3.04964 
	else:                   MisIDEleSF = 1.96952 

if looseCRge2e0_photonCategory:  #CR1+CR2+CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge2e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}=0"
	if selYear == '2016':   MisIDEleSF = 2.21111
	elif selYear == '2017': MisIDEleSF = 3.17469
	else:                   MisIDEleSF = 1.89272 
###
if looseCRe2e0_photonCategory:  #CR1
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"
	if selYear == '2016':   MisIDEleSF = 2.27068
	elif selYear == '2017': MisIDEleSF = 2.96026 
	else:                   MisIDEleSF = 2.09033

if looseCRe3e0_photonCategory:  #CR2
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"
	if selYear == '2016':   MisIDEleSF = 1.97812
	elif selYear == '2017': MisIDEleSF = 8.77671
	else:                   MisIDEleSF = 1.88836

if looseCRge4e0_photonCategory:  #CR3
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 2.161
	elif selYear == '2017': MisIDEleSF = 4.86253 #19.9952 before rebining 
	else:                   MisIDEleSF = 2.45367 

if looseCRe2e1_photonCategory:  #CR4
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 1.83318
	elif selYear == '2017': MisIDEleSF = 2.61846 #2.04351
	else:                   MisIDEleSF = 2.4527 
	
if looseCRe3e1_photonCategory:  #CR5
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 2.57951
	elif selYear == '2017': MisIDEleSF = 2.47114 #1.83117 
	else:                   MisIDEleSF = 2.45971 

if looseCRe2e2_photonCategory:  #CR6
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 1.40717
	elif selYear == '2017': MisIDEleSF = 1.19915 #1.15859
	else:                   MisIDEleSF = 2.35618 

if looseCRe3ge2_photonCategory:  #CR7
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"
	rebin = 4
	if selYear == '2016':   MisIDEleSF = 0.968788
	elif selYear == '2017': MisIDEleSF = 2.0612 #2.49511 
	else:                   MisIDEleSF = 3.9222 

###
if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

# gROOT.SetBatch(True)
# gStyle.SetOptStat(0)

sampleList = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
category = {"GenuinePhoton":kOrange, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen+1 }
file = {}

import CMS_lumi

if selYear == '2016':	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
if selYear == '2017':	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
if selYear == '2018':	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

from Style import *
thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
	ROOT.gROOT.ProcessLine('.L tdrstyle.C')
	ROOT.setTDRStyle()
	print "Found tdrstyle.C file, using this style."
	HasCMSStyle = True
	if os.path.isfile('CMSTopStyle.cc'):
		gROOT.ProcessLine('.L CMSTopStyle.cc+')
		style = CMSTopStyle()
		style.setupICHEPv1()
		print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
	# print "Using default style defined in cuy package."
	thestyle.SetStyle()

ROOT.gROOT.ForceStyle()


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

legend = TLegend(legendStart, 1-T/H-0.01 - legendHeightPer*(len(category)+5), legendEnd, 0.99-(T/H)-0.01)
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
	dataHist.Rebin(rebin)

elif finalState=='Mu':
	sample = "DataMu"
	file[sample] = TFile("%s%s.root"%(fileDir,sample),"read")
	dataHist = file[sample].Get(histNameData%(sample))
	dataHist.SetLineColor(kBlack)
	dataHist.SetMarkerStyle(8)
	dataHist.Rebin(rebin)

else:
	print "Select the channel !!!"
	sys.exit()	

summedHist ={}

for item in category.keys():
	summedHist[item] = None
	for sample in sampleList:
		if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
		if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
		file[sample] = TFile('%s%s.root'%(fileDir,sample),'read')
		tempHist = file[sample].Get(histName%(item,sample))
		if summedHist[item] is None:
			summedHist[item] = tempHist.Clone(item)
			summedHist[item].SetDirectory(0)
		else:
			summedHist[item].Add(tempHist)
if postfit:
	summedHist['MisIDEle'].Scale(MisIDEleSF)

for ih in summedHist:
	summedHist[ih].Rebin(rebin)
	summedHist[ih].SetLineColor(category[ih])
	summedHist[ih].SetFillColor(category[ih])

stack = THStack()
stack.Add(summedHist['HadronicPhoton'])
stack.Add(summedHist['HadronicFake'])
stack.Add(summedHist['GenuinePhoton'])
stack.Add(summedHist['MisIDEle'])
### range fit.
x1=80
x2=100
nBins = (x2-x1)/rebin
h1 = TH1F('myMisIDEle','',nBins,x1,x2)
h2 = TH1F('myHadronicPhoton','',nBins,x1,x2)
h3 = TH1F('myGenuinePhoton','',nBins,x1,x2)
h4 = TH1F('myHadronicFake','',nBins,x1,x2)
h5 = TH1F('myData','',nBins,x1,x2)
h6 = TH1F('myBackground','',nBins,x1,x2)
h7 = TH1F('myTotal','',nBins,x1,x2)

for i in xrange(0,nBins+1):
	h1.SetBinContent(1+i,summedHist['MisIDEle'].GetBinContent(x1/rebin+i+1))
	h2.SetBinContent(1+i,summedHist['HadronicPhoton'].GetBinContent(x1/rebin+i+1))
	h3.SetBinContent(1+i,summedHist['GenuinePhoton'].GetBinContent(x1/rebin+i+1))
	h4.SetBinContent(1+i,summedHist['HadronicFake'].GetBinContent(x1/rebin+i+1))
	h5.SetBinContent(1+i,dataHist.GetBinContent(x1/rebin+i+1))

h6.Add(h2)
h6.Add(h3)
h6.Add(h4)

h7.Add(h6)
h7.Add(h1)
####
# myMisIDEle = summedHist['MisIDEle'].Clone('myMisIDEle')
# OtherHisttemp = summedHist['GenuinePhoton']
# OtherHisttemp.Add(summedHist['HadronicFake'])
# OtherHisttemp.Add(summedHist['HadronicPhoton'])
# myBackground    = OtherHisttemp.Clone("myBackground")
# myData = dataHist.Clone("myData")

# myTotal = myMisIDEle.Clone("myTotal")
# myTotal.Add(myBackground)
if postfit:
	myfile = TFile(plotDirectory+"myMisIDEle_Postfit.root","recreate")
else:
	myfile = TFile(plotDirectory+"myMisIDEle_Prefit.root","recreate")

h1.Write()
h5.Write()
h6.Write()
h7.Write()

# myMisIDEle.Write()
# myBackground.Write()
# myData.Write()
# myTotal.Write()
# myfile.Close()

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

# text = TPaveText(0.35,.75,0.45,0.85,"NDC")
# text.SetTextColor(kBlack)
# text.SetFillColor(0)
# text.SetTextSize(0.04)
# text.SetTextFont(42)

maxVal = stack.GetMaximum()
if not noData: 
    maxVal = max(dataHist.GetMaximum(),maxVal)

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

legend.AddEntry(dataHist,  "Data", 'pe')
legend.AddEntry(summedHist['MisIDEle'],'MisIDEle','f')
legend.AddEntry(summedHist['GenuinePhoton'],'GenuinePhoton','f')
legend.AddEntry(summedHist['HadronicFake'],'HadronicFake','f')
legend.AddEntry(summedHist['HadronicPhoton'],'HadronicPhoton','f')
legend.AddEntry(errorband,"Uncertainty","f")

pad1.cd()

stack.Draw('HIST')
dataHist.Draw('E,X0,SAME')
# text.Draw("same")
legend.Draw("same")
stack.GetXaxis().SetTitle('')
stack.GetXaxis().SetLabelSize(0)
stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
stack.SetTitle(';;Events/%i GeV '%rebin)
stack.GetXaxis().SetRangeUser(selectionRange1,selectionRange2)

# CMS_lumi.channelText = channelText
# CMS_lumi.channelText = regionText
# CMS_lumi.writeChannelText = True
# CMS_lumi.writeExtraText = True
CMS_lumi.CMS_lumi(pad1, 4, 11)

if not noData:
	ratio = dataHist.Clone("temp")
	temp = stack.GetStack().Last().Clone("temp")
	for i_bin in range(1,temp.GetNbinsX()+1):
		temp.SetBinError(i_bin,0.)
	ratio.Divide(temp)
else:
	ratio = dataHist.Clone("temp")
	temp = stack.GetStack().Last().Clone("temp")
    
ratio.SetTitle('')
ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))

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
ratio.GetXaxis().SetTitle('m_{e,#gamma}')
ratio.GetYaxis().SetTitle("Data/MC")
ratio.GetXaxis().SetRangeUser(selectionRange1,selectionRange2)
pad2.cd()
CMS_lumi.CMS_lumi(pad2, 4, 11)

ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
ratio.SetMarkerSize(dataHist.GetMarkerSize())
ratio.SetLineColor(dataHist.GetLineColor())
ratio.SetLineWidth(dataHist.GetLineWidth())
ratio.Draw('e,x0')
errorbandRatio = errorband.Clone("errorRatio")
errorbandRatio.Divide(temp)
errorbandRatio.Draw('e2,same')
oneLine.Draw("same")

canvasRatio.Update()
canvasRatio.RedrawAxis()
if postfit:
	canvasRatio.SaveAs("%s%s_massEG_Postfit.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massEG_Postfit.pdf" %(plotDirectory,plotDirectory[:-1]))
else:
	canvasRatio.SaveAs("%s%s_massEG.root"%(plotDirectory,plotDirectory[:-1]))
	canvasRatio.Print("%s%s_massEG.pdf" %(plotDirectory,plotDirectory[:-1]))
canvasRatio.Close()
    

