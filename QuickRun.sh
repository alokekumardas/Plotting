
#!/bin/bash

# --makeNabinPlots



#echo "Ele channel ******************************************"
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTGamma   --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTbar     --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TGJets    --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WJets     --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZJets     --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WGamma    --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZGamma    --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s Diboson   --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s SingleTop --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTV       --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s QCDEle    --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s GJets     --makePlotsForSF & 
#python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s DataEle   --makePlotsForSF & 
#echo "Mu channel ******************************************"
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTGamma   --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTbar     --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TGJets    --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WJets     --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZJets     --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WGamma    --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZGamma    --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s Diboson   --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s SingleTop --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTV       --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s QCDMu     --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s GJets     --makePlotsForSF &
#python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s DataMu    --makePlotsForSF &


echo "Ele channel ******************************************"
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTGamma   --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTbar     --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TGJets    --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WJets     --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZJets     --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WGamma    --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZGamma    --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s Diboson   --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s SingleTop --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTV       --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s QCDEle    --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s GJets     --syst BTagSF --level up --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s DataEle   --syst BTagSF --level up --makePlotsForSF & 
echo "Mu channel ******************************************"
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTGamma   --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTbar     --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TGJets    --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WJets     --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZJets     --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WGamma    --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZGamma    --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s Diboson   --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s SingleTop --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTV       --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s QCDMu     --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s GJets     --syst BTagSF --level up --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s DataMu    --syst BTagSF --level up --makePlotsForSF &

echo "Ele channel ******************************************"
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTGamma   --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTbar     --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TGJets    --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WJets     --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZJets     --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s WGamma    --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s ZGamma    --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s Diboson   --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s SingleTop --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s TTV       --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s QCDEle    --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s GJets     --syst BTagSF --level down --makePlotsForSF & 
python makeHistograms.py -y 2016 -c Ele --looseCRge2e0 -s DataEle   --syst BTagSF --level down --makePlotsForSF & 
echo "Mu channel ******************************************"
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTGamma   --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTbar     --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TGJets    --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WJets     --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZJets     --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s WGamma    --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s ZGamma    --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s Diboson   --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s SingleTop --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s TTV       --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s QCDMu     --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s GJets     --syst BTagSF --level down --makePlotsForSF &
python makeHistograms.py -y 2016 -c Mu  --looseCRge2e0 -s DataMu    --syst BTagSF --level down --makePlotsForSF &

