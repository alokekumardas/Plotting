python makeHistograms.py -y $1 -c Ele --tight -s TTGamma   --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s TTbar     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s TGJets    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s WJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s ZJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s WGamma    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s ZGamma    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s Diboson   --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s SingleTop --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s TTV       --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s QCDEle    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s GJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Ele --tight -s DataEle   --makeSignalRegionPlots &

python makeHistograms.py -y $1 -c Mu  --tight -s TTGamma   --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s TTbar     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s TGJets    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s WJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s ZJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s WGamma    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s ZGamma    --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s Diboson   --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s SingleTop --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s TTV       --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s QCDMu     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s GJets     --makeSignalRegionPlots &
python makeHistograms.py -y $1 -c Mu  --tight -s DataMu    --makeSignalRegionPlots &
wait
echo "Done making tight histograms!!"

