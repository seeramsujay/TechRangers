import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))
import dss.database

dss.database.fetch_eligibility_rules = MagicMock(return_value=[
    {"scheme_name": "PM-KISAN", "attribute": "land_holding_ha", "operator": "<=", "value": "2.0"},
    {"scheme_name": "Jal Jeevan Mission", "attribute": "tap_water_access", "operator": "=", "value": "False"}
])

from dss.dss_engine import RuleEngine, DSSEngine

def test_rule_engine_evaluation_pass():
    engine = RuleEngine()
    data = {"land_holding_ha": 1.5}
    met, justifications = engine.evaluate("PM-KISAN", data)
    assert met is True
    assert len(justifications) == 0

def test_rule_engine_evaluation_fail():
    engine = RuleEngine()
    data = {"land_holding_ha": 3.5}
    met, justifications = engine.evaluate("PM-KISAN", data)
    assert met is False
    assert any("Condition not met" in j for j in justifications)

def test_dss_engine_schemes():
    dss = DSSEngine()
    assert "PM-KISAN" in dss.schemes_info
    assert "Jal Jeevan Mission" in dss.schemes_info
    assert dss.schemes_info["PM-KISAN"]["priority"] == 1

def test_sql_schemas_presence():
    assert Path("dss_schema.sql").exists()
    assert Path("dss_materialized_view.sql").exists()
