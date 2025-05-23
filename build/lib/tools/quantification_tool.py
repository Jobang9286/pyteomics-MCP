from server import mcp
import pyopenms as oms
import pandas as pd

@mcp.tool()
def quantify_proteins(featurexml_path: str, idxml_path: str, output_csv: str = None) -> str:
    """
    Quantify proteins by mapping features and peptide identifications.

    Args:
        featurexml_path: Path to the featureXML file.
        idxml_path: Path to the idXML file.
        output_csv: Output CSV path to store protein intensities.

    Returns:
        Path to the saved CSV file with protein quantification.
    """
    if output_csv is None:
        output_csv = featurexml_path.replace(".featureXML", "_protein_quant.csv")

    # Load features and identifications
    features = oms.FeatureMap()
    oms.FeatureXMLFile().load(featurexml_path, features)

    proteins = []
    peptides = []
    oms.IdXMLFile().load(idxml_path, proteins, peptides)

    # Map identifications to features
    id_mapper = oms.IDMapper()
    id_mapper.annotate(features, peptides, proteins)

    # Aggregate intensity per protein
    protein_intensity = {}
    for feature in features:
        for hit in feature.getPeptideIdentifications():
            if hit.getHits():
                protein_ids = hit.getHits()[0].extractProteinAccessions()
                intensity = feature.getIntensity()
                for pid in protein_ids:
                    protein_intensity[pid] = protein_intensity.get(pid, 0.0) + intensity

    # Save to CSV
    df = pd.DataFrame(list(protein_intensity.items()), columns=["ProteinID", "Intensity"])
    df.to_csv(output_csv, index=False)

    return output_csv
