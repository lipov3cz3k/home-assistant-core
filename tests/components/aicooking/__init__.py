"""Tests for the Aicooking integration."""
from homeassistant.helpers.service_info.bluetooth import BluetoothServiceInfo

NOT_AICOOKING_SERVICE_INFO = BluetoothServiceInfo(
    name="Not it",
    address="61DE521B-F0BF-9F44-64D4-75BBE1738105",
    rssi=-63,
    manufacturer_data={3234: b"\x00\x01"},
    service_data={},
    service_uuids=[],
    source="local",
)

BBQ_SERVICE_INFO = BluetoothServiceInfo(
    name="BBQ",
    address="aa:bb:cc:dd:ee:ff",
    rssi=-56,
    manufacturer_data={21930: b"21.1"},
    service_uuids=["0000180a-0000-1000-8000-00805f9b34fb"],
    service_data={},
    source="local",
)
