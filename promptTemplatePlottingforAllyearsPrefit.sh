for year in 2016 2017 2018
do
python makePlot_signal_prompt.py -y $year -c Ele --tight_promptTemplate --useQCDMC  &
python makePlot_signal_prompt.py -y $year -c Mu  --tight_promptTemplate --useQCDMC  &
done

wait
echo "Done making prefit signal region M3 photon sevenTemplate Plots!!"

