#!/usr/bin/python

from ROOT import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../L1AnalysisHelpers"))
from CreateHistograms import *

gROOT.Reset()
gROOT.SetBatch(kTRUE);

efficiencyList = []
# TODO: Axis labels
# Entries: Label for histogram (Will be used for filename and title) | binning | parameters used for project functions
efficiencyList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_cs"], cutDict["recoPt5"], []])
efficiencyList.append(["mu1_recoPt", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoPt", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoPt", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoPt", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
efficiencyList.append(["mu1_recoEta", 25, -2.6, 2.6, "Eta1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoEta", 25, -2.6, 2.6, "Eta1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoEta", 25, -2.6, 2.6, "Eta2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoEta", 25, -2.6, 2.6, "Eta2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
efficiencyList.append(["mu1_recoPhi", 25, -3.2, 3.2, "Phi1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoPhi", 25, -3.2, 3.2, "Phi1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoPhi", 25, -3.2, 3.2, "Phi2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoPhi", 25, -3.2, 3.2, "Phi2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
efficiencyList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_us"], cutDict["recoPt5"], []])
efficiencyList.append(["mu1_recoPt", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoPt", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoPt", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoPt", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
efficiencyList.append(["mu1_recoEta", 25, -2.6, 2.6, "Eta1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoEta", 25, -2.6, 2.6, "Eta1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoEta", 25, -2.6, 2.6, "Eta2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoEta", 25, -2.6, 2.6, "Eta2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
efficiencyList.append(["mu1_recoPhi", 25, -3.2, 3.2, "Phi1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu1_recoPhi", 25, -3.2, 3.2, "Phi1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu1"]])
efficiencyList.append(["mu2_recoPhi", 25, -3.2, 3.2, "Phi2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], []])
efficiencyList.append(["mu2_recoPhi", 25, -3.2, 3.2, "Phi2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"], stackCutDict["subsystems_mu2"]])
# TODO: Add invariant calculation.
# TODO: Add 2-D hist showing efficiency for pT of both muons.

rateList = []
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["recoPt5"]])
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_cs"]])
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_us"]])
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["recoPt1"]]) # Plot reco pT with cut on reco pT
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["recoPt1"]]) # Plot reco pT with cut on reco pT
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_cs"]]) # Plot reco pT with cut on GMT pT and correct charge
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_us"]]) # Plot reco pT with cut on GMT pT and usable charge
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_cs"]]) # Plot reco pT with cut on GMT pT and correct charge
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_us"]]) # Plot reco pT with cut on GMT pT and usable charge

eff2Dlist = []
# eff2Dlist.append(["mu1_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "pT1_reco:Eta1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
eff2Dlist.append(["mu1_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta1_reco:pT1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
eff2Dlist.append(["mu2_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta2_reco:pT2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
eff2Dlist.append(["mu1_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta1_reco:pT1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"]])
eff2Dlist.append(["mu2_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta2_reco:pT2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"]])

rate2Dlist = []
rate2Dlist.append(["mu1_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta1_reco:pT1_reco", cutDict["gmtPt1_cs"]])
rate2Dlist.append(["mu2_recoPtEta", 25, 0, 50, 25, -2.6, 2.6, "Eta2_reco:pT2_reco", cutDict["gmtPt1_cs"]])

f = TFile.Open("DiMuNtuple.root")

ntuple = f.Get("ntuple")

dataset = "2012D-Muonia"
for varList in efficiencyList:
    generateEfficiencyHist(varList, dataset)

for varList in rateList:
    generateRateHist(varList, dataset)

for varList in eff2Dlist:
    generate2DEfficiencyHist(varList, dataset)

for varList in rate2Dlist:
    generate2DRateHist(varList, dataset)
