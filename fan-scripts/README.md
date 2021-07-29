## Fan Control
These two scripts allows manual control over the GPU fan speeds.

**Prerequisite:**

 - Enable manual configuration of GPU fan speed on the _Thermal Monitor_ page in _nvidia-settings_.

		sudo nvidia-xconfig --enable-all-gpus --cool-bits=4
		sudo init 6


To take over control from system control and set fans to 100%, run `./fan_up.sh`. 
To relinquish fan control to system, run `./fan_down.sh`. 
