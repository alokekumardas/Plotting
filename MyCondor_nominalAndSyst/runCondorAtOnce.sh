#!/bin/bash

./setup_condor_Histogramming.sh
condor_submit condor_makeHistograms.jdl
