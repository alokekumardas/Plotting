#!/bin/bash
voms-proxy-info --all
job=$1
jobType=$2
sampleType=("TTGamma_SingleLeptFromTbar" \
"TTGamma_SingleLeptFromT" \
"TTGamma_Dilepton" \
"TTGamma_Hadronic" \
"TTbarPowheg_Dilepton" \
"TTbarPowheg_Hadronic" \
"TTbarPowheg_Semilept" \
"W1jets" \
"W2jets" \
"W3jets" \
"W4jets" \
"Data_SingleEle_b" \
"Data_SingleEle_c" \
"Data_SingleEle_d" \
"Data_SingleEle_e" \
"Data_SingleEle_f" \
"DYjetsM10to50" \
"DYjetsM50" \
"ST_s-channel" \
"ST_t-channel" \
"ST_tbar-channel" \
"ST_tW-channel" \
"ST_tbarW-channel" \
"TTWtoQQ" \
"TTWtoLNu" \
"TTZtoLL" \
"WGamma" \
"TGJets" \
"GJets_HT-40To100" \
"GJets_HT-100To200" \
"GJets_HT-200To400" \
"GJets_HT-400To600" \
"GJets_HT-600ToInf" \
"QCD_Pt20to30_Ele" \
"QCD_Pt30to50_Ele" \
"QCD_Pt50to80_Ele" \
"QCD_Pt80to120_Ele" \
"QCD_Pt120to170_Ele" \
"QCD_Pt300toInf_Ele" \
"WW" \
"WZ" \
"ZZ" \
"ZGamma" \
"QCD_Pt170to300_Ele" )

#filelist=`cat filelist_${sampleType[job]}.txt`

datasetname=("/TTGamma_SingleLeptFromTbar_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTGamma_SingleLeptFromT_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTGamma_Dilept_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTGamma_Hadronic_TuneCP5_PSweights_13TeV_madgraph_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/SingleElectron/Run2017B-Nano1June2019-v1/NANOAOD" \
"/SingleElectron/Run2017C-Nano1June2019-v1/NANOAOD" \
"/SingleElectron/Run2017D-Nano1June2019-v1/NANOAOD" \
"/SingleElectron/Run2017E-Nano1June2019-v1/NANOAOD" \
"/SingleElectron/Run2017F-Nano1June2019-v1/NANOAOD" \
"/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/TGJets_TuneCP5_13TeV_amcatnlo_madspin_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/GJets_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/GJets_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_new_pmx_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/GJets_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/GJets_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAODv5-PU2017_12Apr2018_Nano1June2019_102X_mc2017_realistic_v7-v1/NANOAODSIM" \
"/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM" )

USER="aldas"

if [ -z ${_CONDOR_SCRATCH_DIR} ] ; then
        echo "Running Interactively" ;
else
        echo "Running In Batch"
        cd ${_CONDOR_SCRATCH_DIR}
        echo ${_CONDOR_SCRATCH_DIR}
        #echo "xrdcp root://cmseos.fnal.gov//store/user/"${USER}"/CMSSW_10_2_4.tgz ."
        #xrdcp root://cmseos.fnal.gov//store/user/${USER}/CMSSW_10_2_4.tgz .
        source /cvmfs/cms.cern.ch/cmsset_default.sh
        #export $SCRAM_ARCH=slc6_amd64_gcc700
      #  setenv SCRAM_ARCH slc6_amd64_gcc700
        eval `scramv1 project CMSSW CMSSW_10_2_4`
      #  echo $SCRAM_ARCH
        cd CMSSW_10_2_4/src
        eval `scramv1 runtime -sh`
        echo "cd CMSSW_10_2_4/src"
        cd -
        echo "xrdcp root://cmseos.fnal.gov//store/user/"${USER}"/NanoAod.tgz ."
        xrdcp root://cmseos.fnal.gov//store/user/${USER}/NanoAod.tgz .
        #echo "tar -xvf CMSSW_10_2_4.tgz"
        echo "tar -xvf NanoAod.tgz"
        #tar -xzf CMSSW_10_2_4.tgz
        tar -xzf NanoAod.tgz
        cd  NanoAod/TTGammaSemiLep_13TeV/
        cd PileupHists
        echo "xrdcp -r root://cmseos.fnal.gov//store/user/aldas/Data_Pileup.tgz ."
        xrdcp -rf root://cmseos.fnal.gov//store/user/aldas/Data_Pileup.tgz .
        tar -xvf Data_Pileup.tgz
        cd ..
 #       filelist=`cat  ${_CONDOR_SCRATCH_DIR}/filelist_${sampleType[job]}.txt`
        export HOME=$PWD
        sleep 5

fi

#eval `scramv1 runtime -sh`
channel="ele"
channelDir="electrons"
tupleExtraName1=""
tupleExtraName2=""
if [ "$jobType" == "QCD" ] ;	then
	channel="qcdele"
	channelDir="qcdelectrons"
	tupleExtraName1="QCDcr_"
	tupleExtraName2="__QCDcr"
fi
if [ "$jobType" == "Dilep" ] ;	then
	channel="diele"
	channelDir="dielectrons"
fi

#outputdir="root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_v1/13TeV_"
outputdir2="root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_17/13TeV_"





echo "AnalysisNtuple/makeSkim 2017 ${channel} ${sampleType[job]}_skim.root  xrootd `dasgoclient --query="file dataset = ${datasetname[job]}"` "
AnalysisNtuple/makeSkim 2017 ${channel} ${sampleType[job]}_skim.root  xrootd `dasgoclient --query="file dataset = ${datasetname[job]}"`

echo "xrdcp -f ${sampleType[job]}_skim.root ${outputdir2}skims/${channelDir}"
xrdcp -f ${sampleType[job]}_skim.root ${outputdir2}skims/${channelDir}/

echo "AnalysisNtuple/makeAnalysisNtuple 2017 ${sampleType[job]}${tupleExtraName2} . ${outputdir2}skims/${channelDir}/${sampleType[job]}_skim.root"
AnalysisNtuple/makeAnalysisNtuple 2017 ${sampleType[job]}${tupleExtraName2} . ${outputdir2}skims/${channelDir}/${sampleType[job]}_skim.root


echo "xrdcp -f ${tupleExtraName1}${sampleType[job]}_2017_AnalysisNtuple.root ${outputdir2}AnalysisNtuples/${channelDir}"
xrdcp -f ${tupleExtraName1}${sampleType[job]}_2017_AnalysisNtuple.root ${outputdir2}AnalysisNtuples/${channelDir}/

echo "rm -rf ${sampleType[job]}_skim.root "
rm -rf ${sampleType[job]}_skim.root

echo "rm -rf ${tupleExtraName1}${sampleType[job]}_2017_AnalysisNtuple.root"
rm -rf ${tupleExtraName1}${sampleType[job]}_2017_AnalysisNtuple.root

