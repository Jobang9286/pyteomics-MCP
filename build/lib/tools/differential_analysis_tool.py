from server import mcp
import pandas as pd
from scipy.stats import ttest_ind
import os

@mcp.tool()
def compare_groups(quant_csv: str, metadata_csv: str, group_column: str = "Group", 
                   group_a: str = "E3", group_b: str = "E4", output_csv: str = None) -> str:
    """
    Perform differential protein expression analysis between two groups.

    Args:
        quant_csv: CSV file with protein quantification (rows: ProteinID, columns: Sample intensities).
        metadata_csv: CSV file with sample metadata (columns: Sample, Group).
        group_column: Column name in metadata indicating group assignment.
        group_a: First group label (e.g., E3).
        group_b: Second group label (e.g., E4).
        output_csv: Path to save differential expression results.

    Returns:
        Path to saved results CSV.
    """
    if output_csv is None:
        output_csv = "differential_expression_results.csv"

    # Load data
    quant_df = pd.read_csv(quant_csv, index_col=0)
    meta_df = pd.read_csv(metadata_csv)

    # Ensure sample names match
    samples = meta_df["Sample"].values
    quant_df = quant_df[samples]

    # Split groups
    group_a_samples = meta_df[meta_df[group_column] == group_a]["Sample"]
    group_b_samples = meta_df[meta_df[group_column] == group_b]["Sample"]

    results = []

    for protein in quant_df.index:
        vals_a = quant_df.loc[protein, group_a_samples].dropna()
        vals_b = quant_df.loc[protein, group_b_samples].dropna()
        if len(vals_a) >= 2 and len(vals_b) >= 2:
            stat, pval = ttest_ind(vals_a, vals_b, equal_var=False)
            fc = vals_b.mean() / vals_a.mean() if vals_a.mean() > 0 else float("inf")
            log2fc = pd.np.log2(fc) if fc > 0 else 0
        else:
            pval = None
            log2fc = None
        results.append({"ProteinID": protein, "pval": pval, "log2fc": log2fc})

    result_df = pd.DataFrame(results)
    result_df.to_csv(output_csv, index=False)

    return output_csv
