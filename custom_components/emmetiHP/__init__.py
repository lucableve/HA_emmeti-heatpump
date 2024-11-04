"""The Emmeti Heatpump integration."""

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

DOMAIN = "emmetiHP"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Emmeti Heatpump component."""
    hass.data[DOMAIN] = {}

    # Registrare i componenti qui, ad esempio i sensori
    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, config)

    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up Emmeti Heatpump from a config entry."""
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Configurare i sensori e altre entità qui
    await discovery.async_load_platform(hass, "sensor", DOMAIN, {}, entry)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Unload a config entry."""
    unload_ok = await discovery.async_unload_platform(hass, "sensor", entry)

    # Rimuovere l'entry dai dati dell'integrazione
    hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
