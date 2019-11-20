
declare -a StringArray=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )

for val in ${StringArray[@]}; do
    python makePlots_4template_Zjets_pre-post.py -c Mu   -y 2016 --postfitPlots --useQCDMC --$val"_fourTemplate"& 
    python makePlots_4template_Zjets_pre-post.py -c Ele  -y 2016 --postfitPlots --useQCDMC --$val"_fourTemplate"& 
    python makePlots_4template_Zjets_pre-post.py -c Mu   -y 2017 --postfitPlots --useQCDMC --$val"_fourTemplate"&
    python makePlots_4template_Zjets_pre-post.py -c Ele  -y 2017 --postfitPlots --useQCDMC --$val"_fourTemplate"& 
    python makePlots_4template_Zjets_pre-post.py -c Mu   -y 2018 --postfitPlots --useQCDMC --$val"_fourTemplate"& 
    python makePlots_4template_Zjets_pre-post.py -c Ele  -y 2018 --postfitPlots --useQCDMC --$val"_fourTemplate"& 

done
wait
echo "Done postfit plots!" 

