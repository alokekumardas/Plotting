for year in 2016 2017 2018
do
	python makePlots_twoJetTwoTag_postfit.py -y $year -c Ele --looseCRe2e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
	python makePlots_twoJetTwoTag_postfit.py -y $year -c Mu  --looseCRe2e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &

	python makePlots_twoJetTwoTag_postfit.py -y $year -c Ele --looseCRe3e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
	python makePlots_twoJetTwoTag_postfit.py -y $year -c Mu  --looseCRe3e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
done

wait
echo "Done making postfit CRe2e2 Plots!!"

#python makePlots_twoJetTwoTag_postfit.py -y 2018 -c Ele --looseCRe2e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
#python makePlots_twoJetTwoTag_postfit.py -y 2018 -c Mu  --looseCRe2e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &

#python makePlots_twoJetTwoTag_postfit.py -y 2018 -c Ele --looseCRe3e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
#python makePlots_twoJetTwoTag_postfit.py -y 2018 -c Mu  --looseCRe3e0  --postfitplot   --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &



