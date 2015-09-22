#!/usr/bin/python

from ROOT import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),
                             "../../L1AnalysisHelpers"))
from CreateHistograms import *
from dataset_name import *

gROOT.Reset()
gROOT.SetBatch(kTRUE)

# #TODO:0 Add jpsi histos to combination plots
efficiencyList = []
# #TODO:30 Axis labels
# Entries:
# Label (for filename and title) | binning | parameters for project functions
efficiencyList.append(["deltaR_reco", binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt5_cs"], cutDict["diMu-gmtPt5"]])
efficiencyList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoPt", binningDict["pt25Fine"], "pT2_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["leadingMu_recoEta", binningDict["etaFine"], "Eta1_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoEta", binningDict["etaFine"], "Eta2_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["leadingMu_recoPhi", binningDict["phiFine"], "Phi1_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoPhi", binningDict["phiFine"], "Phi2_reco",
                       cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["deltaR_reco", binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt5_us"], cutDict["diMu-gmtPt5"]])
efficiencyList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoPt", binningDict["pt25Fine"], "pT2_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["leadingMu_recoEta", binningDict["etaFine"], "Eta1_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoEta", binningDict["etaFine"], "Eta2_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["leadingMu_recoPhi", binningDict["phiFine"], "Phi1_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
efficiencyList.append(["trailingMu_recoPhi", binningDict["phiFine"], "Phi2_reco",
                       cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])

efficiencyList.append(["leadingMu_recoPhi_central", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["leadingMu_recoPt_central", binningDict["pt25Fine"],
                       "pT1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["leadingMu_recoEta_central", binningDict["etaFine"],
                       "Eta1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoPhi_central", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoPt_central", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoEta_central", binningDict["etaFine"],
                       "Eta2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["leadingMu_recoPhi_forward", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["leadingMu_recoPt_forward", binningDict["pt25Fine"],
                       "pT1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["leadingMu_recoEta_forward", binningDict["etaFine"],
                       "Eta1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["trailingMu_recoPhi_forward", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["trailingMu_recoPt_forward", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])
efficiencyList.append(["trailingMu_recoEta_forward", binningDict["etaFine"],
                       "Eta2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-gmtPt1-forward_etagmt"]])

efficiencyList.append(["leadingMu_recoPhi_central", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["leadingMu_recoPt_central", binningDict["pt25Fine"],
                       "pT1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["leadingMu_recoEta_central", binningDict["etaFine"],
                       "Eta1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["trailingMu_recoPhi_central", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["trailingMu_recoPt_central", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["trailingMu_recoEta_central", binningDict["etaFine"],
                       "Eta2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-central"]])
efficiencyList.append(["leadingMu_recoPhi_forward", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["leadingMu_recoPt_forward", binningDict["pt25Fine"],
                       "pT1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["leadingMu_recoEta_forward", binningDict["etaFine"],
                       "Eta1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["trailingMu_recoPhi_forward", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["trailingMu_recoPt_forward", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])
efficiencyList.append(["trailingMu_recoEta_forward", binningDict["etaFine"],
                       "Eta2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-forward"]])

efficiencyList.append(["leadingMu_recoPhi_barrel", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["leadingMu_recoPt_barrel", binningDict["pt25Fine"],
                       "pT1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["leadingMu_recoEta_barrel", binningDict["etaFine"],
                       "Eta1_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["trailingMu_recoPhi_barrel", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["trailingMu_recoPt_barrel", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])
efficiencyList.append(["trailingMu_recoEta_barrel", binningDict["etaFine"],
                       "Eta2_reco", cutDict["diMu-gmtPt1_us"],
                       cutDict["diMu-recoPt1-brl"]])

# #TODO:0 Make jpsi plots for "central" region (dist and eff)
efficiencyList.append(["jPsi_InvMass", binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1_us"],
                       cutDict["jpsi-Pt1"]])
efficiencyList.append(["jPsi_recoEta", binningDict["etaFine"], "Eta_dimuon",
                       cutDict["jpsi-Pt1_us"], cutDict["jpsi-Pt1"]])
efficiencyList.append(["jPsi_recoPhi", binningDict["phiFine"], "Phi_dimuon",
                       cutDict["jpsi-Pt1_us"], cutDict["jpsi-Pt1"]])
efficiencyList.append(["jPsi_recoPt", binningDict["pt25Fine"], "pT_dimuon",
                       cutDict["jpsi-Pt1_us"], cutDict["jpsi-Pt1"]])


rateList = []
rateList.append(["deltaR_reco", binningDict["distWideFine"],
                 "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)",
                 cutDict["diMu-recoPt5"]])
rateList.append(["deltaR_reco", binningDict["distWideFine"],
                 "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)",
                 cutDict["diMu-gmtPt5_cs"]])
rateList.append(["deltaR_reco", binningDict["distWideFine"],
                 "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)",
                 cutDict["diMu-gmtPt5_us"]])
rateList.append(["leadingMu_recoEta", binningDict["etaFine"], "Eta1_reco",
                 cutDict["diMu-recoPt1"]])
rateList.append(["trailingMu_recoEta", binningDict["etaFine"], "Eta2_reco",
                 cutDict["diMu-recoPt1"]])
# Plot reco pT with cut on reco pT
rateList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-recoPt1"]])
# Plot reco pT with cut on reco pT
rateList.append(["trailingMu_recoPt", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-recoPt1"]])
# Plot reco pT with cut on GMT pT and correct charge
rateList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-gmtPt1_cs"]])
# Plot reco pT with cut on GMT pT and usable charge
rateList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-gmtPt1_us"]])
# Plot reco pT with cut on GMT pT and correct charge
rateList.append(["trailingMu_recoPt", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-gmtPt1_cs"]])
# Plot reco pT with cut on GMT pT and usable charge
rateList.append(["trailingMu_recoPt", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-gmtPt1_us"]])


rateList.append(["leadingMu_recoPt_central", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-recoPt1-central"]])
rateList.append(["trailingMu_recoPt_central", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-recoPt1-central"]])
rateList.append(["leadingMu_recoPt_forward", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-recoPt1-forward"]])
rateList.append(["trailingMu_recoPt_forward", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-recoPt1-forward"]])
rateList.append(["leadingMu_recoPt_brl", binningDict["pt25Fine"], "pT1_reco",
                 cutDict["diMu-recoPt1-brl"]])
rateList.append(["trailingMu_recoPt_brl", binningDict["pt25Fine"], "pT2_reco",
                 cutDict["diMu-recoPt1-brl"]])

rateList.append(["jPsi_InvMass", binningDict["invMassFine"], "InvMass_dimuon",
                 cutDict["jpsi-Pt1"]])
rateList.append(["jPsi_recoEta", binningDict["etaFine"], "Eta_dimuon",
                 cutDict["jpsi-Pt1"]])
rateList.append(["jPsi_recoEta", binningDict["etaFine"], "Eta_dimuon",
                 cutDict["jpsi-Pt1_cs"]])
rateList.append(["jPsi_recoEta", binningDict["etaFine"], "Eta_dimuon",
                 cutDict["jpsi-Pt1_us"]])
rateList.append(["jPsi_recoPt", binningDict["pt25Fine"], "pT_dimuon",
                 cutDict["jpsi-Pt1"]])
rateList.append(["jPsi_recoPt", binningDict["pt25Fine"], "pT_dimuon",
                 cutDict["jpsi-Pt1_cs"]])
rateList.append(["jPsi_recoPt", binningDict["pt25Fine"], "pT_dimuon",
                 cutDict["jpsi-Pt1_us"]])

for varList in efficiencyList:
    generateCombinedEfficiencyHist(varList, "DiMuNtuple.root",
                                   "DiMuNtupleMC.root", dataset, datasetMC)

for varList in rateList:
    generateCombinedRateHist(varList, "DiMuNtuple.root", "DiMuNtupleMC.root",
                             dataset, datasetMC)
