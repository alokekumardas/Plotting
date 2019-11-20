from ROOT import *
import os

import sys
from optparse import OptionParser

parser = OptionParser()



parser.add_option("-c", "--channel", dest="channel", default="mu",type='str',
                     help="Specify which channel mu or ele? default is mu" )

parser.add_option("-y", "--year", dest="Year", default="",type='str',
                     help="Specify which year 2016, 2017 or 2018?" )

parser.add_option("-s", "--step", dest="step", default="",type='str',
                     help="Specify which iteration , ita1 or ita2, or ita3?" )

parser.add_option("-p", "--opt", dest="sel", default="",type='str',
                     help="Specify which selection?" )

(options, args) = parser.parse_args()

channel=options.channel
year=options.Year
step=options.step
sel=options.sel

if channel=="ele":
        Chan="Ele"
elif channel=="mu":
        Chan="Mu"


#sel2 = "Ele_2jet0b_"

file_=TFile("fitDiagnostics%s_%s_%s.root"%(sel,year,step),"read")
#print file_
fit_s=file_.Get("fit_s")

if "pho" in sel:
	par1_fitresult = fit_s.floatParsFinal().find("r")
	r=par1_fitresult.getVal()
	r_err=par1_fitresult.getError()
	par2_fitresult = fit_s.floatParsFinal().find("WGammaSF")
	WGammaSF=par2_fitresult.getVal()
	WGammaSF_err=par2_fitresult.getError()
	par3_fitresult = fit_s.floatParsFinal().find("ZGammaSF")
	ZGammaSF=par3_fitresult.getVal()
	ZGammaSF_err=par3_fitresult.getError()

	#print sel, step
	print "QCDTF_%s=%s"%(sel,r)
        print "QCDTF_err_%s=%s"%(sel,r_err) 
	print "WGammaSF_%s=%s"%(sel,WGammaSF)
        print "WGammaSF_err_%s=%s"%(sel,WGammaSF_err)
	print "ZGammaSF_%s=%s"%(sel,ZGammaSF)
	print "ZGammaSF_err_%s=%s"%(sel,ZGammaSF_err) 
	print "#########################################################################################"
else :
	par1_fitresult = fit_s.floatParsFinal().find("r")
        r=par1_fitresult.getVal()
        r_err=par1_fitresult.getError()
        par2_fitresult = fit_s.floatParsFinal().find("wjetSF")
        wjetSF=par2_fitresult.getVal()
        wjetSF_err=par2_fitresult.getError()

        #print sel, step
	print "QCDTF_%s=%s"%(sel,r)
        print "QCDTF_err_%s=%s"%(sel,r_err) 
	print "WJetsSF_%s=%s"%(sel,wjetSF)
        print "WJetsSF_err_%s=%s"%(sel,wjetSF_err)
	print "##################################"




print dir(fit_s.floatParsFinal().find("r"))
['AClean', 'ADirty', 'AbstractMethod', 'Activate', 'Always', 'AppendPad', 'Auto', 'Browse', 'CheckedHash', 'Class', 'ClassName', 'Class_Name', 'Class_Version', 'Clear', 'Clone', 'CollectErrors', 'Compare', 'ConfigChange', 'Copy', 'CountErrors', 'DeActivate', 'DeclFileLine', 'DeclFileName', 'Delete', 'Dictionary', 'DistancetoPrimitive', 'Draw', 'DrawClass', 'DrawClone', 'Dump', 'Error', 'Execute', 'ExecuteEvent', 'Fatal', 'FillBuffer', 'FindObject', 'GetDrawOption', 'GetDtorOnly', 'GetIconName', 'GetName', 'GetObjectInfo', 'GetObjectStat', 'GetOption', 'GetTitle', 'GetUniqueID', 'HandleTimer', 'HasInconsistentHash', 'Hash', 'Ignore', 'ImplFileLine', 'ImplFileName', 'Info', 'InheritsFrom', 'Inspect', 'InvertBit', 'IsA', 'IsEqual', 'IsFolder', 'IsOnHeap', 'IsSortable', 'IsZombie', 'MayNotUse', 'Never', 'NotAdvised', 'Notify', 'NumEvent', 'Obsolete', 'Paint', 'Pop', 'Print', 'PrintErrors', 'Raw', 'Read', 'RecursiveRemove', 'Relative', 'RelativeExpected', 'ResetBit', 'SaveAs', 'SavePrimitive', 'SetBit', 'SetDrawOption', 'SetDtorOnly', 'SetName', 'SetNameTitle', 'SetObjectStat', 'SetTitle', 'SetUniqueID', 'ShowMembers', 'Sizeof', 'Streamer', 'StreamerNVirtual', 'SysError', 'TestBit', 'TestBits', 'UseCurrentStyle', 'ValueChange', 'Warning', 'Write', '_RooAbsArg__CheckTObjectHashConsistency', '_RooAbsArg__attachToStore', '_RooAbsArg__attachToTree', '_RooAbsArg__attachToVStore', '_RooAbsArg__cleanBranchName', '_RooAbsArg__copyCache', '_RooAbsArg__fillTreeBranch', '_RooAbsArg__getObservablesHook', '_RooAbsArg__getParametersHook', '_RooAbsArg__getProxy', '_RooAbsArg__graphVizAddConnections', '_RooAbsArg__inhibitDirty', '_RooAbsArg__isValid', '_RooAbsArg__numProxies', '_RooAbsArg__operModeHook', '_RooAbsArg__optimizeDirtyHook', '_RooAbsArg__printAttribList', '_RooAbsArg__registerProxy', '_RooAbsArg__setProxyNormSet', '_RooAbsArg__setShapeDirty', '_RooAbsArg__setTreeBranchStatus', '_RooAbsArg__setValueDirty', '_RooAbsArg__syncCache', '_RooAbsArg__unRegisterProxy', '_RooAbsLValue__CheckTObjectHashConsistency', '_RooAbsRealLValue__CheckTObjectHashConsistency', '_RooAbsRealLValue__copyCache', '_RooAbsRealLValue__fitRangeOKForPlotting', '_RooAbsRealLValue__setVal', '_RooAbsRealLValue__setValFast', '_RooAbsReal__CheckTObjectHashConsistency', '_RooAbsReal__attachToTree', '_RooAbsReal__attachToVStore', '_RooAbsReal__chi2FitDriver', '_RooAbsReal__copyCache', '_RooAbsReal__createIntObj', '_RooAbsReal__evaluate', '_RooAbsReal__fillTreeBranch', '_RooAbsReal__findInnerMostIntegration', '_RooAbsReal__globalSelectComp', '_RooAbsReal__integralNameSuffix', '_RooAbsReal__isSelectedComp', '_RooAbsReal__isValid', '_RooAbsReal__isValidReal', '_RooAbsReal__makeProjectionSet', '_RooAbsReal__matchArgs', '_RooAbsReal__matchArgsByName', '_RooAbsReal__plotAsymOn', '_RooAbsReal__plotOn', '_RooAbsReal__plotOnCompSelect', '_RooAbsReal__plotOnWithErrorBand', '_RooAbsReal__plotSanityChecks', '_RooAbsReal__selectComp', '_RooAbsReal__selectNormalization', '_RooAbsReal__selectNormalizationRange', '_RooAbsReal__setTreeBranchStatus', '_RooAbsReal__syncCache', '_RooAbsReal__traceEval', '_RooAbsReal__traceEvalHook', '_RooPrintable__CheckTObjectHashConsistency', '_RooRealVar__CheckTObjectHashConsistency', '_RooRealVar__attachToTree', '_RooRealVar__attachToVStore', '_RooRealVar__chopAt', '_RooRealVar__copyCache', '_RooRealVar__evaluate', '_RooRealVar__fillTreeBranch', '_RooRealVar__setExpensiveObjectCache', '_RooRealVar__setVal', '_RooRealVar__setValFast', '_RooRealVar__sharedProp', '_TNamed__CheckTObjectHashConsistency', '_TObject__AddToTObjectTable', '_TObject__CheckTObjectHashConsistency', '_TObject__DoError', '_TObject__MakeZombie', '__add__', '__assign__', '__bool__', '__class__', '__cmp__', '__contains__', '__cpp_eq__', '__cppname__', '__delattr__', '__destruct__', '__dict__', '__dispatch__', '__div__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__nonzero__', '__radd__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__rsub__', '__scope__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__weakref__', '_get_smart_ptr', '_ioEvoList', '_ioReadStack', 'addOwnedComponents', 'addParameters', 'addServer', 'addServerList', 'aggregateCacheUniqueSuffix', 'analyticalIntegral', 'analyticalIntegralWN', 'asTF', 'attachDataSet', 'attachDataStore', 'attributes', 'binBoundaries', 'bindVars', 'branchNodeServerList', 'cacheUniqueSuffix', 'canNodeBeCached', 'changeServer', 'checkDependents', 'checkObservables', 'chi2FitTo', 'clearEvalErrorLog', 'clearShapeDirty', 'clearValueAndShapeDirty', 'clearValueDirty', 'clientIterator', 'clone', 'cloneTree', 'constOptimizeTestStatistic', 'copyCacheFast', 'crc32', 'createChi2', 'createFundamental', 'createHistogram', 'createIntRI', 'createIntegral', 'createPlotProjection', 'createProfile', 'createRunningIntegral', 'createScanRI', 'defaultErrorLevel', 'defaultIntegratorConfig', 'defaultPrintContents', 'defaultPrintStream', 'defaultPrintStyle', 'deleteSharedProperties', 'dependentOverlaps', 'dependsOn', 'dependsOnValue', 'derivative', 'enableOffsetting', 'errorVar', 'evalErrorIter', 'evalErrorLoggingMode', 'expensiveObjectCache', 'fillDataHist', 'fillHistogram', 'findConstantNodes', 'findNewServer', 'findRoot', 'findServer', 'fixAddCoefNormalization', 'fixAddCoefRange', 'fnv1a32', 'fnv1a32start', 'fnv1a64', 'fnv1a64start', 'forceAnalyticalInt', 'forceNumInt', 'format', 'frame', 'functor', 'getAnalyticalIntegral', 'getAnalyticalIntegralWN', 'getAsymErrorHi', 'getAsymErrorLo', 'getAttribute', 'getBin', 'getBinWidth', 'getBinning', 'getBinningNames', 'getBinningPtr', 'getBins', 'getCache', 'getCloningAncestors', 'getComponents', 'getDependents', 'getError', 'getErrorHi', 'getErrorLo', 'getForceNumInt', 'getIntegratorConfig', 'getMax', 'getMaxVal', 'getMin', 'getObservables', 'getParameters', 'getPlotLabel', 'getPropagatedError', 'getStringAttribute', 'getTitle', 'getTransientAttribute', 'getUnit', 'getVal', 'getValV', 'getVariables', 'graphVizTree', 'hasAsymError', 'hasBinning', 'hasClients', 'hasError', 'hasMax', 'hasMin', 'hasRange', 'hideOffset', 'iGenFunction', 'importWorkspaceHook', 'inRange', 'ioStreamerPass2', 'ioStreamerPass2Finalize', 'isBinnedDistribution', 'isCloneOf', 'isConstant', 'isDerived', 'isFundamental', 'isIdentical', 'isJacobianOK', 'isLValue', 'isOffsetting', 'isShapeDirty', 'isShapeServer', 'isValidReal', 'isValueDirty', 'isValueDirtyAndClear', 'isValueOrShapeDirtyAndClear', 'isValueServer', 'jacobian', 'kAddress', 'kArgs', 'kBitMask', 'kCanDelete', 'kCannotPick', 'kClassName', 'kCollectionHeader', 'kExtras', 'kHasUUID', 'kInconsistent', 'kInline', 'kInvalidObject', 'kIsOnHeap', 'kIsReferenced', 'kMustCleanup', 'kName', 'kNoContextMenu', 'kNotDeleted', 'kObjInCanvas', 'kOverwrite', 'kSingleKey', 'kSingleLine', 'kStandard', 'kTitle', 'kTreeStructure', 'kValue', 'kVerbose', 'kWriteDelete', 'kZombie', 'leafNodeServerList', 'localNoDirtyInhibit', 'logEvalError', 'ls', 'maxVal', 'mean', 'minTrialSamples', 'moment', 'nameFieldLength', 'namePtr', 'numBins', 'numCaches', 'numEvalErrorItems', 'numEvalErrors', 'observableOverlaps', 'offset', 'operMode', 'operator delete', 'operator delete[]', 'operator new', 'operator new[]', 'optimizeCacheMode', 'overlaps', 'ownedComponents', 'plotOn', 'plotSamplingHint', 'plotSliceOn', 'preferredObservableScanOrder', 'printAddress', 'printArgs', 'printClassName', 'printCompactTree', 'printCompactTreeHook', 'printComponentTree', 'printDirty', 'printEvalErrors', 'printExtras', 'printMetaArgs', 'printMultiline', 'printName', 'printScientific', 'printSigDigits', 'printStream', 'printTitle', 'printTree', 'printValue', 'randomize', 'readFromStream', 'recursiveCheckDependents', 'recursiveCheckObservables', 'recursiveRedirectServers', 'redirectServers', 'redirectServersHook', 'registerCache', 'removeAsymError', 'removeError', 'removeMax', 'removeMin', 'removeRange', 'removeServer', 'replaceServer', 'serverIterator', 'serverMIterator', 'serverNameChangeHook', 'setAsymError', 'setAttribute', 'setBin', 'setBinFast', 'setBinning', 'setBins', 'setCacheAndTrackHints', 'setCacheCheck', 'setConstant', 'setData', 'setDirtyInhibit', 'setError', 'setEvalErrorLoggingMode', 'setExpensiveObjectCache', 'setHideOffset', 'setIntegratorConfig', 'setLocalNoDirtyInhibit', 'setMax', 'setMin', 'setOperMode', 'setParameterizeIntegral', 'setPlotLabel', 'setProhibitServerRedirect', 'setRange', 'setShapeDirty', 'setStringAttribute', 'setTransientAttribute', 'setUnit', 'setVal', 'setValueDirty', 'setWorkspace', 'shapeClientIterator', 'shapeClientMIterator', 'sigma', 'specialIntegratorConfig', 'stringAttributes', 'transientAttributes', 'treeNodeServerList', 'unRegisterCache', 'valueClientIterator', 'valueClientMIterator', 'verboseDirty', 'volume', 'wireAllCaches', 'writeToStream']





























