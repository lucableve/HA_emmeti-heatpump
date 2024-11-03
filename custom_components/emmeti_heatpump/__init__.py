from homeassistant import config_entries
from .config_flow import EmmetiHeatpumpConfigFlow

async def async_setup(hass, config):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    # Logica di setup per il componente
    return True

# Registrazione del flusso di configurazione
config_entries.HANDLERS.register("emmeti_heatpump")(EmmetiHeatpumpConfigFlow)
