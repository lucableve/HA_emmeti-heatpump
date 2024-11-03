import logging
import aiohttp
from homeassistant import config_entries
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class EmmetiHeatPumpFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            username = user_input[CONF_USERNAME]
            password = user_input[CONF_PASSWORD]

            # Verifica delle credenziali
            if await self.check_credentials(username, password):
                # Se le credenziali sono corrette, procedi con la configurazione
                return self.async_create_entry(title=username, data=user_input)
            else:
                # Se le credenziali sono errate, mostra un errore
                return self.async_show_form(
                    step_id="user",
                    data=user_input,
                    errors={"base": "invalid_auth"},
                )

        return self.async_show_form(step_id="user")

    async def check_credentials(self, username, password):
        """Controlla le credenziali con la REST API di Emmeti."""
        url = "https://emmeti.aq-iot.net/aq-iot-server-frontend-ha/api/v1/auth/login"
        headers = {
            "sec-ch-ua-platform": "Windows",
            "Referer": "https://emmeti.aq-iot.net/aq-iot-app-emmeti/page/FBDEVLIST",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "Accept": "application/json, text/plain, */*",
            "sec-ch-ua": 'Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?0",
        }
        data = {
            "username": username,
            "password": password,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=data) as response:
                    if response.status == 200:
                        # Estrazione del token JWT dagli header
                        token = response.headers.get("Authorization")
                        if token:
                            _LOGGER.info("Token ricevuto: %s", token)
                            # Qui puoi memorizzare il token per uso futuro
                            return True
                    else:
                        _LOGGER.error("Credenziali non valide: %s", response.status)
                        return False
        except Exception as e:
            _LOGGER.error("Error connecting to Emmeti API: %s", e)
            return False
