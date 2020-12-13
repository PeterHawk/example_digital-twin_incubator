from oomodelling import Model

from digital_twin.models.controller_models.controller_model import ControllerModel
from digital_twin.models.plant_models.four_parameters_model.four_parameter_model import FourParameterIncubatorPlant
from digital_twin.monitoring.kalman_filter_4p import KalmanFilter4P
from digital_twin.monitoring.noise_model import NoiseFeedthrough


class KalmanSystemModel(Model):
    def __init__(self, step_size, std_dev,
                 C_air,
                 G_box,
                 C_heater,
                 G_heater):
        super().__init__()

        self.ctrl = ControllerModel(desired_temperature=35)
        self.plant = FourParameterIncubatorPlant(C_air=C_air,
                                                 G_box=G_box,
                                                 C_heater=C_heater,
                                                 G_heater=G_heater)
        self.noise_sensor = NoiseFeedthrough(std_dev)
        self.kalman = KalmanFilter4P(step_size, std_dev,
                                     C_air=C_air,
                                     G_box=G_box,
                                     C_heater=C_heater,
                                     G_heater=G_heater)

        self.std_dev = self.var(lambda: 0.1 if self.time()<100 else (1.2 if self.time()<150 else 0.1))
        self.noise_sensor.std_dev = self.std_dev
        self.noise_sensor.u = self.plant.T
        self.ctrl.in_temperature = self.noise_sensor.y
        self.plant.in_heater_on = self.ctrl.heater_on

        self.kalman.in_heater_on = self.ctrl.heater_on
        self.kalman.in_T = self.noise_sensor.y

        self.save()
