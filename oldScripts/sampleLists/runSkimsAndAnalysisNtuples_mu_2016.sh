#!/bin/bash

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
"Data_SingleMu_b" \
"Data_SingleMu_c" \
"Data_SingleMu_d" \
"Data_SingleMu_e" \
"Data_SingleMu_f" \
"Data_SingleMu_g" \
"Data_SingleMu_h" \
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
"QCD_Pt20to30_Mu" \
"QCD_Pt30to50_Mu" \
"QCD_Pt50to80_Mu" \
"QCD_Pt80to120_Mu" \
"QCD_Pt120to170_Mu" \
"QCD_Pt170to300_Mu" \
"QCD_Pt300to470_Mu" \
"QCD_Pt470to600_Mu" \
"QCD_Pt600to800_Mu" \
"QCD_Pt800to1000_Mu" \
"QCD_Pt1000toInf_Mu" \
"WW" \
"WZ" \
"ZZ" \
"ZGamma" )

#filelist=`cat filelist_${sampleType[job]}.txt`
datasetname=("/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTGamma_Dilept_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTGamma_Hadronic_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/SingleMuon/Run2016B_ver2-Nano1June2019_ver2-v1/NANOAOD" \
"/SingleMuon/Run2016C-Nano1June2019-v1/NANOAOD" \
"/SingleMuon/Run2016D-Nano1June2019-v1/NANOAOD" \
"/SingleMuon/Run2016E-Nano1June2019-v1/NANOAOD" \
"/SingleMuon/Run2016F-Nano1June2019-v1/NANOAOD" \
"/SingleMuon/Run2016G-Nano1June2019-v1/NANOAOD" \
"/SingleMuon/Run2016H-Nano1June2019-v1/NANOAOD" \
"/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_plus5percentMaterial_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/NANOAODSIM" \
"/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-20to30_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-30to50_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-50to80_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-80to120_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-170to300_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-300to470_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-470to600_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-600to800_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-800to1000_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
"/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv5-PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/NANOAODSIM" \
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
channel="mu"
channelDir="muons"
tupleExtraName1=""
tupleExtraName2=""
if [ "$jobType" == "QCD" ] ;	then
	channel="qcdmu"
	channelDir="qcdmuons"
	tupleExtraName2="__QCDcr"
fi
if [ "$jobType" == "Dilep" ] ;	then
	channel="dimu"
	channelDir="dimuons"
	tupleExtraName1="Dilep_"
	tupleExtraName2="__Dilep"
fi

#outputdir="root://cmseos.fnal.gov//store/user/lpctop/TTGamma/13TeV_"
#outputdir="root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_v1/13TeV_"
outputdir2="root://cmseos.fnal.gov//store/user/aldas/NanoAOD/TTGamma_16/13TeV_"





echo "AnalysisNtuple/makeSkim 2016 ${channel} ${sampleType[job]}_skim.root  xrootd `dasgoclient --query="file dataset = ${datasetname[job]}"` "
AnalysisNtuple/makeSkim 2016 ${channel} ${sampleType[job]}_skim.root  xrootd `dasgoclient --query="file dataset = ${datasetname[job]}"`

echo "xrdcp -f ${sampleType[job]}_skim.root ${outputdir2}skims/${channelDir}"
xrdcp -f ${sampleType[job]}_skim.root ${outputdir2}skims/${channelDir}/

echo "AnalysisNtuple/makeAnalysisNtuple 2016 ${sampleType[job]}${tupleExtraName2} .  ${outputdir2}skims/muons/${sampleType[job]}_skim.root"
AnalysisNtuple/makeAnalysisNtuple 2016 ${sampleType[job]}${tupleExtraName2} . ${outputdir2}skims/muons/${sampleType[job]}_skim.root

echo "xrdcp -f ${tupleExtraName1}${sampleType[job]}_2016_AnalysisNtuple.root ${outputdir2}AnalysisNtuples/${channelDir}"
xrdcp -f ${tupleExtraName1}${sampleType[job]}_2016_AnalysisNtuple.root ${outputdir2}AnalysisNtuples/${channelDir}/

echo "rm -rf ${sampleType[job]}_skim.root "
rm -rf ${sampleType[job]}_skim.root

echo "rm -rf ${tupleExtraName1}${sampleType[job]}_2016_AnalysisNtuple.root"
rm -rf ${tupleExtraName1}${sampleType[job]}_2016_AnalysisNtuple.root

