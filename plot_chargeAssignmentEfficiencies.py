#!/usr/bin/python

from ROOT import *

def generateEfficiencyHist(varList):
    gStyle.SetOptStat(0)
    c1 = TCanvas('c1', "Efficiency vs. " + varList[0] + " - " + varList[5][1] + ", " + varList[6][1], 200, 10, 700, 500)
    tmpHist = TH1D("tmpHist", "", varList[1], varList[2], varList[3])
    efficiencyHist = TH1D("effHist", "Efficiency vs. " + varList[0] + " - " + varList[5][1] + ", " + varList[6][1], varList[1], varList[2], varList[3])
    ntuple.Project("tmpHist", varList[4], "1*" + varList[6][0])
    ntuple.Project("effHist", varList[4], "1*" + varList[5][0])
    efficiencyHist.Divide(tmpHist)
    efficiencyHist.DrawCopy()
    c1.Update()
    c1.Print("plots/hist_eff_"+varList[0]+"_"+varList[5][1] + "_" + varList[6][1]+".pdf", "pdf")

def generate2DEfficiencyHist(varList):
    gStyle.SetOptStat(0)
    c1 = TCanvas('c1', "Efficiency vs. " + varList[0] + " - " + varList[8][1] + ", " + varList[9][1], 200, 10, 700, 500)
    tmpHist = TH2D("tmpHist", "", varList[1], varList[2], varList[3], varList[4], varList[5], varList[6])
    efficiencyHist = TH1D("effHist", "Efficiency vs. " + varList[0] + " - " + varList[8][1] + ", " + varList[9][1], varList[1], varList[2], varList[3], varList[4], varList[5], varList[6])
    ntuple.Project("tmpHist", varList[7], "1*" + varList[9][0])
    ntuple.Project("effHist", varList[7], "1*" + varList[8][0])
    efficiencyHist.Divide(tmpHist)
    efficiencyHist.DrawCopy()
    c1.Update()
    c1.Print("plots/hist2D_eff_"+varList[0]+"_"+varList[8][1] + "_" + varList[9][1]+".pdf", "pdf")

def generateRateHist(varList):
    c1 = TCanvas('c1', "Rate of " + varList[0] + " - " + varList[5][1], 200, 10, 700, 500)
    rateHist = TH1D("rateHist", "Rate of " + varList[0] + " - " + varList[5][1], varList[1], varList[2], varList[3])
    ntuple.Project("rateHist", varList[4], "1*" + varList[5][0])
    rateHist.DrawCopy()
    c1.Update()
    c1.Print("plots/hist_rate_"+varList[0]+"_"+varList[5][1]+".pdf", "pdf")

gROOT.Reset()

correctCharges = "(Ch1_GMT == Ch1_reco) && (Ch2_GMT == Ch2_reco)"
usableCharges = "((Ch1_GMT == Ch1_reco) && (Ch2_GMT == Ch2_reco)) || ((Ch1_GMT != Ch1_reco) && (Ch2_GMT != Ch2_reco))"
cutDict = {}
cutDict["recoPt1"] = ["((pT1_reco>1) && (pT2_reco>1))", "DiRecoMu1"]
cutDict["gmtPt1_cs"] = ["((pT1_GMT>1) && (pT2_GMT>1) &&" + correctCharges + ")", "DiGMTMu1_CorrectSign"]
cutDict["gmtPt1_us"] = ["((pT1_GMT>1) && (pT2_GMT>1) &&" + usableCharges + ")", "DiGMTMu1_UsableSign"]
cutDict["recoPt5"] = ["((pT1_reco>5) && (pT2_reco>5))", "DiRecoMu5"]
cutDict["gmtPt5_cs"] = ["((pT1_GMT>5) && (pT2_GMT>5) &&" + correctCharges + ")", "DiGMTMu5_CorrectSign"]
cutDict["gmtPt5_us"] = ["((pT1_GMT>5) && (pT2_GMT>5) &&" + usableCharges + ")", "DiGMTMu5_UsableSign"]

efficiencyList = []
# TODO: Axis labels, think about more descriptive title.
# TODO: Can combine/infer stuff: Efficiency implies GMT/reco;
# Entries: Label for histogram (Will be used for filename and title) | binning | parameters used for project functions
efficiencyList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_cs"], cutDict["recoPt5"]])
efficiencyList.append(["pT1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
efficiencyList.append(["pT2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_cs"], cutDict["recoPt1"]])
efficiencyList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_us"], cutDict["recoPt5"]])
efficiencyList.append(["pT1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"]])
efficiencyList.append(["pT2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_us"], cutDict["recoPt1"]])
# TODO: Add invariant calculation.
# TODO: Add 2-D hist showing efficiency for pT of both muons.

rateList = []
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["recoPt5"]])
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_cs"]])
rateList.append(["deltaR_reco", 63, 0, 2, "sqrt((Eta1_reco-Eta2_reco)**2+(Phi1_reco-Phi2_reco)**2)", cutDict["gmtPt5_us"]])
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["recoPt1"]])
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["recoPt1"]])
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_cs"]])
rateList.append(["pt1_reco", 25, 0, 50, "pT1_reco", cutDict["gmtPt1_us"]])
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_cs"]])
rateList.append(["pt2_reco", 25, 0, 50, "pT2_reco", cutDict["gmtPt1_us"]])

f = TFile.Open("DiMuNtuple.root")

ntuple = f.Get("ntuple")

for varList in efficiencyList:
    generateEfficiencyHist(varList)

for varList in rateList:
    generateRateHist(varList)
