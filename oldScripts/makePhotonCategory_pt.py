from ROOT import *
import os
import sys
from optparse import OptionParser
import CMS_lumi

parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
					help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )

parser.add_option("--tight_photonCategory", dest="tight_photonCategory", default=False,action="store_true",
					help="draw photon Category for tight selection" )

parser.add_option("--looseCRge2ge0_photonCategory", dest="looseCRge2ge0_photonCategory", default=False,action="store_true",
					help="draw photon Category for loose CR ge2 ge0" )
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

(options, args) = parser.parse_args()
selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()
finalState = options.channel
tight_photonCategory = options.tight_photonCategory
looseCRge2ge0_photonCategory = options.looseCRge2ge0_photonCategory
looseCRe2e0_photonCategory = options.looseCRe2e0_photonCategory
looseCRe2e1_photonCategory = options.looseCRe2e1_photonCategory
looseCRe3e0_photonCategory = options.looseCRe3e0_photonCategory
looseCRge4e0_photonCategory = options.looseCRge4e0_photonCategory
looseCRe3e1_photonCategory = options.looseCRe3e1_photonCategory
looseCRe2e2_photonCategory = options.looseCRe2e2_photonCategory
looseCRe3ge2_photonCategory = options.looseCRe3ge2_photonCategory


gROOT.SetBatch(True)

if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"
if tight_photonCategory:          
	fileDir  = "histograms_%s/%s/hists_tight/"%(selYear, channel)
	plotDirectory = "pho_tightplots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}#geq1"

if looseCRge2ge0_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRge2ge0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge2ge0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq2, N_{b}#geq0"

###
if looseCRe2e0_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe2e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=0"

if looseCRe2e1_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe2e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=1"

if looseCRe3e0_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe3e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=0"

if looseCRge4e0_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRge4e0/"%(selYear, channel)
	plotDirectory = "pho_looseCRge4e0plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}#geq4, N_{b}=0"

if looseCRe3e1_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe3e1/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3e1plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}=1"

if looseCRe2e2_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe2e2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe2e2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=2, N_{b}=2"

if looseCRe3ge2_photonCategory:  
	fileDir  = "histograms_%s/%s/hists_looseCRe3ge2/"%(selYear, channel)
	plotDirectory = "pho_looseCRe3ge2plots_%s_%s/"%(channel, selYear)
	regionText = "N_{j}=3, N_{b}#geq2"

###

if not os.path.exists(plotDirectory):
	os.mkdir(plotDirectory)

gStyle.SetOptStat(0)
MCSamplelist = ['TTGamma', 'TTbar', 'TGJets','SingleTop', 'WJets', 'ZJets', 'WGamma','ZGamma','Diboson','TTV','GJets',"QCD"]
category = {"GenuinePhoton":kYellow, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kGreen }
file = {}
rebin = 5

histName    = "phosel_LeadingPhotonEt_%s_%s"
histNameData= "phosel_LeadingPhotonEt_%s"

# histName    = "phosel_noCut_SIEIE_%s_%s"
# histNameData= "phosel_noCut_SIEIE_%s"

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
	for sample in MCSamplelist:
		if finalState == 'Ele' and sample == 'QCD': sample = 'QCDEle'
		if finalState == 'Mu'  and sample == 'QCD': sample = 'QCDMu'
		file[sample] = TFile('%s%s.root'%(fileDir,sample),'read')
		tempHist = file[sample].Get(histName%(item,sample))
		if summedHist[item] is None:
			summedHist[item] = tempHist.Clone(item)
			summedHist[item].SetDirectory(0)
		else:
			summedHist[item].Add(tempHist)

for ih in summedHist:
	summedHist[ih].Rebin(rebin)
	summedHist[ih].SetLineColor(category[ih])
	summedHist[ih].SetFillColor(category[ih])

category = {"GenuinePhoton":kYellow, "MisIDEle":kRed, "HadronicPhoton":kBlue, "HadronicFake":kOrange }
stack = THStack()
stack.Add(summedHist['HadronicPhoton'])
stack.Add(summedHist['HadronicFake'])
stack.Add(summedHist['MisIDEle'])
stack.Add(summedHist['GenuinePhoton'])
stack.SetTitle('Photon Category;;Events/%i GeV '%rebin)



#############
text1 = TPaveText(0.75,.92,.9,1,"NDC")
text1.SetTextColor(kBlack)
text1.SetFillColor(0)
text1.SetTextSize(0.04)
text1.SetTextFont(42)
if selYear == '2016':text1.AddText('35.92 fb^{-1}(13TeV)')
if selYear == '2017':text1.AddText('41.53 fb^{-1}(13TeV)')
if selYear == '2018':text1.AddText('59.74 fb^{-1}(13TeV)')
###################
text = TPaveText(0.5,.7,.7,.9,"NDC")
text.SetTextColor(kBlack)
text.SetFillColor(0)
text.SetTextSize(0.04)
text.SetTextFont(42)
text.AddText('CMS')
text.AddText('Preliminary')
text.AddText(channelText) 
text.AddText(regionText)
##########################
H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
#################
errorband=stack.GetStack().Last().Clone("error")
errorband.Sumw2()
errorband.SetLineColor(kBlack)
errorband.SetFillColor(kBlack)
errorband.SetFillStyle(3245)
errorband.SetMarkerSize(0)

# legendR.AddEntry(errorband,"Uncertainty","f")
#############################
legend = TLegend(0.7,0.7,.88,.9)
legend.AddEntry(dataHist, "Data", 'pe')
legend.AddEntry(summedHist['GenuinePhoton'],'GenuinePhoton','f')
legend.AddEntry(summedHist['MisIDEle'],'MisIDEle','f')
legend.AddEntry(summedHist['HadronicFake'],'HadronicFake','f')
legend.AddEntry(summedHist['HadronicPhoton'],'HadronicPhoton','f')
legend.AddEntry(errorband,"Uncertainty","f")

legend.SetBorderSize(3)
legend.SetFillColor(0)

canvas = TCanvas('c1','c1',W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(0)

pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
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
pad1.Draw();             
pad1.cd(); 
pad1.SetLogy()              
stack.Draw('hist')
dataHist.Draw('e1,X0,same')
legend.Draw('same')
text.Draw('same')
text1.Draw('same')
stack.GetHistogram().GetXaxis().SetTickLength(0)
stack.GetHistogram().GetXaxis().SetLabelOffset(999)

pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
pad2.SetLeftMargin( L/W )
pad2.SetRightMargin( R/W )
pad2.SetTopMargin( (padOverlap+.08)/(padRatio+padOverlap) )
pad2.SetBottomMargin( 0.19 )
pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetBorderMode(0)
pad2.SetFrameFillStyle(0)
pad2.SetFrameBorderMode(0)
pad2.SetTickx(0)
pad2.SetTicky(0)
pad2.Draw()
pad2.cd()

ratioHist = dataHist.Clone("ratioHist")
ratioHist.SetLineColor(kBlack)
ratioHist.SetMinimum(0.8)  
ratioHist.SetMaximum(1.2) 
ratioHist.Sumw2()
ratioHist.SetStats(0)     
h = stack.GetHistogram().Clone('h') 
ratioHist.Divide(h)
ratioHist.SetMarkerStyle(8)
ratioHist.SetTitle(';Photon Et;Data/MC')
ratioHist.SetLabelSize(0.085,'xy')
ratioHist.SetTitleSize(0.09,'xy')
ratioHist.SetTitleOffset(0.48,'y')
ratioHist.SetTitleOffset(1,'x')
ratioHist.SetNdivisions(2,'y')
ratioHist.SetNdivisions(12,'x')

ratioHist.Draw('e,x0') 
errorband.Draw('e4,same')
canvas.SaveAs("%s%s_pt.root"%(plotDirectory,plotDirectory[:-1]))
canvas.SaveAs("%s%s_pt.pdf" %(plotDirectory,plotDirectory[:-1]))
canvas.Close()
# gApplication.Run()
