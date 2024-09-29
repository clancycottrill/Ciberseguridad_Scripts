#!/bin/bash

# Monitorear conexiones de red activas y mostrar la salida en la terminal
netstat -tunapl | grep ESTABLISHED