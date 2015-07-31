#! /usr/bin/env python

import ROOT
import sys
import math
import tdrstyle
from itertools import izip
from collections import namedtuple
from DataFormats.FWLite import Events, Handle

def makeHistogram (title, binning, quantity):
    histo = ROOT.TH1F (title, "", binning[0],
                        binning[1], binning[2])
    histo.SetMinimum(0)
    if quantity == "mass":
        histo.GetXaxis().SetTitle("J/Psi mass [GeV/c]")
        histo.GetXaxis().SetLabelOffset(0.0100000000000000001)
        histo.GetXaxis().SetTitleOffset(1.2)
        histo.GetYaxis().SetLabelOffset(0.0100000000000000001)
        histo.GetYaxis().SetTitleOffset(1.4)
    elif quantity == "eta":
        histo.GetXaxis().SetTitle("#mbox{#eta}")
        histo.GetXaxis().SetTitleOffset(1.2)
        histo.GetYaxis().SetTitleOffset(1.3)
    elif quantity == "phi":
        histo.GetXaxis().SetTitle("#mbox{#phi}")
    elif quantity == "pt":
        histo.GetXaxis().SetTitle("#mbox{p}_{#mbox{T}} #mbox{[GeV/c]}")
        histo.GetXaxis().SetTitleOffset(1.2)
        histo.GetYaxis().SetTitleOffset(1.3)
    else:
        histo.GetXaxis().SetTitle("")
    histo.GetYaxis().SetTitle("Counts")

    return histo

# Create histograms, etc.
def plotJPsi (events, label, handle, plottingVariables):
    events_noOS.toBegin();
    events_OSrequired.toBegin();

    # Book histograms
    particleHistorgrams = []
    for plottingVar in plottingVariables:
        histo = makeHistogram(plottingVar.title, plottingVar.binning, plottingVar.quantity)
        particleHistorgrams.append(histo)

    # loop over events
    for event in events:
        # use getByLabel, just like in cmsRun
        event.getByLabel (label, handle)
        # get the product
        muons = handle.product()
        # use muons to make J/Psi peak
        numMuons = len (muons)
        if muons < 2: continue
        for outer in xrange (numMuons - 1):
            outerMuon = muons[outer]
            if (not outerMuon.isGlobalMuon()): continue
            for inner in xrange (outer + 1, numMuons):
                innerMuon = muons[inner]
                if (not innerMuon.isGlobalMuon()): continue
                if outerMuon.charge() * innerMuon.charge() >= 0:
                    continue
                inner4v = ROOT.TLorentzVector (innerMuon.px(), innerMuon.py(),
                                               innerMuon.pz(), innerMuon.energy())
                outer4v = ROOT.TLorentzVector (outerMuon.px(), outerMuon.py(),
                                               outerMuon.pz(), outerMuon.energy())
                jpsi = (inner4v + outer4v)

                # TODO: Not sure if that's a good idea actually..
                if outer4v.Pt() > inner4v.Pt():
                    leadingMuon = inner4v
                    secondLeadingMuon = outer4v
                else:
                    leadingMuon = outer4v
                    secondLeadingMuon = inner4v

                for plottingVar, hist in izip(plottingVariables, particleHistorgrams):
                    if len(plottingVar.ptCut) > 0:
                        if (jpsi.Pt() < plottingVar.ptCut[0]): continue
                        if (jpsi.Pt() > plottingVar.ptCut[1]): continue

                    # Select only J/Psi candidates with the correct mass
                    if (jpsi.M() < plottingVar.massCut[0]) or (jpsi.M() > plottingVar.massCut[1]): continue

                    if plottingVar.particleSelector == 0:
                        plotParticle = jpsi
                    elif plottingVar.particleSelector == 1:
                        plotParticle = leadingMuon
                    elif plottingVar.particleSelector == 2:
                        plotParticle = secondLeadingMuon

                    if plottingVar.quantity == "mass":
                        hist.Fill( plotParticle.M() )
                    elif plottingVar.quantity == "eta":
                        hist.Fill( plotParticle.Eta() )
                    elif plottingVar.quantity == "phi":
                        hist.Fill( plotParticle.Phi() )
                    elif plottingVar.quantity == "pt":
                        hist.Fill( plotParticle.Pt() )

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
    jpsiHists_OSrequired = plotJPsi(events_OSrequired, label, handle, plottingVariables)

    ## Modify all below. Put it in loop!
    for jpsiHist_OSrequired, jpsiHist_noOS, plottingVar in izip(jpsiHists_OSrequired, jpsiHists_noOS, plottingVariables):
        jpsiHist_OSrequired.Sumw2()
        jpsiHist_noOS.Sumw2()

        # Draw histograms
        c1 = ROOT.TCanvas("", "", 1024, 786)
        jpsiHist_noOS.SetLineColor(ROOT.kRed)
        jpsiHist_noOS.DrawCopy("E1HIST")
        jpsiHist_OSrequired.SetLineColor(ROOT.kBlue)
        jpsiHist_OSrequired.DrawCopy("E1HISTSAME")
        legend = ROOT.TLegend(0.25,0.2,0.3,0.3)
        legend.SetTextSize(0.0275)
        if (len(plottingVar.ptCut) > 0):
            # legend.SetFillStyle(0)
            legend.AddEntry(jpsiHist_noOS, "HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1; " + plottingVar.ptCut[2], "LEP")
            legend.AddEntry(jpsiHist_OSrequired, "HLT_Dimuon0er16_Jpsi_NoVertexing_v1; " + plottingVar.ptCut[2], "LEP")
        else:
            # legend = ROOT.TLegend(0.47,0.87,0.99,0.99)
            # legend.SetFillStyle(0)
            # legend.SetTextSize(0.0275)
            legend.AddEntry(jpsiHist_noOS, "HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v1", "LEP")
            legend.AddEntry(jpsiHist_OSrequired, "HLT_Dimuon0er16_Jpsi_NoVertexing_v1", "LEP")
        legend.Draw("SAME")
        c1.Print (plottingVar.title + ".png")
        c1.Print (plottingVar.title + ".pdf")


        # Plot efficiencies
        c2 = ROOT.TCanvas("", "", 1024, 786)
        # legend_ratio = ROOT.TLegend(0.78,0.91,0.99,0.99)
        legend_ratio = ROOT.TLegend(0.25,0.2,0.3,0.25)
        legend_ratio.SetTextSize(0.0275)
        # legend_ratio.SetFillStyle(0)
        jpsiHist_ratio = ROOT.TH1F ("jpsiratio", "", plottingVar.binning[0], plottingVar.binning[1], plottingVar.binning[2])
        jpsiHist_ratio.Sumw2()
        jpsiHist_ratio.SetLineColor(ROOT.kBlue);
        jpsiHist_ratio.Divide(jpsiHist_OSrequired, jpsiHist_noOS, 1.0, 1.0)
        jpsiHist_ratio.SetMinimum(0)
        if plottingVar.quantity == "mass":
            jpsiHist_ratio.GetXaxis().SetTitle("J/Psi mass [GeV/c]")
            jpsiHist_ratio.GetXaxis().SetTitleOffset(1.2)
        elif plottingVar.quantity == "eta":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{#eta}")
        elif plottingVar.quantity == "phi":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{#phi}")
        elif plottingVar.quantity == "pt":
            jpsiHist_ratio.GetXaxis().SetTitle("#mbox{p}_{#mbox{T}} #mbox{[GeV/c]}")
            jpsiHist_ratio.GetXaxis().SetTitleOffset(1.2)
        else:
            jpsiHist_ratio.GetXaxis().SetTitle("")
        jpsiHist_ratio.GetYaxis().SetTitle("OS required/no OS")
        jpsiHist_ratio.Draw("E1HIST")
        if (len(plottingVar.ptCut) > 0):
            legend_ratio.AddEntry(jpsiHist_ratio, plottingVar.ptCut[2], "LEP")
            legend_ratio.Draw("SAME")
        line = ROOT.TLine(plottingVar.binning[1], 1, plottingVar.binning[2], 1);
        line.SetLineColor(ROOT.kRed)
        line.Draw("SAME")
        c2.Print (plottingVar.title + "_ratio.png")
        c2.Print (plottingVar.title + "_ratio.pdf")


        # Compute overall efficiency
        nJPsi_noOS = jpsiHist_noOS.Integral()
        nJPsi_OSrequired = jpsiHist_OSrequired.Integral()
        print "J/Psi candidates with OS required: " + str(nJPsi_OSrequired)
        print "J/Psi candidates without OS required: " + str(nJPsi_noOS)
        totalEffError = nJPsi_OSrequired/nJPsi_noOS * math.sqrt( ( 1/nJPsi_noOS ) +  ( 1/nJPsi_OSrequired ) )
        print "Efficiency: " +str(nJPsi_OSrequired/nJPsi_noOS) + "+/-" +str(totalEffError)
        # print "Alternative error (from hist): " +str(jpsiHist_ratio.GetBinError(1))


f_noOS = ROOT.TFile.Open("../../charmonium_HLT_noOS.root")
f_OSrequired = ROOT.TFile.Open("../../charmonium_HLT_OSrequired.root")
events_noOS = Events (f_noOS)
events_OSrequired = Events (f_OSrequired)

# create handle outside of loop
handle  = Handle ("std::vector<pat::Muon>")

# for now, label is just a tuple of strings that is initialized just
# like and edm::InputTag
label = ("selectedPatMuons")

# Structure to hold plotting data
# particleSelector: 0 = DiMuon; 1 = Leading muon; 2 = Second leading muon
PlottingVariables = namedtuple("PlottingVariables", ["quantity", "binning", "title", "ptCut", "massCut", "particleSelector"])

# Binning lists
binning_mass = [25, 2.9, 3.4]
binning_eta = [16, -1.6, 1.6]
binning_pT = [35, 0, 35]
binning_pT_restricted = [12, 3, 15]

binning_mu_eta = [16, -1.6, 1.6]
binning_mu_pT = [20, 0, 20]


# Cuts
pT_3to15 = [3, 15, "#mbox{p}_{#mbox{T}}#mbox{(J/Psi) in [3, 15] GeV/c}"]
mass_3to3_2 = [3, 3.2, ""]


# Particle selector
diMu = 0
leadingMu = 1
secondLeadingMu = 2


# Construct plotting variables
plotMass = PlottingVariables(quantity="mass", binning=binning_mass, title="jpsiMass", ptCut=[], massCut=mass_3to3_2, particleSelector=diMu)
plotMass_pTrestricted = PlottingVariables(quantity="mass", binning=binning_mass, title="jpsiMass_3-15GeV", ptCut=pT_3to15, massCut=mass_3to3_2, particleSelector=diMu)
plotPt = PlottingVariables(quantity="pt", binning=binning_pT, title="jpsiVsPt", ptCut=[], massCut=mass_3to3_2, particleSelector=diMu)
plotPt_pTrestricted = PlottingVariables(quantity="pt", binning=binning_pT_restricted, title="jpsiVsPt_3-15GeV", ptCut=pT_3to15, massCut=mass_3to3_2, particleSelector=diMu)
plotEta = PlottingVariables(quantity="eta", binning=binning_eta, title="jpsiVsEta", ptCut=[], massCut=mass_3to3_2, particleSelector=diMu)
plotEta_pTrestricted = PlottingVariables(quantity="eta", binning=binning_eta, title="jpsiVsEta_3-15GeV", ptCut=pT_3to15, massCut=mass_3to3_2, particleSelector=diMu)

plotMuPt = PlottingVariables(quantity="pt", binning=binning_mu_pT, title="leadingMuVsPt", ptCut=[], massCut=mass_3to3_2, particleSelector=leadingMu)
plotMuPt_pTrestricted = PlottingVariables(quantity="pt", binning=binning_mu_pT, title="leadingMuVsPt-restr_jpsiPt_3-15GeV", ptCut=pT_3to15, massCut=mass_3to3_2, particleSelector=leadingMu)
plotMuEta = PlottingVariables(quantity="eta", binning=binning_mu_eta, title="leadingMuVsEta", ptCut=[], massCut=mass_3to3_2, particleSelector=leadingMu)
plotMuEta_pTrestricted = PlottingVariables(quantity="eta", binning=binning_mu_eta, title="leadingMuVsEta-restr_jpsiPt_3-15GeV", ptCut=pT_3to15, massCut=mass_3to3_2, particleSelector=leadingMu)


# Construct plotting lists
jpsiPlotVars = [plotMass, plotMass_pTrestricted, plotPt, plotPt_pTrestricted,
                plotEta, plotEta_pTrestricted, plotMuPt, plotMuPt_pTrestricted,
                plotMuEta, plotMuEta_pTrestricted]

makeJPsiPlots(label, handle, jpsiPlotVars)
