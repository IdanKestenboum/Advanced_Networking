#!/bin/bash

nc -w 5 10.9.0.5 9090
if [ $? -eq 0 ]; then
	echo "connection successful"
else
	echo "connection failed or timed out"
fi
