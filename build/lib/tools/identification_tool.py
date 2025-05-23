from server import mcp
import pyopenms as oms

@mcp.tool()
def identify_peptides(mzml_path: str, fasta_path: str, out_idxml: str = None) -> str:
    """
    Identify peptides from mzML using SimpleSearchEngine.

    Args:
        mzml_path: Path to the mzML file.
        fasta_path: Path to the FASTA protein database file.
        out_idxml: Path to output idXML file.

    Returns:
        Path to saved idXML file.
    """
    if out_idxml is None:
        out_idxml = mzml_path.replace(".mzML", "_identified.idXML")

    exp = oms.MSExperiment()
    oms.MzMLFile().load(mzml_path, exp)

    search_engine = oms.SimpleSearchEngineAlgorithm()
    params = search_engine.getDefaults()
    params.setValue("database", fasta_path)
    search_engine.setParameters(params)

    proteins = []
    peptides = []
    search_engine.search(exp, proteins, peptides)

    oms.IdXMLFile().store(out_idxml, proteins, peptides)
    return out_idxml
