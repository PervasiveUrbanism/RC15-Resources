# Arduino Sensor Input into vvvv

Part of **RC15 Resources**, the permanent tutorial library for Pervasive Urbanism.

**Software:** Arduino, vvvv gamma  
**Format:** Arduino sketch and vvvv example patch  
**Software version:** The vvvv patch references 2024.6; compatibility with newer versions has not been verified.  
**Original collection:** 240208_Arduino to vvvv

[Browse this topic](../README.md) | [Library home](../../../README.md)

## About this example

A physical sensor can turn changes in an environment into a stream of numerical measurements. This example shows a simple workflow from **Arduino sensor input** to **serial data**, then to **visualisation and recording in vvvv**. Similar methods can be used to investigate changing light conditions or other environmental signals in architectural and urban experiments.

The supplied [Arduino sketch](LightSensor/LightSensor.ino) reads analogue input `A0` and transmits its value as a line of text every **200 milliseconds**. The [vvvv patch](Arduino%20Savevalues%20and%20Graph.vl) uses serial communication to receive the values and includes components for plotting and writing them to a file.

## Explore the example

1. **Prepare the Arduino.** Open [LightSensor.ino](LightSensor/LightSensor.ino) in the Arduino IDE and upload it to your board. The code reads `analogRead(A0)`, so the sensor circuit must provide a suitable **analogue voltage** at that pin. The original wiring is not documented: check the sensor type, its required circuit and your board's permitted input-voltage range before connecting anything. Do not connect an unknown sensor voltage directly to the pin.
2. **Check the readings.** Open the Arduino IDE's Serial Monitor at **9600 baud**. You should see a new integer reading roughly five times per second. Changing the light reaching a correctly connected light-sensitive circuit should alter the numbers. The numeric range depends on the board's ADC resolution and configuration; the readings are not automatically calibrated light measurements.
3. **Connect vvvv.** Close Serial Monitor before opening the serial connection in [Arduino Savevalues and Graph.vl](Arduino%20Savevalues%20and%20Graph.vl), since the port generally cannot be used by both applications at once. Select the correct serial port and **9600 baud** in the vvvv `SerialPort4` setup. The Arduino sends one reading per line using `Serial.println()`; check how the patch separates and converts these incoming values.
4. **Inspect and record.** Follow the visualisation and file-writing sections in the patch. Compare how changing the sensor input affects the display and inspect the destination path before saving measurements.

The intent is to understand how physical measurements become data that can be stored, graphed and reused. Consider what the sensor actually measures and what further calibration or contextual information would be needed before drawing conclusions about a space.

## Troubleshooting

If no values arrive, confirm the USB connection, correct serial port, **9600 baud** setting and whether another application is using the port. If values are fixed or implausible, inspect the analogue wiring, common ground, sensor voltage and the values shown in Serial Monitor before troubleshooting vvvv. If a file is not created, check the output path and write permissions.

**Desktop and hardware verification pending:** The original sensor wiring, the vvvv serial parsing, graph and file export have not been tested during this editorial review. The patch's compatibility with current vvvv versions also needs checking; see the [editorial backlog](../../../EDITORIAL_BACKLOG.md).
