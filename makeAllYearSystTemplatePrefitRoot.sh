
declare -a controlRegion=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
for cr in ${controlRegion[@]}; do
    python makePlots_template_syst_root.py -c Mu   -y 2016 --useQCDMC --$cr 
    python makePlots_template_syst_root.py -c Ele  -y 2016 --useQCDMC --$cr 
    
	python makePlots_template_syst_root.py -c Mu   -y 2017 --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2017 --useQCDMC --$cr  
	
	python makePlots_template_syst_root.py -c Mu   -y 2018 --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2018 --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 

for cr in ${controlRegion[@]}; do
    python makePlots_template_syst_root.py -c Mu   -y 2016 --syst BTagSF_b --level up --useQCDMC --$cr 
    python makePlots_template_syst_root.py -c Ele  -y 2016 --syst BTagSF_b --level up --useQCDMC --$cr 
    
	python makePlots_template_syst_root.py -c Mu   -y 2017 --syst BTagSF_b --level up --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2017 --syst BTagSF_b --level up --useQCDMC --$cr  
	
	python makePlots_template_syst_root.py -c Mu   -y 2018 --syst BTagSF_b --level up --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2018 --syst BTagSF_b --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makePlots_template_syst_root.py -c Mu   -y 2016 --syst BTagSF_b --level down --useQCDMC --$cr  
    python makePlots_template_syst_root.py -c Ele  -y 2016 --syst BTagSF_b --level down --useQCDMC --$cr 
    
	python makePlots_template_syst_root.py -c Mu   -y 2017 --syst BTagSF_b --level down --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2017 --syst BTagSF_b --level down --useQCDMC --$cr 
	
	python makePlots_template_syst_root.py -c Mu   -y 2018 --syst BTagSF_b --level down --useQCDMC --$cr 
	python makePlots_template_syst_root.py -c Ele  -y 2018 --syst BTagSF_b --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 
