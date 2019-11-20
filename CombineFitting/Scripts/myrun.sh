#python data/tutorials/shapes/histogramCreator.py

#echo "created new root file."
echo "======================"
#combine -M FitDiagnostics --do95 1 -n Nabin data/tutorials/shapes/ttgamma.txt --redefineSignalPOIs r,background1_norm,background2_norm --saveWorkspace --saveOverallShapes --saveNLL  --plots

combine -M FitDiagnostics -n Nabin data/tutorials/shapes/ttgamma_sys.txt --plots
echo "========================================================="
echo "========================================================="
echo "========================================================="

combine -M MultiDimFit -n Nabin data/tutorials/shapes/ttgamma_sys.txt

wait
echo "Fitting is done."

text2workspace.py  data/tutorials/shapes/ttgamma_sys.txt 


# do the following to print the informations or open the root file and print RooWorkspace as below.
#f_simple = ROOT.TFile("simple-counting-experiment.root","READ")
#w_simple = f_simple.Get("w")
#w_simple.Print()
python test/printWorkspaceNormalisations.py data/tutorials/shapes/ttgamma.root

echo "RooWorkspace(w) is printed on the screen."


## FitDiagnostics, MultiDimFit

#combine -M MultiDimFit -n Nabin data/tutorials/shapes/ttgamma.txt --expectSignal 5.32 -t 100 --toysNoSystematics -s -1
