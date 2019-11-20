declare -a controlRegion=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
for cr in ${controlRegion[@]}; do
    python makePlots_template_syst_pre-post.py -c Mu   -y 2016 --postfitPlots --useQCDMC --$cr &
    python makePlots_template_syst_pre-post.py -c Ele  -y 2016 --postfitPlots --useQCDMC --$cr &
	python makePlots_template_syst_pre-post.py -c Mu   -y 2017 --postfitPlots --useQCDMC --$cr &
	python makePlots_template_syst_pre-post.py -c Ele  -y 2017 --postfitPlots --useQCDMC --$cr & 
	python makePlots_template_syst_pre-post.py -c Mu   -y 2018 --postfitPlots --useQCDMC --$cr &
	python makePlots_template_syst_pre-post.py -c Ele  -y 2018 --postfitPlots --useQCDMC --$cr &

done
wait
echo "Done postfit plots!" 




