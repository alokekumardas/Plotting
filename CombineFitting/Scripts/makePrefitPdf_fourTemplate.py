import ROOT
import os
import sys
from optparse import OptionParser
import CMS_lumi

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01

parser = OptionParser()
parser.add_option("-y", "--year", dest="Year", default="",type='str',
                     help="Specify which year 2016, 2017 or 2018?" )
                     
parser.add_option("-c", "--channel", dest="channel", default="",type='str',
					help="Specify which channel Mu or Ele? default is Mu" )                     

(options, args) = parser.parse_args()
finalState = options.channel
if finalState=='Mu':
	channel = 'mu'
	channelText = "#mu+jets"
if finalState=='Ele':
	channel = 'ele'
	channelText = "e+jets"
selYear = options.Year
print selYear
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()
if selYear == "2016":
	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"
	if finalState == "Ele":
		folderName = [
		'fourTemplate_tightplots_ele_2016/',
		'fourTemplate_looseCRge2ge0plots_ele_2016/',
		'fourTemplate_looseCRge2e0plots_ele_2016/',
		'fourTemplate_looseCRe3ge2plots_ele_2016/',
		'fourTemplate_looseCRge4e0plots_ele_2016/',
		'fourTemplate_looseCRe2e1plots_ele_2016/',
		'fourTemplate_looseCRe2e0plots_ele_2016/',
		'fourTemplate_looseCRe3e1plots_ele_2016/',
		'fourTemplate_looseCRe2e2plots_ele_2016/',
		'fourTemplate_looseCRe3e0plots_ele_2016/'
		]
	elif finalState == "Mu":
		folderName = [
		'fourTemplate_tightplots_mu_2016/',
		'fourTemplate_looseCRge2ge0plots_mu_2016/',
		'fourTemplate_looseCRge2e0plots_mu_2016/',
		'fourTemplate_looseCRe3ge2plots_mu_2016/',
		'fourTemplate_looseCRge4e0plots_mu_2016/',
		'fourTemplate_looseCRe2e1plots_mu_2016/',
		'fourTemplate_looseCRe2e0plots_mu_2016/',
		'fourTemplate_looseCRe3e1plots_mu_2016/',
		'fourTemplate_looseCRe2e2plots_mu_2016/',
		'fourTemplate_looseCRe3e0plots_mu_2016/'
		]
	else: print "Wrong channel name!!"


elif selYear == '2017':
	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"
	if finalState == "Ele":
		folderName = [
		'fourTemplate_tightplots_ele_2017/',
		'fourTemplate_looseCRge2ge0plots_ele_2017/',
		'fourTemplate_looseCRge2e0plots_ele_2017/',
		'fourTemplate_looseCRe3ge2plots_ele_2017/',
		'fourTemplate_looseCRge4e0plots_ele_2017/',
		'fourTemplate_looseCRe2e1plots_ele_2017/',
		'fourTemplate_looseCRe2e0plots_ele_2017/',
		'fourTemplate_looseCRe3e1plots_ele_2017/',
		'fourTemplate_looseCRe2e2plots_ele_2017/',
		'fourTemplate_looseCRe3e0plots_ele_2017/'
		]
	elif finalState == "Mu":
		folderName = [
		'fourTemplate_tightplots_mu_2017/',
		'fourTemplate_looseCRge2ge0plots_mu_2017/',
		'fourTemplate_looseCRge2e0plots_mu_2017/',
		'fourTemplate_looseCRe3ge2plots_mu_2017/',
		'fourTemplate_looseCRge4e0plots_mu_2017/',
		'fourTemplate_looseCRe2e1plots_mu_2017/',
		'fourTemplate_looseCRe2e0plots_mu_2017/',
		'fourTemplate_looseCRe3e1plots_mu_2017/',
		'fourTemplate_looseCRe2e2plots_mu_2017/',
		'fourTemplate_looseCRe3e0plots_mu_2017/'
		]
	else: print "Wrong channel name!!"


elif selYear == '2018':
	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"
	if finalState == "Ele":
		folderName = [
		'fourTemplate_tightplots_ele_2018/',
		'fourTemplate_looseCRge2ge0plots_ele_2018/',
		'fourTemplate_looseCRge2e0plots_ele_2018/',
		'fourTemplate_looseCRe3ge2plots_ele_2018/',
		'fourTemplate_looseCRge4e0plots_ele_2018/',
		'fourTemplate_looseCRe2e1plots_ele_2018/',
		'fourTemplate_looseCRe2e0plots_ele_2018/',
		'fourTemplate_looseCRe3e1plots_ele_2018/',
		'fourTemplate_looseCRe2e2plots_ele_2018/',
		'fourTemplate_looseCRe3e0plots_ele_2018/'
		]
	elif finalState == "Mu":
		folderName = [
		'fourTemplate_tightplots_mu_2018/',
		'fourTemplate_looseCRge2ge0plots_mu_2018/',
		'fourTemplate_looseCRge2e0plots_mu_2018/',
		'fourTemplate_looseCRe3ge2plots_mu_2018/',
		'fourTemplate_looseCRge4e0plots_mu_2018/',
		'fourTemplate_looseCRe2e1plots_mu_2018/',
		'fourTemplate_looseCRe2e0plots_mu_2018/',
		'fourTemplate_looseCRe3e1plots_mu_2018/',
		'fourTemplate_looseCRe2e2plots_mu_2018/',
		'fourTemplate_looseCRe3e0plots_mu_2018/'
		]
	else: print "Wrong channel name!!"

else:
	print 'select the year!'
	sys.exit()


ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)

from Style import *
thestyle = Style()
thestyle.SetStyle()

ROOT.gROOT.ForceStyle()

for i in folderName:
	myfile = ROOT.TFile('MyFiles/'+i+'fourTemplate_%s_Prefit.root'%(channel),'read')
	
	MisIDEle               = myfile.Get("MisIDEle").Clone()   
	ZgammaBkgPhoton        = myfile.Get("ZgammaBkgPhoton").Clone()   
	WgammaBkgPhoton        = myfile.Get("WgammaBkgPhoton").Clone()   
	OtherSampleBkgPhoton   = myfile.Get("OtherSampleBkgPhoton").Clone()   
	Total                  = myfile.Get("Total").Clone()   
	myData                 = myfile.Get("myData").Clone()   


	MisIDEle.SetLineColor(ROOT.kRed)               
	ZgammaBkgPhoton.SetLineColor(ROOT.kOrange)        
	WgammaBkgPhoton.SetLineColor(ROOT.kBlue)        
	OtherSampleBkgPhoton.SetLineColor(ROOT.kGreen+1)   
	Total.SetLineColor(ROOT.kGray+3)                  
	myData.SetLineColor(ROOT.kBlack)                 

	MisIDEle.SetLineWidth(2)
	ZgammaBkgPhoton.SetLineWidth(2)
	WgammaBkgPhoton.SetLineWidth(2)
	OtherSampleBkgPhoton.SetLineWidth(2)
	Total.SetLineWidth(2)
	myData.SetLineWidth(2)

	myData.SetMarkerStyle(8)
   
	H = 600;
	W = 800;
	T = 0.08*H
	B = 0.12*H
	L = 0.12*W
	R = 0.1*W

	legendHeightPer = 0.04

	legendStart = 0.6
	legendEnd = 0.97-(R/W)

	# legend = ROOT.TLegend(legendStart, 1-T/H-0.01 - legendHeightPer*(9), legendEnd, 0.99-(T/H)-0.01)
	legend = ROOT.TLegend(.15, .5, .35, .8)
	legend.SetBorderSize(0)
	legend.SetFillColor(0)

	ROOT.TGaxis.SetMaxDigits(3)
	canvasRatio = ROOT.TCanvas('c1Ratio','c1Ratio',W,H)
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
	pad1 = ROOT.TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
	pad2 = ROOT.TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
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

	oneLine = ROOT.TF1("oneline","1",-9e9,9e9)
	oneLine.SetLineColor(ROOT.kBlack)
	oneLine.SetLineWidth(1)
	oneLine.SetLineStyle(2)

	# text = ROOT.TPaveText(0.35,.75,0.45,0.85,"NDC")
	# text.SetTextColor(ROOT.kBlack)
	# text.SetFillColor(0)
	# text.SetTextSize(0.04)
	# text.SetTextFont(42)

	maxVal = max(myData.GetMaximum(),Total.GetMaximum())
	minVal = 1
	minVal = max(myData.GetMinimum(),0)
	myData.SetMaximum(1.25*maxVal)
	myData.SetMinimum(0)

	errorband=Total.Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(ROOT.kBlack)
	errorband.SetFillColor(ROOT.kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)

	legend.AddEntry(myData,'Data','pe')
	legend.AddEntry(MisIDEle, 'MisIDEle','f')
	legend.AddEntry(ZgammaBkgPhoton,'ZgammaBkgPhoton','f')
	legend.AddEntry(WgammaBkgPhoton,'WgammaBkgPhoton','f')
	legend.AddEntry(OtherSampleBkgPhoton,'OtherSampleBkgPhoton','f')
	legend.AddEntry(Total,'Total','f')

	legend.AddEntry(errorband,"Uncertainty","f")

	pad1.cd()

	myData.Draw('e1,X0')
	MisIDEle.Draw("hist,same")
	ZgammaBkgPhoton.Draw("hist,same")
	WgammaBkgPhoton.Draw("hist,same")
	OtherSampleBkgPhoton.Draw("hist,same")
	Total.Draw("hist,same")
	# text.Draw("same")
	legend.Draw("same")
	myData.GetXaxis().SetTitle('')
	myData.GetXaxis().SetLabelSize(0)
	myData.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	myData.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	myData.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	myData.SetTitle(';;Events/2 GeV ')
	# MySumHist.GetXaxis().SetRangeUser(selectionRange1,selectionRange2)

	# CMS_lumi.channelText = 'e+jets'
	CMS_lumi.writeChannelText = True
	CMS_lumi.CMS_lumi(pad1, 4, 11)

	ratio = myData.Clone("temp")
	temp = Total.Clone("temp")
	for i_bin in range(1,temp.GetNbinsX()+1):
		temp.SetBinError(i_bin,0.)
	ratio.Divide(temp)
	    
	ratio.SetTitle('')
	ratio.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize()/(padRatio+padOverlap))
	ratio.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize()/(padRatio+padOverlap))
	ratio.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))

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
	ratio.GetXaxis().SetTitle('m_{e,#gamma} GeV')
	ratio.GetYaxis().SetTitle("Data/MC")
	# ratio.GetXaxis().SetRangeUser(selectionRange1,selectionRange2)
	pad2.cd()
	CMS_lumi.CMS_lumi(pad2, 4, 11)

	ratio.SetMarkerStyle(myData.GetMarkerStyle())
	ratio.SetMarkerSize(myData.GetMarkerSize())
	ratio.SetLineColor(myData.GetLineColor())
	ratio.SetLineWidth(myData.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")

	canvasRatio.Update()
	canvasRatio.RedrawAxis()

	canvasRatio.Print("MyFiles/%s%s_%s_Prefit.pdf" %(i,'fourTemplate',channel))
	canvasRatio.Close()
	myfile.Close()


