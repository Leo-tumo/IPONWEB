#!/bin/bash
function gm() {
     git add . && git commit -am "$1" && git push origin main
}

gm "$1"
