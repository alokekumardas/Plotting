for year in 2016 2017 2018
do
python makePlots.py -y $year -c Ele --tight     --useQCDMC  --makeSignalRegionPlots &
python makePlots.py -y $year -c Mu  --tight     --useQCDMC  --makeSignalRegionPlots &
done

wait
echo "Done making prefit signal region Plots!!"



