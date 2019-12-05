#!/bin/bash
rm makeHistograms.py
rm sampleInformation.py
rm HistogramListDict.py

cd ..
tar cfP myHistograms.tar makeHistograms.py sampleInformation.py HistogramListDict.py
mv myHistograms.tar MyCondor_nominalAndSyst
cd MyCondor_nominalAndSyst
xrdcp -f myHistograms.tar  root://cmseos.fnal.gov//store/user/npoudyal/

tar -xvf myHistograms.tar


                                               

