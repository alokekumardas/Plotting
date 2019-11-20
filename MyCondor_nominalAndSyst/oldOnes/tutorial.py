import subprocess

with open('output_subprocess.txt','w') as f: # passing the stdout to a output.txt
	sample = "TTGamma"
	myargs = "root -l root://cmseos.fnal.gov//store/user/%s/%s.root"%("npoudyal",sample)
	myprocess = subprocess.Popen(myargs,shell = True, stdout=f, stderr=f) # if shell is true then we pass an argument as an one string, else we would be passing a list of arguments



