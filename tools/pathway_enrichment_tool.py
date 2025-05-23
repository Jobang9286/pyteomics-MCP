from server import mcp
import pandas as pd

@mcp.tool()
def run_pathway_enrichment(protein_list: list, organism: str = "Mouse", gene_set: str = "GO_Biological_Process_2021", 
                           output_csv: str = "enrichment.csv") -> str:
    """
    Run pathway enrichment via gseapy.

    Args:
        protein_list: List of gene/protein symbols.
        organism: Species.
        gene_set: Enrichr gene set name.
        output_csv: Save path.

    Returns:
        Output path.
    """
    import gseapy as gp
    enr = gp.enrichr(gene_list=protein_list, gene_sets=gene_set,
                     organism=organism, outdir=None, no_plot=True)
    enr.results.to_csv(output_csv, index=False)
    return output_csv
