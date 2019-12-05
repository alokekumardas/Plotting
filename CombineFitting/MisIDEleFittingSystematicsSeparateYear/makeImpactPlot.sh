text2workspace.py  datacard_CR123_2016.txt
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --doInitialFit --robustFit 1
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 --robustFit 1 --doFits
combineTool.py -M Impacts -d datacard_CR123_2016.root -m 125 -o impacts.json
plotImpacts.py -i impacts.json -o impacts


