{
    gROOT->ProcessLine(".x ../L1TriggerDPG/L1Ntuples/macros/initL1Analysis.C");
    gROOT->ProcessLine(".L L1MuEff_ChargeAssignment_ntupleCreator.C+");
    gROOT->ProcessLine("L1MuEff_ChargeAssignment_ntupleCreator macro = L1MuEff_ChargeAssignment_ntupleCreator(\"ntuple_list\");");
    gROOT->ProcessLine("macro.run(-1);");
}
