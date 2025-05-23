from server import mcp
import pyopenms as oms

@mcp.tool()
def load_mzml(file_path: str) -> dict:
    """
    Load mzML file and summarize basic information.

    Args:
        file_path: Path to the mzML file.

    Returns:
        A dictionary with number of spectra and chromatograms.
    """
    exp = oms.MSExperiment()
    oms.MzMLFile().load(file_path, exp)

    return {
        "n_spectra": len(exp.getSpectra()),
        "n_chromatograms": len(exp.getChromatograms()),
        "summary": f"{len(exp.getSpectra())} spectra and {len(exp.getChromatograms())} chromatograms loaded."
    }
