import pytest
from homeassistant import config_entries
from custom_components.emmetiHP import config_flow

@pytest.fixture(autouse=True)
def disable_socket_blocking():
    pytest.importorskip("pytest_socket").enable_socket()

@pytest.fixture
async def setup_integration(hass):
    flow = config_flow.EmmetiHeatpumpConfigFlow()
    flow.hass = hass
    return flow

@pytest.mark.asyncio
async def test_config_flow_user(setup_integration):
    result = await setup_integration.async_step_user({
        "username": "test_user",
        "password": "test_pass",
        "polling_interval": 60
    })

    assert result["type"] == config_entries.FlowResultType.CREATE_ENTRY
    assert result["title"] == "Emmeti Heatpump"
    assert result["data"]["username"] == "test_user"
    assert result["data"]["password"] == "test_pass"
    assert result["data"]["polling_interval"] == 60
