#include "L1Ntuple.h"
#include "hist.C"
#include "Style.C"
#include <TH1D.h>
#include <TH2D.h>
#include <algorithm>
#include <TMath.h>
#include <THStack.h>
#include <TLegend.h>
#include <TLine.h>
#include <TGraphAsymmErrors.h>
#include <sstream>
#include <TLorentzVector.h>
#include "TNtuple.h"
#include "TFile.h"

using namespace L1Analysis;
// --------------------------------------------------------------------
// description: Macro to check the charge assignment for J/Psi muons.
// --------------------------------------------------------------------
#define PHI 0
#define ETA 1
#define PT 2
#define PTETA 3

#define DT 0
#define RPCb 1
#define CSC 2
#define RPCf 3
#define GMT 4
#define RECOPASS 5
const TString msystem[6] = {"DT", "RPCb", "CSC", "RPCf", "GMT", "Reco"};
const TString mquality[8] = {"0", "1", "2", "3", "4", "5", "6", "7"};
const Double_t ptbin[14] = {0., 1., 2.,  3.,  4.,  5.,  6.,
                            7., 9., 11., 15., 20., 28., 100.};
const TString muSystems[6] = {"DTRPC", "CSCRPC", "DT", "CSC", "RPCb", "RPCf"};
enum muSysEnum { eDTRPC, eCSCRPC, eDT, eCSC, eRPCb, eRPCf, none };
const Int_t nptbin = 13;
const TString md[2] = {"num", "den"};
int Nsys = 5;
Double_t pig = acos(-1.);

Int_t onedhisto_nbins = 60;
Int_t twodhisto_nbins = 36;

class GMTChargeAssignmentNtupleizer : public L1Ntuple {
 public:
  // constructor
  GMTChargeAssignmentNtupleizer(std::string filename)
      : L1Ntuple(filename) {}
  GMTChargeAssignmentNtupleizer() : L1Ntuple() {}
  ~GMTChargeAssignmentNtupleizer() {}

  // main function macro : arguments can be adpated to your need
  void run(Long64_t nevents);

 private:
  TFile* fout;

  // your private methods can be declared here
  TNtuple* ntuple;
  void fillNtuple(int recoMu1, int recoMu2, int gmtMu1, int gmtMu2,
                  std::pair<bool, bool> diMuMatch,
                  std::vector<std::string> contDict, Float_t ntupleValues[]);
  void toggleBranches();
  double dphi(int iRecoMu, int iL1Mu, int iL1Sys);  // calculate delta phi
                                                    // between iRecoMu muon and
                                                    // iL1Mu trigcand of type
                                                    // iL1Sys
  double deta(int iRecoMu, int iL1Mu, int iL1Sys);  // calculate delta eta
                                                    // between iRecoMu muon and
                                                    // iL1Mu trigcand of type
                                                    // iL1Sys
  double dpt(int iRecoMu, int iL1Mu, int iL1Sys);  // calculate delta pt between
                                                   // iRecoMu muon and iL1Mu
                                                   // trigcand of type iL1Sys
  double bestL1match(int iRecoMu, int& iL1Muint, int iL1Sys, float ptcut,
                     int exclMu);  // finds best match between iRecoMu muon and
                                   // trig cands of type iL1Sys
  std::pair<bool, bool> matchDiMuons(int iRecoMu1, int iRecoMu2, int& L1Mu1, int& L1Mu2,
                    int iL1Sys, float ptcut,
                    float dRmax);  // finds the best two
                                   // matches (lowest
                                   // dR=dR1+dR2) for
                                   // the two iRecoMus.
  double dRreco(int iRecoMu1, int iRecoMu2);
  muSysEnum whichSubsystem(int mu);

  TH1D* hist_invarMass_reco;
  TH1D* hist_invarMass_gmt;
  TH1D* hist_invarMass_JPsi_reco;
  TH1D* histRecodR;
  TH1I* hist_numberOfMissmatchedMuons;
  TH1D* histAllDiMuons_eta;
  TH1D* histAllDiMuons_pt;
  TH1D* histCorrectCharges_eta;
  TH1D* histCorrectCharges_pt;
  TH1D* histOneCorrectCharge_eta;
  TH1D* histOneCorrectCharge_pt;
  TH1D* histOneFlippedCharge_eta;
  TH1D* histOneFlippedCharge_pt;
  TH1D* histBothFlippedCharge_eta;
  TH1D* histBothFlippedCharge_pt;
  TH1D* histUsableforOS_eta;
  TH1D* histUsableforOS_pt;
  std::vector<TH1D*> histVecCorrectCharges_eta;
  std::vector<TH1D*> histVecCorrectCharges_pt;
  std::vector<TH1D*> histVecOneCorrectCharge_eta;
  std::vector<TH1D*> histVecOneCorrectCharge_pt;
  std::vector<TH1D*> histVecOneFlippedCharge_eta;
  std::vector<TH1D*> histVecOneFlippedCharge_pt;
  std::vector<TH1D*> histVecBothFlippedCharge_eta;
  std::vector<TH1D*> histVecBothFlippedCharge_pt;
  std::vector<TH1D*> histVecUsableForOS_eta;
  std::vector<TH1D*> histVecUsableForOS_pt;
  TH2D* H2AllDiMuons;
  TH2D* H2AllCorrectCharges;
  TH2D* H2AllFlippedCharges;
  TH2D* H2CorrectCharges;
  TH2D* H2OneCorrectCharge;
  TH2D* H2OneFlippedCharge;
  TH2D* H2BothFlippedCharge;
  TH2D* H2UsableForOS;
  TH2D* H2UsableForOS_crosscheck;
  void bookhistos();  // to book histograms
  bool trigcuts();
  bool glmucuts(int imu);
  int candqual(int iL1Mu, int iL1Sys);
  double candphi(int iRecoMu, int iL1Sys);
  bool sysmucuts(int imu, int iSys, int what, float ptcut);
};

// --------------------------------------------------------------------
// run function
// --------------------------------------------------------------------
void GMTChargeAssignmentNtupleizer::run(Long64_t nevents) {
  toggleBranches();

  // Create ntuple
  // TODO: Generate contStream from vec.
  // TODO: Make vec a vec of pairs?
  std::vector<std::string> varList;
  varList.push_back("N");
  varList.push_back("Eta");
  varList.push_back("Phi");
  varList.push_back("pT");
  varList.push_back("Ch");
  varList.push_back("InvMass");
  std::ostringstream ntupleContStream;
  std::vector<std::string> contDict;
  ntupleContStream << "Qual1_GMT:Qual2_GMT:SubsysID1_GMT:SubsysID2_GMT:dR_reco";
  contDict.push_back("Qual1_GMT");
  contDict.push_back("Qual2_GMT");
  contDict.push_back("SubsysID1_GMT");
  contDict.push_back("SubsysID2_GMT");
  contDict.push_back("dR_reco");
  for (std::vector<std::string>::iterator name = varList.begin(); name != varList.end(); ++name) {
    ntupleContStream << ":" << *name << "1_reco:" << *name << "1_GMT";
    contDict.push_back(*name + "1_reco");
    // std::cout << name + "1_Reco" << std::endl;
    contDict.push_back(*name + "1_GMT");
    ntupleContStream << ":" << *name << "2_reco:" << *name << "2_GMT";
    contDict.push_back(*name + "2_reco");
    contDict.push_back(*name + "2_GMT");
  }
  std::string fname("DiMuNtuple.root");
  TFile* out = new TFile(fname.c_str(), "RECREATE");
  out->cd();
  std::string ntupleContent(ntupleContStream.str());
  ntuple = new TNtuple("ntuple", "ntupledump", ntupleContent.c_str());

  // load TDR style
  setTDRStyle();

  // number of events to process
  if (nevents == -1 || nevents > GetEntries()) {
    nevents = GetEntries();
  }
  std::cout << nevents << " to process ..." << std::endl;

  // loop over the events
  for (Long64_t i = 0; i < nevents; i++) {
    // load the i-th event
    Long64_t ientry = LoadTree(i);
    if (ientry < 0) break;
    GetEntry(i);

    // process progress
    if (i != 0 && (i % 50000) == 0) {
      std::cout << "- processing event " << i << "\n" << std::endl;
    }

    // We're only checking GMT data here:
    int iSys = GMT;

    // We're only interested in events with di-muons.
    if (recoMuon_->nMuons < 2) {
      continue;
    }

    for (int mu1 = 0; mu1 < recoMuon_->nMuons; ++mu1) {
      if (!glmucuts(mu1)) {
        continue;
      }
      // TODO: Also sysmucuts??
      for (int mu2 = mu1 + 1; mu2 < recoMuon_->nMuons; ++mu2) {
        if (!glmucuts(mu2)) {
          continue;
        }
        if (mu1 == mu2) {
          continue;
        }

        // Find L1 candidates for both muons.
        // TODO: Which pT cut??
        int cand1, cand2;
        std::pair<bool, bool> diMuMatch =
            matchDiMuons(mu1, mu2, cand1, cand2, GMT, 0, 0.3);

        if (diMuMatch.first && diMuMatch.second) {
          if (cand1 == cand2) {
            std::cout << "This should now be impossible." << std::endl;
            // continue;
          }
          Float_t ntupleValues[contDict.size()];

          fillNtuple(mu1, mu2, cand1, cand2, diMuMatch, contDict, ntupleValues);

          ntuple->Fill(ntupleValues);
        }
      }
    }
  }  // loop over events
  out->Write();
}

void GMTChargeAssignmentNtupleizer::fillNtuple(
    int recoMu1, int recoMu2, int gmtMu1, int gmtMu2,
    std::pair<bool, bool> diMuMatch, std::vector<std::string> contDict,
    Float_t ntupleValues[]) {
  for (size_t varIt = 0; varIt < contDict.size(); ++varIt) {
    if (contDict[varIt] == "dR_reco") {
      ntupleValues[varIt] = dRreco(recoMu1, recoMu2);
    }
    if (contDict[varIt] == "N_reco") {
      ntupleValues[varIt] = recoMuon_->nMuons;
    }
    if (contDict[varIt] == "pT1_reco") {
      ntupleValues[varIt] = recoMuon_->pt[recoMu1];
    }
    if (contDict[varIt] == "pT2_reco") {
      ntupleValues[varIt] = recoMuon_->pt[recoMu2];
    }
    if (contDict[varIt] == "Eta1_reco") {
      ntupleValues[varIt] = recoMuon_->eta[recoMu1];
    }
    if (contDict[varIt] == "Eta2_reco") {
      ntupleValues[varIt] = recoMuon_->eta[recoMu2];
    }
    if (contDict[varIt] == "Phi1_reco") {
      ntupleValues[varIt] = recoMuon_->phi[recoMu1];
    }
    if (contDict[varIt] == "Phi2_reco") {
      ntupleValues[varIt] = recoMuon_->phi[recoMu2];
    }
    if (contDict[varIt] == "Ch1_reco") {
      ntupleValues[varIt] = recoMuon_->ch[recoMu1];
    }
    if (contDict[varIt] == "Ch2_reco") {
      ntupleValues[varIt] = recoMuon_->ch[recoMu2];
    }
    if (contDict[varIt] == "InvMass_reco") {
      // Calc invariant mass of reco muons.
      TLorentzVector muVec1;
      muVec1.SetPtEtaPhiM(recoMuon_->pt[recoMu1], recoMuon_->eta[recoMu1],
                          recoMuon_->phi[recoMu1], 0);
      TLorentzVector muVec2;
      muVec2.SetPtEtaPhiM(recoMuon_->pt[recoMu2], recoMuon_->eta[recoMu2],
                          recoMuon_->phi[recoMu2], 0);
      double invMass = (muVec1 + muVec2).Mag();
      ntupleValues[varIt] = invMass;
    }

    if (contDict[varIt] == "N_GMT") {
      ntupleValues[varIt] = gmt_->N;
    }
    if (contDict[varIt] == "pT1_GMT") {
      ntupleValues[varIt] = gmt_->Pt[gmtMu1];
    }
    if (contDict[varIt] == "Eta1_GMT") {
      ntupleValues[varIt] = gmt_->Eta[gmtMu1];
    }
    if (contDict[varIt] == "Phi1_GMT") {
      ntupleValues[varIt] = gmt_->Phi[gmtMu1];
    }
    if (contDict[varIt] == "Ch1_GMT") {
      ntupleValues[varIt] = gmt_->Cha[gmtMu1];
    }
    if (contDict[varIt] == "Qual1_GMT") {
      ntupleValues[varIt] = gmt_->Qual[gmtMu1];
    }
    if (contDict[varIt] == "SubsysID1_GMT") {
      ntupleValues[varIt] = whichSubsystem(gmtMu1);
    }
    if (contDict[varIt] == "pT2_GMT") {
      ntupleValues[varIt] = gmt_->Pt[gmtMu2];
    }
    if (contDict[varIt] == "Eta2_GMT") {
      ntupleValues[varIt] = gmt_->Eta[gmtMu2];
    }
    if (contDict[varIt] == "Phi2_GMT") {
      ntupleValues[varIt] = gmt_->Phi[gmtMu2];
    }
    if (contDict[varIt] == "Ch2_GMT") {
      ntupleValues[varIt] = gmt_->Cha[gmtMu2];
    }
    if (contDict[varIt] == "InvMass_reco") {
      TLorentzVector muVec1;
      muVec1.SetPtEtaPhiM(gmt_->Pt[gmtMu1], gmt_->Eta[gmtMu1], gmt_->Phi[gmtMu1], 0);
      TLorentzVector muVec2;
      muVec2.SetPtEtaPhiM(gmt_->Pt[gmtMu2], gmt_->Eta[gmtMu2], gmt_->Phi[gmtMu2], 0);
      double invMass = (muVec1 + muVec2).Mag();
      ntupleValues[varIt] = invMass;
    }
    if (contDict[varIt] == "Qual2_GMT") {
      ntupleValues[varIt] = gmt_->Qual[gmtMu2];
    }
    if (contDict[varIt] == "SubsysID2_GMT") {
      ntupleValues[varIt] = whichSubsystem(gmtMu2);
    }
  }
}

bool GMTChargeAssignmentNtupleizer::trigcuts() {
  bool cond;
  bool DTAct = std::find(event_->hlt.begin(), event_->hlt.end(),
                         "HLT_Activity_DT") != event_->hlt.end();
  bool CSCAct = std::find(event_->hlt.begin(), event_->hlt.end(),
                          "HLT_Activity_CSC") != event_->hlt.end();
  cond = (DTAct || CSCAct);
  return cond;
}

bool GMTChargeAssignmentNtupleizer::sysmucuts(int imu, int iSys,
                                                       int what, float ptcut) {
  bool condeta = false;
  if (iSys == DT || iSys == RPCb) condeta = (fabs(recoMuon_->eta[imu]) < 1.05);
  if (iSys == CSC)
    condeta =
        (fabs(recoMuon_->eta[imu]) >= 1.05 && fabs(recoMuon_->eta[imu]) < 2.6);
  if (iSys == RPCf)
    condeta = (fabs(recoMuon_->eta[imu]) >= 1.05) &&
              (fabs(recoMuon_->eta[imu]) < 1.6);
  if (iSys == GMT) condeta = (fabs(recoMuon_->eta[imu]) < 2.6);

  bool condpt = false;
  if (ptcut <= 0) {
    condpt = true;
  } else {
    if (iSys == DT || iSys == RPCb)
      condpt = (fabs(recoMuon_->pt[imu]) >= ptcut);
    if (iSys == CSC) condpt = (fabs(recoMuon_->pt[imu]) >= ptcut);
    if (iSys == RPCf) condpt = (fabs(recoMuon_->pt[imu]) >= ptcut);
    if (iSys == GMT) condpt = (fabs(recoMuon_->pt[imu]) >= ptcut);
  }

  bool cond = false;
  if (what == ETA) cond = condeta;
  if (what == PT) cond = condpt;
  if (what == PTETA) cond = (condeta && condpt);

  return cond;
}
bool GMTChargeAssignmentNtupleizer::glmucuts(int imu) {
  return (recoMuon_->type[imu] == 0);
}

int GMTChargeAssignmentNtupleizer::candqual(int iL1Mu, int iL1Sys) {
  int q = -99;
  if (iL1Sys == DT) q = gmt_->Qualdt[iL1Mu];
  if (iL1Sys == RPCb) q = gmt_->Qualrpcb[iL1Mu];
  if (iL1Sys == CSC) q = gmt_->Qualcsc[iL1Mu];
  if (iL1Sys == RPCf) q = gmt_->Qualrpcf[iL1Mu];
  if (iL1Sys == GMT) q = gmt_->Qual[iL1Mu];
  if (iL1Sys == RECOPASS) q = 7;
  return q;
}
double GMTChargeAssignmentNtupleizer::candphi(int iRecoMu,
                                                       int iL1Sys) {
  double p = -9999;
  if (iL1Sys == DT || iL1Sys == RPCb) p = recoMuon_->sa_phi_mb2[iRecoMu];
  if (iL1Sys == CSC || iL1Sys == RPCf) {
    if (recoMuon_->eta[iRecoMu] > 0) p = recoMuon_->sa_phi_me2_p[iRecoMu];
    if (recoMuon_->eta[iRecoMu] < 0) p = recoMuon_->sa_phi_me2_n[iRecoMu];
  }
  if (iL1Sys == GMT) {
    if (recoMuon_->eta[iRecoMu] > 1.05) p = recoMuon_->sa_phi_me2_p[iRecoMu];
    if (recoMuon_->eta[iRecoMu] < -1.05) p = recoMuon_->sa_phi_me2_n[iRecoMu];
    if (fabs(recoMuon_->eta[iRecoMu] <= 1.05))
      p = recoMuon_->sa_phi_mb2[iRecoMu];
  }
  return p;
}
double GMTChargeAssignmentNtupleizer::dphi(int iRecoMu, int iL1Mu,
                                                    int iL1Sys) {
  if (recoMuon_->type[iRecoMu] != 0) return -9999;  // not a global
  Double_t trigphi = -99999;
  if (iL1Sys == DT) trigphi = gmt_->Phidt[iL1Mu];
  if (iL1Sys == RPCb) trigphi = gmt_->Phirpcb[iL1Mu];
  if (iL1Sys == CSC) trigphi = gmt_->Phicsc[iL1Mu];
  if (iL1Sys == RPCf) trigphi = gmt_->Phirpcf[iL1Mu];
  if (iL1Sys == GMT) trigphi = gmt_->Phi[iL1Mu];
  Double_t recophi = -99999;
  Double_t recophi2 = -99999;
  if (iL1Sys == DT || iL1Sys == RPCb)
    recophi = recoMuon_->sa_phi_mb2[iRecoMu] - (pig / 144.);
  if ((iL1Sys == CSC || iL1Sys == RPCf) && recoMuon_->eta[iRecoMu] >= 0)
    recophi = recoMuon_->sa_phi_me2_p[iRecoMu] - (pig / 144.);
  if ((iL1Sys == CSC || iL1Sys == RPCf) && recoMuon_->eta[iRecoMu] < 0)
    recophi = recoMuon_->sa_phi_me2_n[iRecoMu] - (pig / 144.);
  if (iL1Sys == GMT) {
    recophi = recoMuon_->sa_phi_mb2[iRecoMu] - (pig / 144.);
    if (recoMuon_->eta[iRecoMu] >= 0)
      recophi2 = recoMuon_->sa_phi_me2_p[iRecoMu] - (pig / 144.);
    else
      recophi2 = recoMuon_->sa_phi_me2_n[iRecoMu] - (pig / 144.);
  }
  Double_t newphisep = recophi - trigphi;
  if (newphisep < -pig) newphisep = newphisep + 2 * pig;
  if (newphisep > pig) newphisep = newphisep - 2 * pig;
  Double_t newphisep2 = recophi2 - trigphi;
  if (newphisep2 < -pig) newphisep2 = newphisep2 + 2 * pig;
  if (newphisep2 > pig) newphisep2 = newphisep2 - 2 * pig;
  if (iL1Sys == GMT)
    if (fabs(newphisep) > fabs(newphisep2)) newphisep = newphisep2;

  if (iL1Sys == RECOPASS) newphisep = 0;
  if (newphisep > 1000) return -999;
  return newphisep;
}

double GMTChargeAssignmentNtupleizer::deta(int iRecoMu, int iL1Mu,
                                                    int iL1Sys) {
  if (recoMuon_->type[iRecoMu] != 0) return -9999;  // not a global
  Double_t trigeta = -99999;
  if (iL1Sys == DT) trigeta = gmt_->Etadt[iL1Mu];
  if (iL1Sys == RPCb) trigeta = gmt_->Etarpcb[iL1Mu];
  if (iL1Sys == CSC) trigeta = gmt_->Etacsc[iL1Mu];
  if (iL1Sys == RPCf) trigeta = gmt_->Etarpcf[iL1Mu];
  if (iL1Sys == GMT) trigeta = gmt_->Eta[iL1Mu];
  Double_t newetasep = recoMuon_->eta[iRecoMu] - trigeta;
  if (iL1Sys == RECOPASS) newetasep = 0;
  if (newetasep > 1000) return -999;
  return newetasep;
}
double GMTChargeAssignmentNtupleizer::dpt(
    int iRecoMu, int iL1Mu,
    int iL1Sys) {  // the tracker pt is used
  Double_t trigpt = -99999;
  if (iL1Sys == DT) trigpt = gmt_->Ptdt[iL1Mu];
  if (iL1Sys == RPCb) trigpt = gmt_->Ptrpcb[iL1Mu];
  if (iL1Sys == CSC) trigpt = gmt_->Ptcsc[iL1Mu];
  if (iL1Sys == RPCf) trigpt = gmt_->Ptrpcf[iL1Mu];
  if (iL1Sys == GMT) trigpt = gmt_->Pt[iL1Mu];
  Float_t newptsep = recoMuon_->tr_pt[iRecoMu] - trigpt;
  if (iL1Sys == RECOPASS) newptsep = 0;
  if (newptsep > 1000) return -999;
  return newptsep;
}

double GMTChargeAssignmentNtupleizer::bestL1match(
    int iRecoMu, int& iL1Mu, int iL1Sys, float ptcut, int exclMu) {
  Double_t bestdeltar = 9999;
  int cand = 9999;
  if (iL1Sys == DT) {
    for (Int_t im = 0; im < gmt_->Ndt; im++) {
      Double_t deltaphi = dphi(iRecoMu, im, iL1Sys);
      Double_t deltaeta = deta(iRecoMu, im, iL1Sys);
      Double_t deltar = sqrt(deltaphi * deltaphi + deltaeta * deltaeta);
      if (deltar < bestdeltar && gmt_->Bxdt[im] == 0 && im != exclMu) {
        bestdeltar = deltar;
        cand = im;
      }
    }
  }
  if (iL1Sys == RPCb) {
    for (Int_t im = 0; im < gmt_->Nrpcb; im++) {
      Double_t deltaphi = dphi(iRecoMu, im, iL1Sys);
      Double_t deltaeta = deta(iRecoMu, im, iL1Sys);
      Double_t deltar = sqrt(deltaphi * deltaphi + deltaeta * deltaeta);
      if (deltar < bestdeltar && gmt_->Bxrpcb[im] == 0 && im != exclMu) {
        bestdeltar = deltar;
        cand = im;
      }
    }
  }
  if (iL1Sys == RPCf) {
    for (Int_t im = 0; im < gmt_->Nrpcf; im++) {
      Double_t deltaphi = dphi(iRecoMu, im, iL1Sys);
      Double_t deltaeta = deta(iRecoMu, im, iL1Sys);
      Double_t deltar = sqrt(deltaphi * deltaphi + deltaeta * deltaeta);
      if (deltar < bestdeltar && gmt_->Bxrpcf[im] == 0 && im != exclMu) {
        bestdeltar = deltar;
        cand = im;
      }
    }
  }
  if (iL1Sys == CSC) {
    for (Int_t im = 0; im < gmt_->Ncsc; im++) {
      Double_t deltaphi = dphi(iRecoMu, im, iL1Sys);
      Double_t deltaeta = deta(iRecoMu, im, iL1Sys);
      Double_t deltar = sqrt(deltaphi * deltaphi + deltaeta * deltaeta);
      if (deltar < bestdeltar && gmt_->Bxcsc[im] == 0 && im != exclMu) {
        bestdeltar = deltar;
        cand = im;
      }
    }
  }
  if (iL1Sys == GMT) {
    for (Int_t im = 0; im < gmt_->N; im++) {
      Double_t deltaphi = dphi(iRecoMu, im, iL1Sys);
      Double_t deltaeta = deta(iRecoMu, im, iL1Sys);
      Double_t deltar = sqrt(deltaphi * deltaphi + deltaeta * deltaeta);
      if (deltar < bestdeltar && gmt_->CandBx[im] == 0 &&
          gmt_->Pt[im] >= ptcut && im != exclMu) {
        bestdeltar = deltar;
        cand = im;
      }
    }
  }
  if (iL1Sys == RECOPASS) {
    bestdeltar = 0;
    cand = -1;
  }

  iL1Mu = cand;
  return bestdeltar;
}

double GMTChargeAssignmentNtupleizer::dRreco(int iRecoMu1,
                                                      int iRecoMu2) {
  double dR = -9999;
  if (recoMuon_->type[iRecoMu1] != 0) return -9999;  // not a global
  if (recoMuon_->type[iRecoMu2] != 0) return -9999;  // not a global
  double recophi1 = recoMuon_->sa_phi_mb2[iRecoMu1];
  double recophi2 = recoMuon_->sa_phi_mb2[iRecoMu2];
  double recoeta1 = recoMuon_->eta[iRecoMu1];
  double recoeta2 = recoMuon_->eta[iRecoMu2];
  double ddphi = fabs(recophi1 - recophi2);
  if (ddphi > pig) ddphi -= 2 * pig;
  double ddeta = fabs(recoeta1 - recoeta2);
  dR = sqrt(ddphi * ddphi + ddeta * ddeta);
  return dR;
}

muSysEnum GMTChargeAssignmentNtupleizer::whichSubsystem(int mu) {
  muSysEnum muSys;
  if (gmt_->IdxDTBX[mu] != -1 && gmt_->IdxRPCb[mu] != -1) {
    muSys = eDTRPC;
  } else if (gmt_->IdxCSC[mu] != -1 && gmt_->IdxRPCf[mu] != -1) {
    muSys = eCSCRPC;
  } else if (gmt_->IdxDTBX[mu] != -1) {
    int Ndt = gmt_->Ndt;
    for (int k = 0; k < Ndt; ++k) {
      // Go through Bxdt and search for first muon in triggered beam crossing
      if (gmt_->Bxdt[k] == 0) {
        muSys = eDT;
      }
    }
  } else if (gmt_->IdxCSC[mu] != -1) {
    int Ncsc = gmt_->Ncsc;
    for (int k = 0; k < Ncsc; ++k) {
      if (gmt_->Bxcsc[k] == 0) {
        muSys = eCSC;
      }
    }
  } else if (gmt_->IdxRPCb[mu] != -1) {
    int Nrpcb = gmt_->Nrpcb;
    for (int k = 0; k < Nrpcb; ++k) {
      if (gmt_->Bxrpcb[k] == 0) {
        muSys = eRPCb;
      }
    }
  } else if (gmt_->IdxRPCf[mu] != -1) {
    int Nrpcf = gmt_->Nrpcf;
    for (int k = 0; k < Nrpcf; ++k) {
      if (gmt_->Bxrpcf[k] == 0) {
        muSys = eRPCf;
      }
    }
  } else {
    // This will crash the macro.
    muSys = none;
    std::cout << "This shouldn't happen." << std::endl;
  }

  return muSys;
}

std::pair<bool, bool> GMTChargeAssignmentNtupleizer::matchDiMuons(
    int iRecoMu1, int iRecoMu2, int& L1Mu1, int& L1Mu2, int iL1Sys, float ptcut,
    float dRmax) {
  int cand11, cand12, cand21, cand22;
  float dR11, dR12, dR21, dR22, dR1, dR2, dRtot1, dRtot2;
  dR11 = bestL1match(iRecoMu1, cand11, iL1Sys, ptcut, 9999999);
  dR12 = bestL1match(iRecoMu2, cand12, iL1Sys, ptcut, cand11);
  dRtot1 = dR11 + dR12;

  dR22 = bestL1match(iRecoMu2, cand22, iL1Sys, ptcut, 9999999);
  dR21 = bestL1match(iRecoMu1, cand21, iL1Sys, ptcut, cand22);
  dRtot2 = dR21 + dR22;

  if (dRtot1 < dRtot2) {
    L1Mu1 = cand11;
    L1Mu2 = cand12;
    dR1 = dR11;
    dR2 = dR12;
  } else {
    L1Mu1 = cand21;
    L1Mu2 = cand22;
    dR1 = dR21;
    dR2 = dR22;
  }

  return std::pair<bool, bool>(dR1 < dRmax, dR2 < dRmax);
}

void GMTChargeAssignmentNtupleizer::toggleBranches() {
  // Select only needed branches:
  fChain->SetBranchStatus("*", 0);

  fChain->SetBranchStatus("Ndt", 1);
  fChain->SetBranchStatus("Bxdt", 1);
  // fChain->SetBranchStatus("Qualdt",1);

  fChain->SetBranchStatus("Ncsc", 1);
  fChain->SetBranchStatus("Bxcsc", 1);
  // fChain->SetBranchStatus("Qualcsc",1);

  fChain->SetBranchStatus("Nrpcb", 1);
  fChain->SetBranchStatus("Bxrpcb", 1);
  // fChain->SetBranchStatus("Qualrpcb",1);

  fChain->SetBranchStatus("Nrpcf", 1);
  fChain->SetBranchStatus("Bxrpcf", 1);
  // fChain->SetBranchStatus("Qualrpcf",1);

  fChain->SetBranchStatus("N", 1);
  fChain->SetBranchStatus("CandBx", 1);
  fChain->SetBranchStatus("Qual", 1);
  fChain->SetBranchStatus("Eta", 1);
  fChain->SetBranchStatus("Phi", 1);
  fChain->SetBranchStatus("Pt", 1);
  fChain->SetBranchStatus("Cha", 1);
  fChain->SetBranchStatus("IdxDTBX", 1);
  fChain->SetBranchStatus("IdxRPCb", 1);
  fChain->SetBranchStatus("IdxCSC", 1);
  fChain->SetBranchStatus("IdxRPCf", 1);

  fChain->SetBranchStatus("nMuons", 1);
  fChain->SetBranchStatus("pt", 1);
  fChain->SetBranchStatus("eta", 1);
  fChain->SetBranchStatus("phi", 1);
  fChain->SetBranchStatus("ch", 1);
  // fChain->SetBranchStatus("sa_validhits",1);
  // fChain->SetBranchStatus("tr_validhits",1);
  fChain->SetBranchStatus("howmanytypes", 1);
  // fChain->SetBranchStatus("tr_pt",1);
  // fChain->SetBranchStatus("tr_validpixhits",1);
  fChain->SetBranchStatus("type", 1);
  // fChain->SetBranchStatus("normchi2",1);
  fChain->SetBranchStatus("tr_imp_point_x", 1);
  fChain->SetBranchStatus("tr_imp_point_y", 1);
  fChain->SetBranchStatus("tr_imp_point_z", 1);
  fChain->SetBranchStatus("sa_phi_mb2", 1);
  fChain->SetBranchStatus("sa_phi_me2_p", 1);
  fChain->SetBranchStatus("sa_phi_me2_n", 1);

  fChain->SetBranchStatus("hlt", 1);
}
