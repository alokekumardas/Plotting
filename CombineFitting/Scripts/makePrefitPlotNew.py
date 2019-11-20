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

(options, args) = parser.parse_args()

selYear = options.Year
if selYear=="":
	print "Specify which year 2016, 2017 or 2018?"
	sys.exit()
if selYear == '2016':
	folderName = [
	'pho_tightplots_ele_2016/',
	'pho_looseCRge2ge0plots_ele_2016/',
	'pho_looseCRge2e0plots_ele_2016/',
	'pho_looseCRe3ge2plots_ele_2016/',
	'pho_looseCRge4e0plots_ele_2016/',
	'pho_looseCRe2e1plots_ele_2016/',
	'pho_looseCRe2e0plots_ele_2016/',
	'pho_looseCRe3e1plots_ele_2016/',
	'pho_looseCRe2e2plots_ele_2016/',
	'pho_looseCRe3e0plots_ele_2016/'
	]
	CMS_lumi.lumi_13TeV = "35.92 fb^{-1}"


elif selYear == '2017':
	folderName = [
	'pho_tightplots_ele_2017/',
	'pho_looseCRge2ge0plots_ele_2017/',
	'pho_looseCRge2e0plots_ele_2017/',
	'pho_looseCRe3ge2plots_ele_2017/',
	'pho_looseCRge4e0plots_ele_2017/',
	'pho_looseCRe2e1plots_ele_2017/',
	'pho_looseCRe2e0plots_ele_2017/',
	'pho_looseCRe3e1plots_ele_2017/',
	'pho_looseCRe2e2plots_ele_2017/',
	'pho_looseCRe3e0plots_ele_2017/'
	]
	CMS_lumi.lumi_13TeV = "41.53 fb^{-1}"


elif selYear=='2018':
	folderName = [
	'pho_tightplots_ele_2018/',
	'pho_looseCRge2ge0plots_ele_2018/',
	'pho_looseCRge2e0plots_ele_2018/',
	'pho_looseCRe3ge2plots_ele_2018/',
	'pho_looseCRge4e0plots_ele_2018/',
	'pho_looseCRe2e1plots_ele_2018/',
	'pho_looseCRe2e0plots_ele_2018/',
	'pho_looseCRe3e1plots_ele_2018/',
	'pho_looseCRe2e2plots_ele_2018/',
	'pho_looseCRe3e0plots_ele_2018/'
	]
	CMS_lumi.lumi_13TeV = "59.74 fb^{-1}"

else:
	print 'select the year!'

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)


from Style import *
thestyle = Style()
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

# selectionRange1=80
# selectionRange2=100

for i in folderName:
	myfile = ROOT.TFile('MyFiles/'+i+'myMisIDEle_Prefit.root','read')
	
	MisIDEle   = myfile.Get("myMisIDEle").Clone()   
	OtherHist  = myfile.Get("myBackground").Clone()
	MyDataHist = myfile.Get("myData").Clone() 
	MySumHist  = myfile.Get("myTotal").Clone()

	MisIDEle.SetLineColor(ROOT.kRed)
	OtherHist.SetLineColor(ROOT.kBlue)
	MyDataHist.SetLineColor(ROOT.kBlack)
	MySumHist.SetLineColor(ROOT.kGreen+1)

	MisIDEle.  SetLineWidth(2)
	OtherHist. SetLineWidth(2)
	MyDataHist.SetLineWidth(2)
	MySumHist. SetLineWidth(2)

	MyDataHist.SetMarkerStyle(8)

	# MisIDEle.SetFillColor(ROOT.kRed)
	# OtherHist.SetFillColor(ROOT.kBlue)
	# MyDataHist.SetFillColor(ROOT.kBlack)
	# MySumHist.SetFillColor(ROOT.kGreen+1)
    
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

	maxVal = max(MyDataHist.GetMaximum(),MySumHist.GetMaximum())
	minVal = 1
	minVal = max(MyDataHist.GetMinimum(),0)
	MyDataHist.SetMaximum(1.25*maxVal)
	MyDataHist.SetMinimum(0)

	errorband=MySumHist.Clone("error")
	errorband.Sumw2()
	errorband.SetLineColor(ROOT.kBlack)
	errorband.SetFillColor(ROOT.kBlack)
	errorband.SetFillStyle(3245)
	errorband.SetMarkerSize(0)

	legend.AddEntry(MyDataHist,'Data','pe')
	legend.AddEntry(MisIDEle,'MisIDEle','f')
	legend.AddEntry(OtherHist,'Other','f')
	legend.AddEntry(MySumHist,'Sum','f')
	legend.AddEntry(errorband,"Uncertainty","f")

	pad1.cd()

	MyDataHist.Draw('e1,X0')
	MisIDEle. Draw("hist,same")
	OtherHist.Draw("hist,same")
	MySumHist.Draw("hist,same")
	# text.Draw("same")
	legend.Draw("same")
	MyDataHist.GetXaxis().SetTitle('')
	MyDataHist.GetXaxis().SetLabelSize(0)
	MyDataHist.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
	MyDataHist.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
	MyDataHist.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
	MyDataHist.SetTitle(';;Events/2 GeV ')
	# MySumHist.GetXaxis().SetRangeUser(selectionRange1,selectionRange2)

	# CMS_lumi.channelText = 'e+jets'
	CMS_lumi.writeChannelText = True
	CMS_lumi.CMS_lumi(pad1, 4, 11)

	ratio = MyDataHist.Clone("temp")
	temp = MySumHist.Clone("temp")
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

	ratio.SetMarkerStyle(MyDataHist.GetMarkerStyle())
	ratio.SetMarkerSize(MyDataHist.GetMarkerSize())
	ratio.SetLineColor(MyDataHist.GetLineColor())
	ratio.SetLineWidth(MyDataHist.GetLineWidth())
	ratio.Draw('e,x0')
	errorbandRatio = errorband.Clone("errorRatio")
	errorbandRatio.Divide(temp)
	errorbandRatio.Draw('e2,same')
	oneLine.Draw("same")

	canvasRatio.Update()
	canvasRatio.RedrawAxis()

	canvasRatio.Print("MyFiles/%s%s_Prefit.pdf" %(i,'myMisIDEle'))
	canvasRatio.Close()
	myfile.Close()


