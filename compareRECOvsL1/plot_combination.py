#!/usr/bin/python

from ROOT import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../L1AnalysisHelpers"))
from CreateHistograms import *
from dataset_name import *

gROOT.Reset()
gROOT.SetBatch(kTRUE);

# #TODO:0 Add jpsi histos to combination plots
efficiencyList = []
# #TODO:30 Axis labels
# Entries: Label for histogram (Will be used for filename and title) | binning | parameters used for project functions
efficiencyList.append(["deltaR_reco", binningDict["distWideFine"], "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["diMu-gmtPt5_cs"], cutDict["diMu-gmtPt5"]])
efficiencyList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu1_recoEta", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoEta", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu1_recoPhi", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoPhi", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["deltaR_reco", binningDict["distWideFine"], "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["diMu-gmtPt5_us"], cutDict["diMu-gmtPt5"]])
efficiencyList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu1_recoEta", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoEta", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu1_recoPhi", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["mu2_recoPhi", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])

efficiencyList.append(["mu1_recoPhi_central", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu1_recoPt_central", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu1_recoEta_central", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu2_recoPhi_central", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu2_recoPt_central", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu2_recoEta_central", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["mu1_recoPhi_forward", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["mu1_recoPt_forward", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["mu1_recoEta_forward", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["mu2_recoPhi_forward", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["mu2_recoPt_forward", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["mu2_recoEta_forward", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1-forward_etagmt"]])

efficiencyList.append(["mu1_recoPhi_central", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu1_recoPt_central", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu1_recoEta_central", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu2_recoPhi_central", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu2_recoPt_central", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu2_recoEta_central", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["mu1_recoPhi_forward", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["mu1_recoPt_forward", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["mu1_recoEta_forward", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["mu2_recoPhi_forward", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["mu2_recoPt_forward", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["mu2_recoEta_forward", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-forward"]])

efficiencyList.append(["mu1_recoPhi_barrel", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["mu1_recoPt_barrel", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["mu1_recoEta_barrel", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["mu2_recoPhi_barrel", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["mu2_recoPt_barrel", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["mu2_recoEta_barrel", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-recoPt1-brl"]])




rateList = []
rateList.append(["deltaR_reco", binningDict["distWideFine"], "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["diMu-recoPt5"]])
rateList.append(["deltaR_reco", binningDict["distWideFine"], "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["diMu-gmtPt5_cs"]])
rateList.append(["deltaR_reco", binningDict["distWideFine"], "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["diMu-gmtPt5_us"]])
rateList.append(["mu1_recoEta", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-recoPt1"]])
rateList.append(["mu2_recoEta", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-recoPt1"]])
rateList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-recoPt1"]]) # Plot reco pT with cut on reco pT
rateList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-recoPt1"]]) # Plot reco pT with cut on reco pT
rateList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_cs"]]) # Plot reco pT with cut on GMT pT and correct charge
rateList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"]]) # Plot reco pT with cut on GMT pT and usable charge
rateList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_cs"]]) # Plot reco pT with cut on GMT pT and correct charge
rateList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"]]) # Plot reco pT with cut on GMT pT and usable charge


rateList.append(["mu1_recoPt_central", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-recoPt1-central"]])
rateList.append(["mu2_recoPt_central", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-recoPt1-central"]])
rateList.append(["mu1_recoPt_forward", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-recoPt1-forward"]])
rateList.append(["mu2_recoPt_forward", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-recoPt1-forward"]])
rateList.append(["mu1_recoPt_brl", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-recoPt1-brl"]])
rateList.append(["mu2_recoPt_brl", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-recoPt1-brl"]])

for varList in efficiencyList:
    generateCombinedEfficiencyHist(varList, "DiMuNtuple.root", "DiMuNtupleMC.root", dataset, datasetMC)

for varList in rateList:
    generateCombinedRateHist(varList, "DiMuNtuple.root", "DiMuNtupleMC.root", dataset, datasetMC)
