for year in 2016 2017 2018
do
python makePlot_twoJetTwoTag_split.py -y $year -c Ele --looseCRe2e2_sevenTemplate --useQCDMC --postfitPlots &
python makePlot_twoJetTwoTag_split.py -y $year -c Mu  --looseCRe2e2_sevenTemplate --useQCDMC --postfitPlots &
done

wait
echo "done"
