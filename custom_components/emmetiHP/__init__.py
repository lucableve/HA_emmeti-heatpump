import logging
from datetime import timedelta
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_USERNAME, CONF_PASSWORD

DOMAIN = "emmetiHP"
_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USERNAME): str,
        vol.Required(CONF_PASSWORD): str,
        vol.Optional(CONF_NAME): str,
    })
}, extra=vol.ALLOW_EXTRA)

async def async_setup(hass, config):
    if DOMAIN not in config:
        return True

    return True

async def async_setup_entry(hass, entry):
    """Set up Emmeti HP from a config entry."""
    _LOGGER.debug("Setting up Emmeti HP...")
    # Logica di configurazione qui
    return True

async def async_unload_entry(hass, entry):
    """Unload an entry."""
    _LOGGER.debug("Unloading Emmeti HP...")
    return True
