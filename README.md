# MarantzAmpWebAPI
A super hacked together web api for issuing commands to a Marantz PM6005 Amp. 

## Description
A super basic Python Flask Web API used for controlling a Marantz PM6005 via ir-ctl in Linux. 

The "API" has several basic commands, each of which is mapped to the IR Code required to perform the action on the amp. 
It requires a Raspberry Pi and an IR LED - in this case just using a breadboard.

Can be used via Node Red for nice Home Automation integration. 
