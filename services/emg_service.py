import numpy as np
from typing import List, Tuple

from matplotlib import pyplot as plt
from scipy import signal

from models import EMGModel


class EMGService:
    def __init__(self):
        pass

    # region Private
    # noinspection PyMethodMayBeStatic
    def __butter(self, data: List[float]) -> List[float]:
        """
        1-Hz lowpass Butterworth filter was applied as recommended in [10]
        [10] S. Thomas, S. Ganapathy, G. Saon, and H. Soltau, “Analyzing convolutional neural networks for speech activity detection in mismatched acoustic conditions,” in Acoustics, Speech and Signal Processing (ICASSP), 2014 IEEE International Conference on, 2014, pp. 2519–2523
        :param data: EMG signal data
        :return: List[float]
        """
        # check emg_position
        if data is None or len(data) == 0:
            self.__log.error(message="The data parameter was none or empty in the __butter function")
            return list()

        fc = 0.05
        fs = 1.0
        wn = fc / (fs * 0.5)
        b, a = signal.butter(4, wn, analog=False)
        return signal.lfilter(b, a, data)
    # end __butter()

    # noinspection PyMethodMayBeStatic
    def __stft(self, data: List[float]) -> Tuple[List[float], List[float], List[float]]:
        f, t, zxx = signal.stft(
            data,
            fs=1.0,
            window='hamming',
            nperseg=50,
            noverlap=20,
            nfft=256,
        )

        # https://www.youtube.com/watch?v=g1_wcbGUcDY
        # see better (power in dBs)
        size_x, size_y = zxx.shape
        power = np.zeros((size_x, size_y), dtype="float64")
        for x in range(size_x):
            for y in range(size_y):
                if zxx[x, y] != 0:
                    power[x, y] = 10 * np.log10(np.abs(zxx[x, y]))
        return f, t, power
    # end __stft()
    # endregion

    # region Public
    def show_action(self, title: str, action_names: List[str], emg_data: List[EMGModel], low_pass: bool = False,
                    multi_figure: bool = False):
        # check action_name_list
        if action_names is None or len(action_names) == 0:
            self.__log.error(message="The action_name_list parameter was none or empty in the show_action function")
            return

        # check emg_data
        if emg_data is None or len(emg_data) == 0:
            self.__log.error(message="The emg_data parameter was none or empty in the show_action function")
            return

        number_subplot: int = len(emg_data)
        fig, axs = plt.subplots(nrows=number_subplot, ncols=1)
        fig.suptitle(title)
        fig.subplots_adjust(left=0.05, bottom=0.05, right=0.96, top=0.94, hspace=2.5)

        for index in range(number_subplot):
            data: List[float] = emg_data[index]
            data = data if not low_pass else self.__butter(data)
            axs[index].set_title(action_names[index])
            axs[index].set_xlim([0, len(data)])
            axs[index].set_xticks((np.arange(0, len(data) + 1000, 1000)))
            axs[index].set_ylim([min(data), max(data)])
            axs[index].plot(data)

        for ax in axs.flat:
            ax.set(xlabel="Time [millisecond]", ylabel="Amplitude [μV]")

        if not multi_figure:
            plt.show()
    # end show_action()

    def show_action_spectrogram(self, title: str, action_names: List[str], emg_data: List[EMGModel],
                                low_pass: bool = False, multi_figure: bool = False):
        # check action_name_list
        if action_names is None or len(action_names) == 0:
            self.__log.error(message="The action_name_list parameter was none or empty in the show_action function")
            return

        # check emg_data
        if emg_data is None or len(emg_data) == 0:
            self.__log.error(message="The emg_data parameter was none or empty in the show_action function")
            return

        number_subplot: int = len(emg_data)
        fig, axs = plt.subplots(nrows=number_subplot, ncols=1)
        fig.suptitle(title)
        fig.subplots_adjust(left=0.05, bottom=0.05, right=0.96, top=0.94, hspace=0.8)

        for index in range(number_subplot):
            data: List[float] = emg_data[index]
            data = data if not low_pass else self.__butter(data)
            f, t, zxx = self.__stft(data)
            axs[index].set_title(action_names[index])
            axs[index].set_xlim([0, len(data)])
            axs[index].set_xticks((np.arange(0, len(data) + 1000, 1000)))
            axs[index].pcolormesh(t, f, zxx, cmap="viridis")

        if not multi_figure:
            plt.show()
    # end show_action_spectrogram()
    # endregion
# end class EMGService
