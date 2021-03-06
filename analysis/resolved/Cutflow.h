#pragma once
#include <string>
#include <vector>

#include <ROOT/RResultPtr.hxx>
#include <RtypesCore.h>
#include <TFile.h>

/// TResultProxy for Count()
using CountProxy = ROOT::RDF::RResultPtr<ULong64_t>;

/// Store cutflow and write as ROOT::TH1.
class Cutflow {

public:
  Cutflow() = default;
  Cutflow(const std::string &name /**< [in] Cutflow (and TH1) name*/,
          TFile &file /**< [out] File to save to*/)
      : file(&file), name(name), labels(), values() {}

  /// Add entry to cutflow
  inline void add(const std::string &label, CountProxy &&value) {
    labels.push_back(label);
    values.push_back(value);
  }

  /// Get value for entry
  ULong64_t get(const std::string &label);

  /// Write cutflow to file
  void write();

private:
  std::vector<std::string> labels;
  std::vector<CountProxy> values;
  TFile *file;
  const std::string name;
};
