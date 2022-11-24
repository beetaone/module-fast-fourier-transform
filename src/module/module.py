"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

import lzma
import numpy as np
from scipy.fft import rfft
from scipy.signal import find_peaks
from logging import getLogger
from .params import PARAMS
import base64

log = getLogger("module")


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        # decompress data
        decompressed_superposed_bytes = lzma.decompress(base64.b64decode(received_data[PARAMS["INPUT_LABEL"]]))
        superposed_waveform = np.frombuffer(decompressed_superposed_bytes)

        # detect frequencies and magnitudes
        freq_data = rfft(superposed_waveform)
        x_frequency = np.linspace(0.0, PARAMS["SAMPLE_SIZE"] / 2, int(len(superposed_waveform) / 2))
        y_amplitude = 2 / len(superposed_waveform) * np.abs(freq_data[0:int(len(superposed_waveform) / 2)])
        peaks_index, properties = find_peaks(y_amplitude, prominence=1, width=0)

        # construct output data
        processed_data = []
        for i in range(len(peaks_index)):

            peaks = {'frequency': x_frequency[peaks_index[i]], 'magnitude': properties['prominences'][i]}
            processed_data.append(peaks)

        return processed_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
