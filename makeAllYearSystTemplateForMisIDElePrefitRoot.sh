
declare -a controlRegion=("looseCRge2e0" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" )
for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 

for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst BTagSF_b --level up --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst BTagSF_b --level up --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst BTagSF_b --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst BTagSF_b --level up --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst BTagSF_b --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst BTagSF_b --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst BTagSF_b --level down --useQCDMC --$cr  
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst BTagSF_b --level down --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst BTagSF_b --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst BTagSF_b --level down --useQCDMC --$cr 
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst BTagSF_b --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst BTagSF_b --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 

for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst BTagSF_l --level up --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst BTagSF_l --level up --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst BTagSF_l --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst BTagSF_l --level up --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst BTagSF_l --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst BTagSF_l --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst BTagSF_l --level down --useQCDMC --$cr  
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst BTagSF_l --level down --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst BTagSF_l --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst BTagSF_l --level down --useQCDMC --$cr 
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst BTagSF_l --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst BTagSF_l --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst PU --level up --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst PU --level up --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst PU --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst PU --level up --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst PU --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst PU --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst PU --level down --useQCDMC --$cr  
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst PU --level down --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst PU --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst PU --level down --useQCDMC --$cr 
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst PU --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst PU --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 



for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst MuEff --level up --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst MuEff --level up --useQCDMC --$cr # WILL MUEFF SCALE FACTOR EFFECT, ELE CHANNEL OR NOT? 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst MuEff --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst MuEff --level up --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst MuEff --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst MuEff --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst MuEff --level down --useQCDMC --$cr  
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst MuEff --level down --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst MuEff --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst MuEff --level down --useQCDMC --$cr 
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst MuEff --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst MuEff --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst PhoEff --level up --useQCDMC --$cr 
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst PhoEff --level up --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst PhoEff --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst PhoEff --level up --useQCDMC --$cr  
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst PhoEff --level up --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst PhoEff --level up --useQCDMC --$cr 

done
wait
echo "Done prefit plots!" 


for cr in ${controlRegion[@]}; do
    python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2016 --syst PhoEff --level down --useQCDMC --$cr  
    python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2016 --syst PhoEff --level down --useQCDMC --$cr 
    
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2017 --syst PhoEff --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2017 --syst PhoEff --level down --useQCDMC --$cr 
	
	python makeRootTemplateSystForMisIDEle.py -c Mu   -y 2018 --syst PhoEff --level down --useQCDMC --$cr 
	python makeRootTemplateSystForMisIDEle.py -c Ele  -y 2018 --syst PhoEff --level down --useQCDMC --$cr 
done
wait
echo "Done prefit plots!" 
