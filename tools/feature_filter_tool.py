from server import mcp
from pyteomics import mzml

@mcp.tool()
def filter_spectra_by_mz(file_path: str, mz_min: float, mz_max: float, out_path: str = "filtered_spectra.txt") -> str:
    """
    Filter spectra by precursor m/z range and save summary.

    Args:
        file_path: mzML input path.
        mz_min: Minimum precursor m/z.
        mz_max: Maximum precursor m/z.
        out_path: Output text file with filtered precursor info.

    Returns:
        Path to saved file.
    """
    with mzml.MzML(file_path) as reader:
        filtered = []
        for spec in reader:
            prec = spec.get('precursorList', {}).get('precursor', [{}])[0]
            ion = prec.get('selectedIonList', {}).get('selectedIon', [{}])[0]
            mz = ion.get('selected ion m/z')
            if mz and mz_min <= mz <= mz_max:
                filtered.append((spec['id'], mz))

    with open(out_path, 'w') as f:
        for sid, mz in filtered:
            f.write(f"{sid}	{mz}\n")

    return out_path
