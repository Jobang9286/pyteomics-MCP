from server import mcp
from pyteomics import mzml

@mcp.tool()
def load_mzml_summary(file_path: str) -> dict:
    """
    Load mzML file and summarize spectrum count and retention times.

    Args:
        file_path: Path to the mzML file.

    Returns:
        Summary dict.
    """
    with mzml.MzML(file_path) as reader:
        n_spectra = sum(1 for _ in reader)
        rts = [spec['scanList']['scan'][0]['scan start time'] for spec in reader if 'scanList' in spec]
    return {
        "n_spectra": n_spectra,
        "min_rt": min(rts) if rts else None,
        "max_rt": max(rts) if rts else None
    }
