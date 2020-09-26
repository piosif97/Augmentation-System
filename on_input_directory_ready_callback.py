import abc


class OnInputDirectoryReadyCallback(abc.ABC):
    @abc.abstractmethod
    def on_input_directory_ready_callback(self, input_directory):
        pass
