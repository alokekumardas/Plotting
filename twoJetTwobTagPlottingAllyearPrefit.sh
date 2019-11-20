for year in 2016 2017 2018
do
	python makePlots_twoJetTwoTag.py -y $year -c Ele --looseCRe3e0     --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
	python makePlots_twoJetTwoTag.py -y $year -c Mu  --looseCRe3e0     --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
	
	python makePlots_twoJetTwoTag.py -y $year -c Ele --looseCRe2e0     --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &
	python makePlots_twoJetTwoTag.py -y $year -c Mu  --looseCRe2e0     --useQCDMC  --plot phosel_jet1Pt --plot phosel_WtransMass &


done

wait
echo "Done making prefit CRe2e2 Plots!!"


