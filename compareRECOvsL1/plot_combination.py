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

efficiencyList = []
# #Doing:10 Axis labels
# Entries:
# Label (for filename and title) | binning | parameters for project functions
efficiencyList.append(["deltaR", binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
# pT plots
efficiencyList.append(["leadingMu_recoPt", binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoPt", binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["jPsi_recoPt", binningDict["pt25Fine"], "pT_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# eta plots
efficiencyList.append(["leadingMu_recoEta",
                       binningDict["etaFine_centralRegion"], "Eta1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoEta",
                       binningDict["etaFine_centralRegion"], "Eta2_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["jPsi_recoEta", binningDict["etaFine_centralRegion"],
                       "Eta_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# phi plots
efficiencyList.append(["leadingMu_recoPhi", binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["trailingMu_recoPhi", binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append(["jPsi_recoPhi", binningDict["phiFine"], "Phi_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# invariant mass
efficiencyList.append(["jPsi_InvMass", binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_cs"],
                       cutDict["jpsi-Pt1-central"]])
efficiencyList.append(["jPsi_InvMass", binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])


for varList in efficiencyList:
    generateCombinedEfficiencyHist(varList, "DiMuNtuple.root",
                                   "DiMuNtupleMC.root", dataset, datasetMC)
