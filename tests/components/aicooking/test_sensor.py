"""Test the INKBIRD config flow."""


from homeassistant.components.aicooking.const import DOMAIN
from homeassistant.components.sensor import ATTR_STATE_CLASS
from homeassistant.const import ATTR_FRIENDLY_NAME, ATTR_UNIT_OF_MEASUREMENT

from . import BBQ_SERVICE_INFO

from tests.common import MockConfigEntry
from tests.components.bluetooth import inject_bluetooth_service_info


async def test_sensors(hass):
    """Test setting up creates the sensors."""
    entry = MockConfigEntry(
        domain=DOMAIN,
        unique_id="aa:bb:cc:dd:ee:ff",
    )
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_all()) == 0
    inject_bluetooth_service_info(hass, BBQ_SERVICE_INFO)
    await hass.async_block_till_done()
    assert len(hass.states.async_all()) == 1

    temp_sensor = hass.states.get("sensor.bbq_temperature")
    temp_sensor_attribtes = temp_sensor.attributes
    assert temp_sensor.state == "21.1"
    assert temp_sensor_attribtes[ATTR_FRIENDLY_NAME] == "BBQ Temperature"
    assert temp_sensor_attribtes[ATTR_UNIT_OF_MEASUREMENT] == "°C"
    assert temp_sensor_attribtes[ATTR_STATE_CLASS] == "measurement"

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
