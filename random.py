import psutil as psutil

"""
Module viginere.py
"""


class Random:
    """
    Class for generating random number.
    """

    __author__ = "Temuri Takalandze <me@abgeo.dev>"
    __copyright__ = "Copyright 2019, abgeo.dev"
    __license__ = "MIT"
    __version__ = "0.9"
    __maintainer__ = "Temrui Takalandze"
    __email__ = "me@abgeo.dev"
    __status__ = "Development"

    @classmethod
    def get_random_number(cls):
        ctx_switches, interrupts, soft_interrupts, syscalls = psutil.cpu_stats()
        bat_percent, secsleft, power_plugged = psutil.sensors_battery()
        freq_current, freq_min, freq_max = psutil.cpu_freq()

        random_number = ((ctx_switches % soft_interrupts / bat_percent * secsleft) % freq_current) * interrupts

        return random_number
