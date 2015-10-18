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
# #TODO:10 Axis labels
# Entries:
# Label (for filename and title) | binning | parameters for project functions
efficiencyList.append([["deltaR", "TODO"], binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
# pT plots
efficiencyList.append([["leadingMu_recoPt", "TODO"], binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPt", "TODO"], binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoPt", "TODO"], binningDict["pt25Fine"], "pT_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# eta plots
efficiencyList.append([["leadingMu_recoEta", "TODO"],
                       binningDict["etaFine_centralRegion"], "Eta1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoEta", "TODO"],
                       binningDict["etaFine_centralRegion"], "Eta2_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoEta", "TODO"], binningDict["etaFine_centralRegion"],
                       "Eta_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# phi plots
efficiencyList.append([["leadingMu_recoPhi", "TODO"], binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPhi", "TODO"], binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoPhi", "TODO"], binningDict["phiFine"], "Phi_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# invariant mass
efficiencyList.append([["jPsi_InvMass", "TODO"], binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_cs"],
                       cutDict["jpsi-Pt1-central"]])
efficiencyList.append([["jPsi_InvMass", "TODO"], binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])


stackList = []
# pT plots
stackList.append([["leadingMu_recoPt", "TODO"], binningDict["pt25Fine"], "pT1_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu1"]])
stackList.append([["trailingMu_recoPt", "TODO"], binningDict["pt25Fine"], "pT2_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu2"]])
# eta plots
stackList.append([["leadingMu_recoEta", "TODO"], binningDict["etaFine"], "Eta1_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu1"]])
stackList.append([["trailingMu_recoEta", "TODO"], binningDict["etaFine"], "Eta2_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu2"]])
# phi plots
stackList.append([["leadingMu_recoPhi", "TODO"], binningDict["phiFine"], "Phi1_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu1"]])
stackList.append([["trailingMu_recoPhi", "TODO"], binningDict["phiFine"], "Phi2_reco",
                  cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"],
                  stackCutDict["subsystems_mu2"]])

rateList = []

for varList in efficiencyList:
    generateEfficiencyHist(varList, "DiMuNtuple.root", dataset)

for varList in stackList:
    generateEfficiencyStack(varList, "DiMuNtuple.root", dataset)

for varList in rateList:
    generateRateHist(varList, "DiMuNtuple.root", dataset)
