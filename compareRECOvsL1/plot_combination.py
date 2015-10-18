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

# #TODO:0 Cut on inv mass between 3 and 3.2 for stack plots!

efficiencyList = []
# Entries:
# Label (for filename and axis) | binning | parameters for project functions
efficiencyList.append([["deltaR", "#DeltaR(#mu^{-}#mu^{+})"],
                       binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
# pT plots
efficiencyList.append([["leadingMu_recoPt", "p_{T}(leading #mu) [GeV/c]"],
                       binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPt", "p_{T}(trailing #mu) [GeV/c]"],
                       binningDict["pt25Fine"], "pT2_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["jPsi_recoPt", "p_{T}(J/#Psi) [GeV/c]"],
                       binningDict["pt25Fine"], "pT_dimuon",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
# efficiencyList.append([["jPsi_recoPt", "p_{T}(J/#Psi) [GeV/c]"],
#                        binningDict["pt25Fine"], "pT_dimuon",
#                        cutDict["jpsi-Pt1-central_us"],
#                        cutDict["jpsi-Pt1-central"]])
# eta plots
efficiencyList.append([["leadingMu_recoEta", "#eta(leading #mu)"],
                       binningDict["etaFine_centralRegion"], "Eta1_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["trailingMu_recoEta", "#eta(trailing #mu)"],
                       binningDict["etaFine_centralRegion"], "Eta2_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["jPsi_recoEta", "#eta(J/#Psi)"],
                       binningDict["etaFine_centralRegion"], "Eta_dimuon",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
# efficiencyList.append([["jPsi_recoEta", "#eta(J/#Psi)"],
#                        binningDict["etaFine_centralRegion"], "Eta_dimuon",
#                        cutDict["jpsi-Pt1-central_us"],
#                        cutDict["jpsi-Pt1-central"]])
# phi plots
efficiencyList.append([["leadingMu_recoPhi", "#phi (leading #mu)"],
                       binningDict["phiFine"], "Phi1_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPhi", "#phi(trailing #mu)"],
                       binningDict["phiFine"], "Phi2_reco",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["jPsi_recoPhi", "#phi(J/#Psi)"],
                       binningDict["phiFine"], "Phi_dimuon",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
# efficiencyList.append([["jPsi_recoPhi", "#phi(J/#Psi)"],
#                        binningDict["phiFine"], "Phi_dimuon",
#                        cutDict["jpsi-Pt1-central_us"],
#                        cutDict["jpsi-Pt1-central"]])
# invariant mass
efficiencyList.append([["jPsi_InvMass", "M(#mu^{+}#mu^{-}) [GeV/c^{2}]"],
                       binningDict["invMassFine"], "InvMass_dimuon",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_cs"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
efficiencyList.append([["jPsi_InvMass", "M(#mu^{+}#mu^{-}) [GeV/c^{2}]"],
                       binningDict["invMassFine"], "InvMass_dimuon",
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-mass3to32-central_etagmt"]])
# efficiencyList.append([["jPsi_InvMass", "M(#mu^{+}#mu^{-}) [GeV/c^{2}]"],
#                        binningDict["invMassFine"], "InvMass_dimuon",
#                        cutDict["jpsi-Pt1-central_cs"],
#                        cutDict["jpsi-Pt1-central"]])
# efficiencyList.append([["jPsi_InvMass", "M(#mu^{+}#mu^{-}) [GeV/c^{2}]"],
#                        binningDict["invMassFine"], "InvMass_dimuon",
#                        cutDict["jpsi-Pt1-central_us"],
#                        cutDict["jpsi-Pt1-central"]])


for varList in efficiencyList:
    generateCombinedEfficiencyHist(varList, "DiMuNtuple.root",
                                   "DiMuNtupleMC.root", dataset, datasetMC)
