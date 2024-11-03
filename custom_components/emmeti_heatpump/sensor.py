from homeassistant.helpers.entity import Entity
import homeassistant.util.dt as dt_util

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([EmmetiHeatpumpSensor()])

class EmmetiHeatpumpSensor(Entity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "Emmeti Heatpump Time"

    @property
    def state(self):
        return self._state

    def update(self):
        self._state = dt_util.now().strftime("%H:%M:%S")
