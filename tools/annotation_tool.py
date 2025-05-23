from server import mcp
from pyteomics import parser, mass

@mcp.tool()
def annotate_peptide(peptide: str, ion_type: str = 'b') -> dict:
    """
    Annotate fragment ions for a peptide.

    Args:
        peptide: Peptide sequence.
        ion_type: Fragment ion type ('b' or 'y').

    Returns:
        Ion m/z values.
    """
    ions = {}
    for i in range(1, len(peptide)):
        ions[f'{ion_type}{i}'] = mass.fast_mass(peptide[:i] if ion_type == 'b' else peptide[-i:], ion_type=ion_type)
    return ions
