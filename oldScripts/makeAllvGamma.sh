declare -a StringArray=("tight" "looseCRge2e0" "looseCRge2ge0" "looseCRe3ge2" "looseCRge4e0" "looseCRe3e0" "looseCRe2e1" "looseCRe2e0" "looseCRe2e2" "looseCRe3e1" )
for val in ${StringArray[@]}; do
    python makeVGammaSF.py -c Mu   -y 2016 --useQCDMC --$val"_vGamma" 
    #python makeVGammaSF.py -c Mu   -y 2017 --useQCDMC --$val"_vGamma" &
    #python makeVGammaSF.py -c Mu   -y 2018 --useQCDMC --$val"_vGamma" &
    
done

wait
echo "Done!" 


