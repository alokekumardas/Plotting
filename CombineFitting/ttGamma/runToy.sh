for i in `seq 0.2 .2 2`; do 
	echo $i; 

	combine -M FitDiagnostics -n $i datacard_all.txt --expectSignal=$i -t 200 -s -1 --redefineSignalPOIs r,nonPromptSF &
	#combine -M FitDiagnostics -s -1 -t 200 -n $i datacard_all.txt --setParameters=$i --redefineSignalPOIs r,nonPromptSF --trackParameters r,nonPromptSF --expectSignal=$i&
	#combine -M FitDiagnostics -s -1 -t 200 -n $i datacard_all.txt --setParameters=$i --redefineSignalPOIs r,nonPromptSF --trackParameters r,nonPromptSF --expectSignal=$i &
done

wait

echo "Done"


