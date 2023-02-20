#!/bin/bash
gsettings set org.gnome.ControlCenter last-panel ''
env XDG_CURRENT_DESKTOP=GNOME gnome-control-center
