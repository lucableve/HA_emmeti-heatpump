import pytest
from datetime import datetime
from homeassistant.util import dt as dt_util
from custom_components.emmetiHP.sensor import EmmetiHeatpumpSensor


@pytest.fixture
async def sensor_entity(hass):
    # Crea l'entità del sensore
    sensor = EmmetiHeatpumpSensor()
    await sensor.async_added_to_hass()
    return sensor


async def test_sensor_name(sensor_entity):
    """Testa il nome del sensore."""
    assert sensor_entity.name == "Emmeti Heatpump Time"


async def test_sensor_state(sensor_entity):
    """Testa lo stato del sensore."""
    # Aggiorna lo stato del sensore
    await sensor_entity.async_update()
    expected_state = dt_util.now().strftime("%H:%M:%S")

    # Verifica che lo stato del sensore sia uguale al tempo corrente
    assert sensor_entity.state == expected_state
