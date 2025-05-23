from server import mcp
import pyopenms as oms

@mcp.tool()
def run_feature_finder_centroided(mzml_path: str, out_featurexml: str = None) -> str:
    """
    Run feature finding on centroided MS data using FeatureFinderCentroided.

    Args:
        mzml_path: Path to input mzML file.
        out_featurexml: Path to output featureXML file.

    Returns:
        Path to saved featureXML file.
    """
    if out_featurexml is None:
        out_featurexml = mzml_path.replace(".mzML", "_features.featureXML")

    exp = oms.MSExperiment()
    oms.MzMLFile().load(mzml_path, exp)

    features = oms.FeatureMap()
    ff = oms.FeatureFinder()
    ff.setLogType(oms.LogType.NONE)
    ff.run("centroided", exp, features, oms.Param(), oms.FeatureFinder().getDefaults())

    oms.FeatureXMLFile().store(out_featurexml, features)
    return out_featurexml
