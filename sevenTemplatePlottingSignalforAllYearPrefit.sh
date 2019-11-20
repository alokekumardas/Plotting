for year in 2016 2017 2018
do
python makePlot_twoJetTwoTag_split.py -y $year -c Ele --looseCRe2e2_sevenTemplate --useQCDMC  &
python makePlot_twoJetTwoTag_split.py -y $year -c Mu  --looseCRe2e2_sevenTemplate --useQCDMC  &
done

wait
echo "Done making prefit signal region M3 photon sevenTemplate Plots!!"

