# STM32F407 DISC BOARD - LED Blinking using MicroPython

## Overview
This project demonstrates how to blink the onboard LEDs of an STM32F407 Discovery Board using MicroPython. It cycles through all four built-in LEDs using a `main.py` script that runs on the board after flashing MicroPython firmware.

## Prerequisites
Before starting, ensure you have the following:

- **STM32F407 Discovery Board**
- **USB ST-LINK debugger cable**
- **ST-Link Utility / STM32CubeProgrammer** installed
- **MicroPython firmware for STM32** (Download from official site)
- **main.py** script for LED blinking
- **Tera Term** (for serial communication)

## Download MicroPython for STM32

You can download the latest MicroPython firmware for STM32 from the official website:

👉 [MicroPython STM32 Downloads](https://micropython.org/download/)

Select the firmware for **STM32F4 - Discovery F4** and download the `.hex` file.

## Flashing MicroPython Firmware

### Step 1: Connect STM32F407 via ST-LINK
Connect the STM32F407 Discovery board to your computer using the ST-LINK USB connector.

### Step 2: Flash Using STM32CubeProgrammer
1. Open **STM32CubeProgrammer**.
2. Connect to the board using **ST-LINK**.
3. Select the downloaded `.hex` MicroPython firmware.
4. Click **Start Programming** to flash the board.
5. After flashing, the board is ready to run `.py` scripts.

## Creating and Uploading main.py

After flashing MicroPython:

1. Use **Tera Term**, **Thonny IDE**, **rshell**, **mpremote**, or **PuTTY** to connect to your board over USB.
2. Create a file named `main.py`.
3. Paste the LED blinking code into `main.py`.
4. Save and run the script on the STM32 board.

You can also use **Tera Term** to run the script manually:
- Open Tera Term and connect to the correct COM port.
- Paste or type your `main.py` codeand **enter** to run code present in `main.py`
- Press `Ctrl+D` to **Soft reboot: Restarts the board and executes main.py if it exists** the script.
- Press `Ctrl+C` to perform a **Interrupt: Stops a currently running script in the REPL**.

## LED Blinking Code (`main.py`)

```python
# main.py
import pyb
import time  

# LED sequence for list
led_sequence = [1, 3, 2, 4, 1, 3, 2, 4, 1, 3, 2, 4]

for led in led_sequence:
    pyb.LED(led).on()  # Turn ON the LED
    time.sleep(1)  # Wait 1 second
    pyb.LED(led).off()  # Turn OFF the LED
```

### Explanation:
- `pyb.LED(n)`: Accesses the onboard LED numbered `n` (1 to 4).
- `on()` / `off()`: Turns the LED on or off.
- The script cycles through the LED sequence three times with a 1-second delay between transitions.

## Cloning this Repository

You can clone this GitHub repository using:

```sh
git clone https://github.com/AbisheckD/Python_in_STM32.git
cd Python_in_STM32
```

## Troubleshooting

- **Board Not Detected?** Ensure correct USB cable and ST-LINK driver are installed.
- **Script not running?** Make sure the filename is `main.py`. MicroPython runs this file on boot.
- **Tera Term not responding?** Ensure you are using the correct COM port and baud rate (typically 115200).
- **Permission Issues?** Try running Tera Term or terminal as administrator.
- **Soft Reset/Run**: In Tera Term, use:
  - Press `Ctrl+D` to **Soft reboot: Restarts the board** the script.
  - Press `Ctrl+C` to perform a **Interrupt: Current running script**.

## License
This project is open-source and available under the MIT License.

## Contributing
Feel free to fork this repository, create pull requests, or report issues. Contributions are welcome!

---

🔗 **GitHub Repository:** [AbisheckD/Python_in_STM32](https://github.com/AbisheckD/Python_in_STM32)
