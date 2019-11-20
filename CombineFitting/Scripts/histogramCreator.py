import ROOT

bkgHist1 = ROOT.TH1F('background1','',5,0,5)
bkgHist2 = ROOT.TH1F('background2','',5,0,5)
signalHist = ROOT.TH1F('signal','',5,0,5)
dataHist = ROOT.TH1F('data_obs','',5,0,5) # seems data_obs is necessary

for i in xrange(5):
	bkgHist1.SetBinContent(i+1,100-20*(i))
	bkgHist2.SetBinContent(i+1,30)
	signalHist.SetBinContent(i+1,20*(i+1))

#dataHist.Add(bkgHist1,2)
dataHist.Add(bkgHist2,3) # solving parallel lines
dataHist.Add(signalHist,4)

file    = ROOT.TFile('mytest-input.root','recreate')
bkgHist1.Write()
bkgHist2.Write()
signalHist.Write()
dataHist.Write()
file.Close()

# shapes data_obs        trial mytest-input.root  data
# shapes signal  	       trial mytest-input.root	signal
# shapes background      trial mytest-input.root	background




# python data/tutorials/shapes/histogramCreator.py
# wait
# text2workspace.py data/tutorials/shapes/ttgamma.txt
# wait
# python test/printWorkspaceNormalisations.py data/tutorials/shapes/ttgamma.root
# wait
# echo "Done..."

# combine -M FitDiagnostics data/tutorials/shapes/ttgamma.txt

# echo "Done......."








# /uscms_data/d3/npoudyal/TTGammaSemiLeptonic13TeV/CMSSW_10_2_14/src/HiggsAnalysis/CombinedLimit/myfiles
# bkg.root
# signal.root
