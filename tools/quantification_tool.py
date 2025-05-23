from server import mcp
from pyteomics import mzml
import pandas as pd

@mcp.tool()
def quantify_precursors(mzml_path: str, out_csv: str = "precursor_intensities.csv") -> str:
    """
    Quantify precursor ion intensities from mzML.

    Args:
        mzml_path: mzML input path.
        out_csv: Output CSV file.

    Returns:
        Path to saved CSV.
    """
    data = []
    with mzml.MzML(mzml_path) as reader:
        for spec in reader:
            prec = spec.get('precursorList', {}).get('precursor', [{}])[0]
            ion = prec.get('selectedIonList', {}).get('selectedIon', [{}])[0]
            mz = ion.get('selected ion m/z')
            inten = ion.get('peak intensity')
            if mz and inten:
                data.append({"id": spec['id'], "mz": mz, "intensity": inten})
    pd.DataFrame(data).to_csv(out_csv, index=False)
    return out_csv
