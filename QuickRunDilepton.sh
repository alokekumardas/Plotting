
#!/bin/bash

# --makeNabinPlots

python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s TTbar     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s TGJets    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s WJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s ZJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s WGamma    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s Diboson   --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s SingleTop --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s TTV       --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s QCDEle    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s GJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiEle --looseCRge2e0  -s DataEle   --dilepmassPlots &

python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s TTGamma   --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s TTbar     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s TGJets    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s WJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s ZJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s WGamma    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s ZGamma    --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s Diboson   --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s SingleTop --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s TTV       --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s QCDMu     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s GJets     --dilepmassPlots &
python makeHistograms.py -y 2016 -c DiMu  --looseCRge2e0  -s DataMu    --dilepmassPlots &
