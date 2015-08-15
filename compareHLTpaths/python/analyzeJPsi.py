#! /usr/bin/env python

import ROOT
import math
import tdrstyle
from itertools import izip
from collections import namedtuple
from DataFormats.FWLite import Events, Handle


def makeHistogram(title, binning, quantity):
    histo = ROOT.TH1F(title, "", binning[0],
                      binning[1], binning[2])
    histo.SetMinimum(0)
    if quantity == "mass":
        histo.GetXaxis().SetTitle("J/Psi mass [GeV/c]")
        histo.GetXaxis().SetLabelOffset(0.0100000000000000002)
        histo.GetYaxis().SetLabelOffset(0.0100000000000000002)
        histo.GetYaxis().SetTitleOffset(1.4)
    elif quantity == "eta":
        histo.GetXaxis().SetTitle("#mbox{#eta}")
        histo.GetYaxis().SetTitleOffset(1.3)
    elif quantity == "phi":
        histo.GetXaxis().SetTitle("#mbox{#phi}")
    elif quantity == "pt":
        histo.GetXaxis().SetTitle("#mbox{p}_{#mbox{T}} #mbox{[GeV/c]}")
        histo.GetYaxis().SetTitleOffset(1.3)
    else:
        histo.GetXaxis().SetTitle("")
    histo.GetYaxis().SetTitle("Counts")

    return histo


# Create histograms, etc.
def plotJPsi(events, label, handle, plottingVariables):
    events_noOS.toBegin()
    events_OSrequired.toBegin()

    # Book histograms
    particleHistorgrams = []
    for plottingVar in plottingVariables:
        histo = makeHistogram(plottingVar.title, plottingVar.binning,
                              plottingVar.quantity)
        particleHistorgrams.append(histo)

    # loop over events
    for event in events:
        # use getByLabel, just like in cmsRun
        event.getByLabel(label, handle)
        # get the product
        muons = handle.product()
        # use muons to make J/Psi peak
        numMuons = len(muons)
        if muons < 2:
            continue
        for outer in xrange(numMuons - 1):
            outerMuon = muons[outer]
            if (not outerMuon.isGlobalMuon()):
                continue
            for inner in xrange(outer + 1, numMuons):
                innerMuon = muons[inner]
                if (not innerMuon.isGlobalMuon()):
                    continue
                if outerMuon.charge() * innerMuon.charge() >= 0:
                    continue
                inner4v = ROOT.TLorentzVector(innerMuon.px(), innerMuon.py(),
                                              innerMuon.pz(),
                                              innerMuon.energy())
                outer4v = ROOT.TLorentzVector(outerMuon.px(), outerMuon.py(),
                                              outerMuon.pz(),
                                              outerMuon.energy())
                jpsi = (inner4v + outer4v)

                if outer4v.Pt() > inner4v.Pt():
                    leadingMuon = outer4v
                    trailingMuon = inner4v
                else:
                    leadingMuon = inner4v
                    trailingMuon = outer4v

                for plottingVar, hist in izip(plottingVariables,
                                              particleHistorgrams):
                    if len(plottingVar.ptCut) > 0:
                        if (jpsi.Pt() < plottingVar.ptCut[0]):
                            continue
                        if (jpsi.Pt() > plottingVar.ptCut[1]):
                            continue

                    # Select only J/Psi candidates with the correct mass
                    if plottingVar.massCut[0] < plottingVar.massCut[1]:
                        if (jpsi.M() < plottingVar.massCut[0]) or \
                           (jpsi.M() > plottingVar.massCut[1]):
                            continue
                    else:
                        if (jpsi.M() <= plottingVar.massCut[0]) and \
                           (jpsi.M() >= plottingVar.massCut[1]):
                            continue

                    if plottingVar.particleSelector == 0:
                        plotParticle = jpsi
                    elif plottingVar.particleSelector == 1:
                        plotParticle = leadingMuon
                    elif plottingVar.particleSelector == 2:
                        plotParticle = trailingMuon

                    if plottingVar.quantity == "mass":
                        hist.Fill(plotParticle.M())
                    elif plottingVar.quantity == "eta":
                        hist.Fill(plotParticle.Eta())
                    elif plottingVar.quantity == "phi":
                        hist.Fill(plotParticle.Phi())
                    elif plottingVar.quantity == "pt":
                        hist.Fill(plotParticle.Pt())

    return particleHistorgrams


def makeJPsiPlots(label, handle, plottingVariables):
    ROOT.gROOT.SetBatch()        # don't pop up canvases
    # ROOT.gROOT.SetStyle('Plain') # white background
    # ROOT.gStyle.SetOptStat(0)    # No statistics
    # ROOT.gStyle.SetLegendFont(32)
    # ROOT.gStyle.SetTitleFont(32, "xyz")
    # ROOT.gStyle.SetLabelFont(32, "xyz")
    # ROOT.gStyle.SetStatFont(32)
    # ROOT.gStyle.SetLegendBorderSize(0)
    ROOT.gStyle.SetErrorX(0)

    tdrstyle.setTDRStyle()

    jpsiHists_noOS = plotJPsi(events_noOS, label, handle, plottingVariables)
    jpsiHists_OSrequired = plotJPsi(events_OSrequired, label, handle,
                                    plottingVariables)

    # Modify all below. Put it in loop!
    for jpsiHist_OSreq, jpsiHist_noOS, plotVar in izip(jpsiHists_OSrequired,
                                                       jpsiHists_noOS,
                                                       plottingVariables):
        jpsiHist_OSreq.Sumw2()
        jpsiHist_noOS.Sumw2()

        # Draw histograms
        c1 = ROOT.TCanvas("", "", 1024, 786)
        jpsiHist_noOS.SetLineColor(ROOT.kRed)
        jpsiHist_noOS.DrawCopy("E1HIST")
        jpsiHist_OSreq.SetLineColor(ROOT.kBlue)
        jpsiHist_OSreq.DrawCopy("E1HISTSAME")
        legend = ROOT.TLegend(plotVar.legendPositions[0][0],
                              plotVar.legendPositions[0][1],
                              plotVar.legendPositions[0][2],
                              plotVar.legendPositions[0][3])
        legend.SetTextSize(0.0275)
        if (len(plotVar.ptCut) > 0):
            # legend.SetFillStyle(0)
            legend.AddEntry(jpsiHist_noOS,
                            "#splitline{\
                            HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1;}{" +
                            plotVar.ptCut[2] + "}", "LEP")
            legend.AddEntry(jpsiHist_OSreq,
                            "#splitline{\
                            HLT_Dimuon0er16_Jpsi_NoVertexing_v1;}{" +
                            plotVar.ptCut[2] + "}", "LEP")
        else:
            # legend = ROOT.TLegend(0.47,0.87,0.99,0.99)
            # legend.SetFillStyle(0)
            # legend.SetTextSize(0.0275)
            legend.AddEntry(jpsiHist_noOS,
                            "HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1", "LEP")
            legend.AddEntry(jpsiHist_OSreq,
                            "HLT_Dimuon0er16_Jpsi_NoVertexing_v1", "LEP")
        legend.Draw("SAME")
        c1.Print(plotVar.title + ".png")
        c1.Print(plotVar.title + ".pdf")

        # Plot efficiencies
        c2 = ROOT.TCanvas("", "", 1024, 786)
        # legend_ratio = ROOT.TLegend(0.78,0.91,0.99,0.99)
        legend_ratio = ROOT.TLegend(plotVar.legendPositions[1][0],
                                    plotVar.legendPositions[1][1],
                                    plotVar.legendPositions[1][2],
                                    plotVar.legendPositions[1][3])
        legend_ratio.SetTextSize(0.0275)
        # legend_ratio.SetFillStyle(0)
        jpsiHist_ratio = ROOT.TH1F("jpsiratio", "", plotVar.binning[0],
                                   plotVar.binning[1],
                                   plotVar.binning[2])
        jpsiHist_ratio.Sumw2()
        jpsiHist_ratio.SetLineColor(ROOT.kBlue)
        jpsiHist_ratio.Divide(jpsiHist_OSreq, jpsiHist_noOS, 1.0, 1.0)
        jpsiHist_ratio.SetMinimum(0)
        if plotVar.quantity == "mass":
            jpsiHist_ratio.GetXaxis().SetTitle("J/Psi mass [GeV/c]")
            jpsiHist_ratio.GetXaxis().SetLabelOffset(0.0100000000000000002)
            jpsiHist_ratio.GetYaxis().SetLabelOffset(0.0100000000000000002)
        elif plotVar.quantity == "eta":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{#eta}")
        elif plotVar.quantity == "phi":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{#phi}")
        elif plotVar.quantity == "pt":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{p}_{#mbox{T}} \
            #mbox{[GeV/c]}")
        else:
            jpsiHist_ratio.GetXaxis().SetTitle("")
        jpsiHist_ratio.GetYaxis().SetTitle("OS required/no OS")
        jpsiHist_ratio.Draw("E1HIST")
        if (len(plotVar.ptCut) > 0):
            legend_ratio.AddEntry(jpsiHist_ratio, plotVar.ptCut[2], "LEP")
            legend_ratio.Draw("SAME")
        line = ROOT.TLine(plotVar.binning[1], 1, plotVar.binning[2], 1)
        line.SetLineColor(ROOT.kRed)
        line.Draw("SAME")
        c2.Print(plotVar.title + "_ratio.png")
        c2.Print(plotVar.title + "_ratio.pdf")

        # Compute overall efficiency
        nJPsi_noOS = jpsiHist_noOS.Integral()
        nJPsi_OSrequired = jpsiHist_OSreq.Integral()
        print "J/Psi candidates with OS required: " + str(nJPsi_OSrequired)
        print "J/Psi candidates without OS required: " + str(nJPsi_noOS)
        totalEffError = nJPsi_OSrequired/nJPsi_noOS * \
            math.sqrt((1/nJPsi_noOS) + (1/nJPsi_OSrequired))
        print "Efficiency: " + str(nJPsi_OSrequired/nJPsi_noOS) + \
            "+/-" + str(totalEffError)


f_noOS = ROOT.TFile.Open("../../../charmonium_HLT_noOS.root")
f_OSrequired = ROOT.TFile.Open("../../../charmonium_HLT_OSrequired.root")
events_noOS = Events(f_noOS)
events_OSrequired = Events(f_OSrequired)

# create handle outside of loop
handle = Handle("std::vector<pat::Muon>")

# for now, label is just a tuple of strings that is initialized just
# like and edm::InputTag
label = ("selectedPatMuons")

# Structure to hold plotting data
# particleSelector: 0 = DiMuon; 1 = Leading muon; 2 = Second leading muon
PlottingVariables = namedtuple("PlottingVariables", ["quantity", "binning",
                                                     "title", "ptCut",
                                                     "massCut",
                                                     "particleSelector",
                                                     "legendPositions"])

# Binning lists
binning_background = [10, 0, 10]
binning_mass = [25, 2.9, 3.4]
binning_eta = [16, -1.6, 1.6]
binning_pT = [35, 0, 35]
binning_pT_restricted = [12, 3, 15]

binning_mu_eta = [16, -1.6, 1.6]
binning_mu_pT = [20, 0, 20]


# Cuts
background_outside3to3_2 = [3.2, 3, ""]
background_outside2_8to3_4 = [3.4, 2.8, ""]
mass_3to3_2 = [3, 3.2, ""]
pT_3to15 = [3, 15, "#mbox{p}_{#mbox{T}}#mbox{(J/Psi) in [3, 15] GeV/c}"]


# Particle selector
diMu = 0
leadingMu = 1
trailingMu = 2

# Legend position (left edge) possibilities
upperRight = [0.5, 0.75, 0.65, 0.9]
upperLeft = [0.2, 0.75, 0.25, 0.9]
lowerRight = [0.5, 0.2, 0.65, 0.35]
lowerLeft = [0.2, 0.2, 0.35, 0.35]
topCenter = [0.4, 0.75, 0.45, 0.9]
bottomCenter = [0.4, 0.3, 0.45, 0.35]
upperRight_narrow = [0.5, 0.8, 0.65, 0.9]
upperLeft_narrow = [0.2, 0.8, 0.25, 0.9]
lowerRight_narrow = [0.5, 0.2, 0.65, 0.3]
lowerLeft_narrow = [0.2, 0.2, 0.25, 0.3]
topCenter_narrow = [0.4, 0.8, 0.45, 0.9]
bottomCenter_narrow = [0.4, 0.3, 0.45, 0.3]

defaultLegendPositions = [upperRight, upperRight]

# Construct plotting variables
plotBackgrnd_ex3to3_2 = PlottingVariables(quantity="mass",
                                          binning=binning_background,
                                          title="background_ex3to3_2",
                                          ptCut=[],
                                          massCut=background_outside3to3_2,
                                          particleSelector=diMu,
                                          legendPositions=[upperRight,
                                                           upperLeft_narrow])
plotBackgrnd_ex2_8to3_4 = PlottingVariables(quantity="mass",
                                            binning=binning_background,
                                            title="background_ex2_8to3_4",
                                            ptCut=[],
                                            massCut=background_outside2_8to3_4,
                                            particleSelector=diMu,
                                            legendPositions=[upperRight,
                                                             upperLeft_narrow])
plotMass = PlottingVariables(quantity="mass", binning=binning_mass,
                             title="jpsiMass", ptCut=[], massCut=mass_3to3_2,
                             particleSelector=diMu,
                             legendPositions=[upperRight, upperLeft_narrow])
plotMass_pT3to15 = PlottingVariables(quantity="mass",
                                     binning=binning_mass,
                                     title="jpsiMass_3-15GeV",
                                     ptCut=pT_3to15, massCut=mass_3to3_2,
                                     particleSelector=diMu,
                                     legendPositions=[upperRight,
                                                      upperLeft_narrow])
plotPt = PlottingVariables(quantity="pt", binning=binning_pT, title="jpsiVsPt",
                           ptCut=[], massCut=mass_3to3_2,
                           particleSelector=diMu,
                           legendPositions=[upperRight, upperLeft_narrow])
plotPt_pT3to15 = PlottingVariables(quantity="pt",
                                   binning=binning_pT_restricted,
                                   title="jpsiVsPt_3-15GeV",
                                   ptCut=pT_3to15, massCut=mass_3to3_2,
                                   particleSelector=diMu,
                                   legendPositions=[bottomCenter,
                                                    upperRight_narrow])
plotEta = PlottingVariables(quantity="eta", binning=binning_eta,
                            title="jpsiVsEta", ptCut=[], massCut=mass_3to3_2,
                            particleSelector=diMu,
                            legendPositions=[lowerLeft, lowerLeft_narrow])
plotEta_pT3to15 = PlottingVariables(quantity="eta", binning=binning_eta,
                                    title="jpsiVsEta_3-15GeV",
                                    ptCut=pT_3to15, massCut=mass_3to3_2,
                                    particleSelector=diMu,
                                    legendPositions=[lowerLeft,
                                                     lowerLeft_narrow])

plotLeadingMuPt = PlottingVariables(quantity="pt", binning=binning_mu_pT,
                                    title="leadingMuVsPt", ptCut=[],
                                    massCut=mass_3to3_2,
                                    particleSelector=leadingMu,
                                    legendPositions=[upperRight,
                                                     upperLeft_narrow])
plotLeadingMuPt_pT3to15 = PlottingVariables(quantity="pt",
                                            binning=binning_mu_pT,
                                            title="\
                                            leadingMuVsPt-restr_jpsiPt_3-15GeV\
                                            ",
                                            ptCut=pT_3to15,
                                            massCut=mass_3to3_2,
                                            particleSelector=leadingMu,
                                            legendPositions=[upperRight,
                                                             lowerRight_narrow
                                                             ])
plotLeadingMuEta = PlottingVariables(quantity="eta", binning=binning_mu_eta,
                                     title="leadingMuVsEta", ptCut=[],
                                     massCut=mass_3to3_2,
                                     particleSelector=leadingMu,
                                     legendPositions=[lowerLeft,
                                                      lowerLeft_narrow])
plotLeadingMuEta_pT3to15 = PlottingVariables(quantity="eta",
                                             binning=binning_mu_eta,
                                             title="\
                                            leadingMuVsEta-restr_jpsiPt_3-15GeV\
                                             ",
                                             ptCut=pT_3to15,
                                             massCut=mass_3to3_2,
                                             particleSelector=leadingMu,
                                             legendPositions=[lowerLeft,
                                                              lowerLeft_narrow
                                                              ])

plotTrailingMuPt = PlottingVariables(quantity="pt", binning=binning_mu_pT,
                                     title="trailingMuVsPt", ptCut=[],
                                     massCut=mass_3to3_2,
                                     particleSelector=trailingMu,
                                     legendPositions=[upperRight,
                                                      upperLeft_narrow])
plotTrailingMuPt_pT3to15 = PlottingVariables(quantity="pt",
                                             binning=binning_mu_pT,
                                             title="\
                                             trailingMuVsPt-restr_jpsiPt_3-15GeV\
                                             ",
                                             ptCut=pT_3to15,
                                             massCut=mass_3to3_2,
                                             particleSelector=trailingMu,
                                             legendPositions=[upperRight,
                                                              lowerRight_narrow
                                                              ])
plotTrailingMuEta = PlottingVariables(quantity="eta", binning=binning_mu_eta,
                                      title="trailingMuVsEta", ptCut=[],
                                      massCut=mass_3to3_2,
                                      particleSelector=trailingMu,
                                      legendPositions=[lowerLeft,
                                                       lowerLeft_narrow])
plotTrailingMuEta_pT3to15 = PlottingVariables(quantity="eta",
                                              binning=binning_mu_eta,
                                              title="\
                                            trailingMuVsEta-restr_jpsiPt_3-15GeV\
                                              ",
                                              ptCut=pT_3to15,
                                              massCut=mass_3to3_2,
                                              particleSelector=trailingMu,
                                              legendPositions=[lowerLeft,
                                                               lowerLeft_narrow
                                                               ])

# Construct plotting lists
jpsiPlotVars = [plotBackgrnd_ex3to3_2, plotBackgrnd_ex2_8to3_4,
                plotMass, plotMass_pT3to15, plotPt, plotPt_pT3to15,
                plotEta, plotEta_pT3to15,
                plotLeadingMuPt, plotLeadingMuPt_pT3to15,
                plotLeadingMuEta, plotLeadingMuEta_pT3to15,
                plotTrailingMuPt, plotTrailingMuPt_pT3to15,
                plotTrailingMuEta, plotTrailingMuEta_pT3to15]

makeJPsiPlots(label, handle, jpsiPlotVars)
