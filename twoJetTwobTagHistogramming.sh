python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s QCDEle    --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s DataEle   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTGamma   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTbar     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TGJets    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZGamma    --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s Diboson   --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s SingleTop --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTV       --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s QCDMu     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s GJets     --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s DataMu    --makePlotsForSF &
wait
echo "Done making CRe2e2 histograms!!"


