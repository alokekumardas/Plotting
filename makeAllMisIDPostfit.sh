
declare -a StringArray=("looseCRge2e0" "looseCRge4e0" "looseCRe2e1" "looseCRe2e0" "looseCRe3e0" )

for val in ${StringArray[@]}; do
    python makePlots_misIDEle_pre-post.py -c Mu   -y 2016 --postfitPlots --useQCDMC --$val& 
    python makePlots_misIDEle_pre-post.py -c Ele  -y 2016 --postfitPlots --useQCDMC --$val& 
    python makePlots_misIDEle_pre-post.py -c Mu   -y 2017 --postfitPlots --useQCDMC --$val&
    python makePlots_misIDEle_pre-post.py -c Ele  -y 2017 --postfitPlots --useQCDMC --$val& 
    python makePlots_misIDEle_pre-post.py -c Mu   -y 2018 --postfitPlots --useQCDMC --$val& 
    python makePlots_misIDEle_pre-post.py -c Ele  -y 2018 --postfitPlots --useQCDMC --$val& 

done
wait
echo "Done postfit plots!" 

