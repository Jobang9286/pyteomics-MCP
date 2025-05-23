from server import mcp
import pandas as pd
from scipy.stats import ttest_ind

@mcp.tool()
def compare_groups(quant_csv: str, metadata_csv: str, group_column: str = "Group", 
                   group_a: str = "E3", group_b: str = "E4", output_csv: str = None) -> str:
    """
    Perform differential analysis of precursor intensities between two groups.

    Args:
        quant_csv: CSV with intensity data (rows: IDs, columns: samples).
        metadata_csv: CSV with sample metadata.
        group_column: Column with group info.
        group_a: Group A label.
        group_b: Group B label.
        output_csv: Path to save results.

    Returns:
        Path to results file.
    """
    if output_csv is None:
        output_csv = "differential_results.csv"

    df = pd.read_csv(quant_csv, index_col=0)
    meta = pd.read_csv(metadata_csv)
    g1 = meta[meta[group_column] == group_a]['Sample']
    g2 = meta[meta[group_column] == group_b]['Sample']

    results = []
    for id in df.index:
        x, y = df.loc[id, g1].dropna(), df.loc[id, g2].dropna()
        if len(x) >= 2 and len(y) >= 2:
            stat, p = ttest_ind(x, y)
            logfc = (y.mean() / x.mean()) if x.mean() != 0 else 0
            results.append({"id": id, "pval": p, "log2fc": pd.np.log2(logfc)})

    pd.DataFrame(results).to_csv(output_csv, index=False)
    return output_csv
