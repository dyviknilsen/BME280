BME280 Indoor Climate Presentation Page by Jonas Dyvik Nilsen v1.0, February 2nd 2019

This school project was created to not only display, but also analyze the results from a BME280 sensor unit, connected to an ESP32 microcontroller running MicroPython.

Features:

	- Displays three sensor values (Temperature, Relative Humidity and Atmospheric Pressure) in a numeric and visual form, together with a dynamic color and written statement that changes based on the result.
	- Failsafe system to keep the progression bars from going below 1% or above 100%, ensuring that the bar stays within it's limits and always displays a color.
	- Dynamic web page that adapts to the resolution of the device screen.
	- Refresh button to easily update the results displayed.
	- 5 second automatic refresh commented out in the HTML document.
	- Separate CSS document and favicon folder located on the https://dyviknilsen.no domain. Files included in separate folder.
	
Credits:
	https://www.w3schools.com
