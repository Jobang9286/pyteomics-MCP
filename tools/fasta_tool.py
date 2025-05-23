from server import mcp
from pyteomics import fasta

@mcp.tool()
def parse_fasta_ids(fasta_path: str) -> list:
    """
    Parse FASTA file and return protein IDs.

    Args:
        fasta_path: Path to FASTA file.

    Returns:
        List of protein identifiers.
    """
    return [header.split()[0] for header, _ in fasta.read(fasta_path)]
