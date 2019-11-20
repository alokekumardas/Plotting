#!/bin/bash



python makeHistograms.py -y $1 -c Ele --tight -s TTGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTbar      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TGJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WGamma     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZGamma     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s Diboson    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s SingleTop  --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTV        --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s QCDEle     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s GJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s DataEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTbar      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TGJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WGamma     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZGamma     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s Diboson    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s SingleTop  --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTV        --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s QCDMu      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s GJets      --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s DataMu     --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s QCDEle    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s DataEle   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTGamma   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTbar     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TGJets    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZGamma    --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s Diboson   --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s SingleTop --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTV       --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s QCDMu     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s GJets     --syst BTagSF_l --level up --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s DataMu    --syst BTagSF_l --level up --makePlotsForSF &
wait

echo "up systematic is processes done!"

wait

python makeHistograms.py -y $1 -c Ele --tight -s TTGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTbar      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TGJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s WGamma     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s ZGamma     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s Diboson    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s SingleTop  --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s TTV        --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s QCDEle     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s GJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --tight -s DataEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTbar      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TGJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s WGamma     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s ZGamma     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s Diboson    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s SingleTop  --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s TTV        --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s QCDMu      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s GJets      --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --tight -s DataMu     --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2ge0 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2ge0 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge2e0  -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge2e0  -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e0 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e0 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e0 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e0 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRge4e0 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRge4e0 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e1 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e1 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3e1 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3e1 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe2e2 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe2e2 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &

wait

python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s QCDEle    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Ele --looseCRe3ge2 -s DataEle   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTGamma   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTbar     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TGJets    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s WGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s ZGamma    --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s Diboson   --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s SingleTop --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s TTV       --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s QCDMu     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s GJets     --syst BTagSF_l --level down --makePlotsForSF &
python makeHistograms.py -y $1 -c Mu  --looseCRe3ge2 -s DataMu    --syst BTagSF_l --level down --makePlotsForSF &
wait

echo "Up and Down both are done."

