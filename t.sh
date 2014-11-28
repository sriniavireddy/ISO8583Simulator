#!/usr/bin/expect;
spawn /x/web/STAGE2P1754/qatools/Simulator/StartSimulator.py;
expect "Starting to receive";
send "\r";
expect eof;
