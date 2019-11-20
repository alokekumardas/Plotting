#!/bin/bash

echo "Not running twoJetTwobTagHistogramming.sh for making new histograms."

echo "Now running twoJetTwobTagPlottingAllyearPrefit.sh  Prefit for all 3 years"
./twoJetTwobTagPlottingAllyearPrefit.sh
echo "Now running twoJetTwobTagPlottingAllyearPostfit.sh  Postfit for all 3 years"
./twoJetTwobTagPlottingAllyearPrefit.sh

echo "Copy Pre post plots and tex files to make slides"
