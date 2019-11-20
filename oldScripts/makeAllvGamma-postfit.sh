declare -a StringYear=("2016" "2017" "2018")
for year in  ${StringYear[@]}; do

python makePlots_VGpostfit.py -y $year -c Mu  --tight           --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRge2ge0   --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRge2e0    --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe2e0     --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe3e0     --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRge4e0    --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe2e1     --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe3e1     --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe2e2     --useQCDMC --postfitplotvGamma  &
python makePlots_VGpostfit.py -y $year -c Mu  --looseCRe3ge2    --useQCDMC --postfitplotvGamma  &

done
wait

echo "All processes done!"


