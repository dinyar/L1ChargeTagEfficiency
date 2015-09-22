{
  gROOT->ProcessLine(".x ../../L1TriggerDPG/L1Ntuples/macros/initL1Analysis.C");
  gROOT->ProcessLine(".L GMTChargeAssignmentNtupleizer.C+");
  gROOT->ProcessLine(
      "GMTChargeAssignmentNtupleizer macro = "
      "GMTChargeAssignmentNtupleizer(\"ntuple_list\");");
  gROOT->ProcessLine("macro.run(-1);");
}
