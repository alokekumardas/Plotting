python makePlots_syst.py -y $1 -c Ele --tight           --useQCDMC  --makePlotsForSF &      
python makePlots_syst.py -y $1 -c Mu  --tight           --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRge2ge0   --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRge2ge0   --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRge2e0    --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRge2e0    --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe2e0     --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe2e0     --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe3e0     --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe3e0     --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRge4e0    --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRge4e0    --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe2e1     --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe2e1     --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe3e1     --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe3e1     --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe2e2     --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe2e2     --useQCDMC  --makePlotsForSF &

python makePlots_syst.py -y $1 -c Ele --looseCRe3ge2    --useQCDMC  --makePlotsForSF &
python makePlots_syst.py -y $1 -c Mu  --looseCRe3ge2    --useQCDMC  --makePlotsForSF &

wait
echo "All systematic processes done!"
