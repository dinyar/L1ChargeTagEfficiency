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
# Entries:
# Label (for filename and axis) | binning | parameters for project functions
efficiencyList.append([["deltaR", "#mbox{#DeltaR()}#mbox{#mu}^#mbox{-}#mbox{#mu}^#mbox{+}#mbox{)}"], binningDict["distWideFine"],
                       "sqrt((Eta1_reco-Eta2_reco)**2+\
                       (Phi1_reco-Phi2_reco)**2)",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
# pT plots
efficiencyList.append([["leadingMu_recoPt", "#mbox{p}_{#mbox{T}}#mbox{(leading #mu)} #mbox{[GeV/c]}"], binningDict["pt25Fine"], "pT1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPt", "#mbox{p}_{#mbox{T}}#mbox{(trailing #mu)} #mbox{[GeV/c]}"], binningDict["pt25Fine"],
                       "pT2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoPt", "#mbox{p}_{#mbox{T}}#mbox{(J/#Psi)} #mbox{[GeV/c]}"], binningDict["pt25Fine"], "pT_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# eta plots
efficiencyList.append([["leadingMu_recoEta", "#mbox{#eta(leading #mu)}"],
                       binningDict["etaFine_centralRegion"], "Eta1_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoEta", "#mbox{#eta(trailing #mu)}"],
                       binningDict["etaFine_centralRegion"], "Eta2_reco",
                       cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoEta", "#mbox{#eta(J/#Psi)}"], binningDict["etaFine_centralRegion"],
                       "Eta_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# phi plots
efficiencyList.append([["leadingMu_recoPhi", "#mbox{#phi (leading #mu)}"], binningDict["phiFine"],
                       "Phi1_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["trailingMu_recoPhi", "#mbox{#phi(trailing #mu)}"], binningDict["phiFine"],
                       "Phi2_reco", cutDict["diMu-gmtPt1-central_etagmt_us"],
                       cutDict["diMu-gmtPt1-central_etagmt"]])
efficiencyList.append([["jPsi_recoPhi", "#mbox{#phi(J/#Psi)}"], binningDict["phiFine"], "Phi_dimuon",
                       cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])
# invariant mass
efficiencyList.append([["jPsi_InvMass", "#mbox{M}#mbox{(#mu}^#mbox{-}#mbox{#mu}^#mbox{+}#mbox{)} #mbox{[GeV/c}^#mbox{2}#mbox{]}"], binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_cs"],
                       cutDict["jpsi-Pt1-central"]])
efficiencyList.append([["jPsi_InvMass", "#mbox{M}#mbox{(#mu}^#mbox{-}#mbox{#mu}^#mbox{+}#mbox{)} #mbox{[GeV/c}^#mbox{2}#mbox{]}"], binningDict["invMassFine"],
                       "InvMass_dimuon", cutDict["jpsi-Pt1-central_us"],
                       cutDict["jpsi-Pt1-central"]])


for varList in efficiencyList:
    generateCombinedEfficiencyHist(varList, "DiMuNtuple.root",
                                   "DiMuNtupleMC.root", dataset, datasetMC)
