from server import mcp

# Import all Pyteomics-based tools
from tools.ms_loading_tool import load_mzml_summary
from tools.feature_filter_tool import filter_spectra_by_mz
from tools.fasta_tool import parse_fasta_ids
from tools.annotation_tool import annotate_peptide
from tools.quantification_tool import quantify_precursors
from tools.differential_analysis_tool import compare_groups
from tools.pathway_enrichment_tool import run_pathway_enrichment

if __name__ == "__main__":
    mcp.run()
