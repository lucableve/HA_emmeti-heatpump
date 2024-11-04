from homeassistant import config_entries
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("username"): cv.string,
    vol.Required("password"): cv.string,
    vol.Required("polling_interval", default=60): cv.positive_int,
})


class EmmetiHeatpumpConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Emmeti Heatpump", data=user_input)

        return self.async_show_form(step_id="user", data_schema=DATA_SCHEMA)
