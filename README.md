# CTSimulation
CT Scan Simulation with a given signal-to-noise ratio

Included in `ComputedTomographySimulation.py` is a method named `simulate_ct` which takes as an argument a two-dimensional NumPy array (image) and a signal-to-noise ratio (snr).
<br>
<br>
Running the simulation with a quarter-circle, we can vary the snr to simulate the scan.
<br>

Here is the image beside its sinogram (Radon transform)<br>

![alt text](https://github.com/D-Thatcher/CTSimulation/blob/master/100_radon.png)

And the simulated resultant CT images:<br>

<b>Signal-to-Noise Ratio : 100<b><br>

![alt text](https://github.com/D-Thatcher/CTSimulation/blob/master/100_inverse.png)


<b>Signal-to-Noise Ratio : 1<b><br>

![alt text](https://github.com/D-Thatcher/CTSimulation/blob/master/1_inverse.png)
