
python makePrefitPdf_fourTemplate_Zjets.py -y 2016 -c DiEle
python makePrefitPdf_fourTemplate_Zjets.py -y 2016 -c DiMu

python makePrefitPdf_fourTemplate_Zjets.py -y 2017 -c DiEle
python makePrefitPdf_fourTemplate_Zjets.py -y 2017 -c DiMu

python makePrefitPdf_fourTemplate_Zjets.py -y 2018 -c DiEle
python makePrefitPdf_fourTemplate_Zjets.py -y 2018 -c DiMu

python makePrefitZJets.py -y 2016 -c DiMu
python makePrefitZJets.py -y 2016 -c DiEle

python makePrefitZJets.py -y 2017 -c DiMu
python makePrefitZJets.py -y 2017 -c DiEle

python makePrefitZJets.py -y 2018 -c DiMu
python makePrefitZJets.py -y 2018 -c DiEle


echo "Done"
