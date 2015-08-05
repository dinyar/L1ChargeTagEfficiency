These scripts run on one (dimuon) dataset containing RAW+RECO data. They then compare the trigger charge assignment with the RECO charge assignment.

The ntuples required for this have to be produced with different CMSSW versions:
  * CMSSW_5_3_18 for 2012D data (`2012D-Muonia`)
  * CMSSW_6_2_12 for 2015 MC (`JpsiToMuMu_JPsiPt7WithFSR_13TeV`)
    * This however needs to be patched to fix the CSCTF charge-flip bug.
