import matplotlib.pyplot as plt


def plot_incubator_data(data):
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1)

    ax1.plot(data["time"], data["t1"], label="t1")
    ax1.plot(data["time"], data["t2"], label="t2")
    ax1.plot(data["time"], data["t3"], label="t3")
    ax1.plot(data["time"], data["average_temperature"], label="average_temperature")
    ax1.legend()

    ax2.plot(data["time"], data["heater_on"], label="heater_on")
    ax2.plot(data["time"], data["fan_on"], label="fan_on")
    ax2.legend()

    ax3.plot(data["time"], data["execution_interval"], label="execution_interval")
    ax3.plot(data["time"], data["elapsed"], label="elapsed")
    ax3.legend()

    ax4.plot(data["time"], data["power_in"], label="power_in")
    ax4.legend()

    ax5.plot(data["time"], data["energy_in"], label="energy_in")
    ax5.plot(data["time"], data["potential_energy"], label="potential_energy")
    ax5.legend()