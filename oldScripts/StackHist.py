
import ROOT



f1 = ROOT.TFile.Open('histograms/ele/hists_tight/TTGamma.root', 'read')
hist1 = f1.Get('presel_jet1Pt_TTGamma')
hist1.SetFillColor(40)
hist1.Rebin(10)

f2 = ROOT.TFile.Open('histograms/ele/hists_tight/TTbar.root', 'read')
hist2 = f2.Get('presel_jet1Pt_TTbar')
hist2.SetFillColor(2)
hist2.Rebin(10)

f3 = ROOT.TFile.Open('histograms/ele/hists_tight/TGJets.root', 'read')
hist3 = f3.Get('presel_jet1Pt_TGJets')
hist3.SetFillColor(3)
hist3.Rebin(10)

f4 = ROOT.TFile.Open('histograms/ele/hists_tight/WJets.root', 'read')
hist4 = f4.Get('presel_jet1Pt_WJets')
hist4.SetFillColor(4)
hist4.Rebin(10)

f5 = ROOT.TFile.Open('histograms/ele/hists_tight/ZJets.root', 'read')
hist5 = f5.Get('presel_jet1Pt_ZJets')
hist5.SetFillColor(5)
hist5.Rebin(10)

#f6 = ROOT.TFile.Open('histograms/ele/hists_tight/ZJets_NLO.root', 'read')
#hist6 = f6.Get('presel_jet1Pt_ZJets_NLO')
#hist6.SetFillColor(6)

f7 = ROOT.TFile.Open('histograms/ele/hists_tight/WGamma.root', 'read')
hist7 = f7.Get('presel_jet1Pt_WGamma')
hist7.SetFillColor(7)
hist7.Rebin(10)

f8 = ROOT.TFile.Open('histograms/ele/hists_tight/ZGamma.root', 'read')
hist8 = f8.Get('presel_jet1Pt_ZGamma')
hist8.SetFillColor(8)
hist8.Rebin(10)

f9 = ROOT.TFile.Open('histograms/ele/hists_tight/Diboson.root', 'read')
hist9 = f9.Get('presel_jet1Pt_Diboson')
hist9.SetFillColor(9)
hist9.Rebin(10)

f10 = ROOT.TFile.Open('histograms/ele/hists_tight/SingleTop.root', 'read')
hist10 = f10.Get('presel_jet1Pt_SingleTop')
hist10.SetFillColor(40)
hist10.Rebin(10)

#f11 = ROOT.TFile.Open('histograms/ele/hists_tight/ST-tch.root', 'read')
#hist11 = f11.Get('presel_jet1Pt_ST-tch')
#hist11.SetFillColor(11)

#f12 = ROOT.TFile.Open('histograms/ele/hists_tight/ST-sch.root', 'read')
#hist12 = f12.Get('presel_jet1Pt_ST-sch')
#hist12.SetFillColor(12)

#f13 = ROOT.TFile.Open('histograms/ele/hists_tight/ST-tW.root', 'read')
#hist13 = f13.Get('presel_jet1Pt_ST-tW')
#hist13.SetFillColor(13)

f14 = ROOT.TFile.Open('histograms/ele/hists_tight/TTV.root', 'read')
hist14 = f14.Get('presel_jet1Pt_TTV')
hist14.SetFillColor(14)
hist14.Rebin(10)

f15 = ROOT.TFile.Open('histograms/ele/hists_tight/QCDEle.root', 'read')
hist15 = f15.Get('presel_jet1Pt_QCDEle')
hist15.SetFillColor(15)
hist15.Rebin(10)

f16 = ROOT.TFile.Open('histograms/ele/hists_tight/GJets.root', 'read')
hist16 = f16.Get('presel_jet1Pt_GJets')
hist16.SetFillColor(16)
hist16.Rebin(10)

f17 = ROOT.TFile.Open('histograms/ele/hists_tight/DataEle.root', 'read')
hist17 = f17.Get('presel_jet1Pt_DataEle')
hist17.SetMarkerStyle(20)
hist17.SetMarkerSize(1.05)
hist17.Rebin(10)

hs = ROOT.THStack()
hs.Add(hist2) # red = tt
hs.Add(hist3)
hs.Add(hist4)
hs.Add(hist5)
hs.Add(hist7)
hs.Add(hist8)
hs.Add(hist9)
hs.Add(hist10)
hs.Add(hist14)
hs.Add(hist15)
hs.Add(hist16)
hs.Add(hist1) # white = ttgamma

c =ROOT. TCanvas()
# c.SetLogy()
hs.Draw('hists')
hist17.Draw('same E1')

ROOT.gApplication.Run()


