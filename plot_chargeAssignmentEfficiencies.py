#!/usr/bin/python

from ROOT import *
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "../L1AnalysisHelpers"))
from CreateHistograms import *
from dataset_name import *

gROOT.Reset()
gROOT.SetBatch(kTRUE);

efficiencyList = []
# TODO: Axis labels
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
# TODO: Add invariant calculation.
# TODO: Add 2-D hist showing efficiency for pT of both muons.

stackList = []
stackList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])
stackList.append(["mu1_recoEta", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoEta", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])
stackList.append(["mu1_recoPhi", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoPhi", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])
stackList.append(["mu1_recoPt", binningDict["pt25Fine"], "pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoPt", binningDict["pt25Fine"], "pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])
stackList.append(["mu1_recoEta", binningDict["etaFine"], "Eta1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoEta", binningDict["etaFine"], "Eta2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])
stackList.append(["mu1_recoPhi", binningDict["phiFine"], "Phi1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu1"]])
stackList.append(["mu2_recoPhi", binningDict["phiFine"], "Phi2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"], stackCutDict["subsystems_mu2"]])

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

eff2Dlist = []
# eff2Dlist.append(["mu1_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "pT1_reco:Eta1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
eff2Dlist.append(["mu1_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta1_reco:pT1_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
eff2Dlist.append(["mu2_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta2_reco:pT2_reco", cutDict["diMu-gmtPt1_cs"], cutDict["diMu-gmtPt1"]])
eff2Dlist.append(["mu1_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta1_reco:pT1_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])
eff2Dlist.append(["mu2_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta2_reco:pT2_reco", cutDict["diMu-gmtPt1_us"], cutDict["diMu-gmtPt1"]])

rate2Dlist = []
rate2Dlist.append(["mu1_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta1_reco:pT1_reco", cutDict["diMu-gmtPt1_cs"]])
rate2Dlist.append(["mu2_recoPtEta", binningDict["pt25Fine"], binningDict["etaFine"], "Eta2_reco:pT2_reco", cutDict["diMu-gmtPt1_cs"]])

for varList in efficiencyList:
    generateEfficiencyHist(varList, "DiMuNtuple.root", dataset)

for varList in stackList:
    generateEfficiencyStack(varList, "DiMuNtuple.root", dataset)

for varList in rateList:
    generateRateHist(varList, "DiMuNtuple.root", dataset)

for varList in eff2Dlist:
    generate2DEfficiencyHist(varList, "DiMuNtuple.root", dataset)

for varList in rate2Dlist:
    generate2DRateHist(varList, "DiMuNtuple.root", dataset)
