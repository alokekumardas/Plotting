ControlRegion=["tight", "looseCRge2e0", "looseCRge2ge0", "looseCRe3ge2", "looseCRge4e0", "looseCRe3e0", "looseCRe2e1", "looseCRe2e0", "looseCRe2e2", "looseCRe3e1" ]


cfile = open('localTest.sh','w')

for year in ["2016", "2017", "2018"]:
    for cr in ControlRegion:
            run_commandEle =  \
            './makeHistograms_condor_nominal.sh Ele %s %s \n\
\n\n' %(year, cr)
            cfile.write(run_commandEle)
            run_commandMu =  \
            './makeHistograms_condor_nominal.sh Mu %s %s \n\
\n\n' %(year, cr)
            cfile.write(run_commandMu)
            
            
            
systematics = ["PU","MuEff","PhoEff","BTagSF_b","BTagSF_l"]

for syst in systematics:
	myfile = open('localTest_%s.sh'%syst,'w')

	for year in ["2016", "2017", "2018"]:
		for cr in ControlRegion:
			run_commandEleup =  \
			'./makeHistograms_condor_syst.sh Ele %s %s %s up &\n\
\n\n' %(year, cr, syst)
			myfile.write(run_commandEleup)
			run_commandMuup =  \
			'./makeHistograms_condor_syst.sh Mu %s %s %s up &\n\
\n\n' %(year, cr, syst)
			myfile.write(run_commandMuup)
			run_commandEledown =  \
			'./makeHistograms_condor_syst.sh Ele %s %s %s down &\n\
\n\n' %(year, cr, syst)
			myfile.write(run_commandEledown)
			run_commandMudown =  \
			'./makeHistograms_condor_syst.sh Mu %s %s %s down &\n\
\n\n' %(year, cr, syst)
			myfile.write(run_commandMudown)           
			
	myfile.close() 
