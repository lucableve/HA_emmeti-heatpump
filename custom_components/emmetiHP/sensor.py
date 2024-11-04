from homeassistant.helpers.entity import Entity
import homeassistant.util.dt as dt_util
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    username = config_entry.data["username"]
    password = config_entry.data["password"]
    polling_interval = config_entry.data["polling_interval"]

    # Per ora, mostriamo solo un sensore con l'ora corrente
    async_add_entities([EmmetiHeatpumpSensor(polling_interval)])

class EmmetiHeatpumpSensor(Entity):
    def __init__(self, polling_interval):
        self._state = None
        self._polling_interval = polling_interval

    @property
    def name(self):
        return "Emmeti Heatpump Time"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        # Aggiorna l'ora corrente come esempio
        self._state = dt_util.now().strftime("%H:%M:%S")
