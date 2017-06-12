#!/usr/bin/python
# coding = utf-8

from JubiAPI import JuBiSpot

JubiURL = "www.jubi.com"

jubiSpot = JuBiSpot(JubiURL)

print(jubiSpot.ticker("btc"))

print(jubiSpot.depth("btc"))

print(jubiSpot.orders("btc"))

