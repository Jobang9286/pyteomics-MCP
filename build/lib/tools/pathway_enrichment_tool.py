from server import mcp
import pandas as pd
from typing import List
import os

@mcp.tool()
def run_pathway_enrichment(protein_list: List[str], organism: str = "Mouse", gene_set: str = "GO_Biological_Process_2021", 
                           output_csv: str = "pathway_enrichment_results.csv") -> str:
    """
    Run pathway enrichment analysis using Enrichr via gseapy.

    Args:
        protein_list: List of significant protein/gene symbols.
        organism: 'Mouse' or 'Human'.
        gene_set: Gene set library to use (e.g., GO_Biological_Process_2021).
        output_csv: Path to save enrichment results.

    Returns:
        Path to saved results CSV.
    """
    try:
        import gseapy as gp
    except ImportError:
        raise ImportError("gseapy is not installed. Run 'pip install gseapy'.")

    enr = gp.enrichr(gene_list=protein_list,
                     gene_sets=gene_set,
                     organism=organism,
                     description="PathwayEnrichment",
                     outdir=None,
                     no_plot=True)

    df = enr.results
    df.to_csv(output_csv, index=False)
    return output_csv
