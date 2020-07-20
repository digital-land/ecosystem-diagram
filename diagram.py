#!/usr/bin/env python3

import sys
from math import sqrt

# ISO paper aspect ratio
page_width = 1280
page_height = 905


def header():
    print("""<?xml version="1.0" encoding="utf-8"?>""")
    print("""<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" xmlns:bx="https://boxy-svg.com" xmlns:xlink="http://www.w3.org/1999/xlink">""" % (page_width, page_height))

def footer():
    print("</svg>")

def defs():
    print("""  <defs>
    <linearGradient id="colour-users" bx:pinned="true">
      <stop style="stop-color: #FFF"/>
    </linearGradient>
    <linearGradient id="colour-services" bx:pinned="true">
      <stop style="stop-color: #e8f7f6"/>
    </linearGradient>
    <linearGradient id="colour-platforms" bx:pinned="true">
      <stop style="stop-color: #d2efee"/>
    </linearGradient>
    <linearGradient id="colour-processes" bx:pinned="true">
      <stop style="stop-color: #bce7e5"/>
    </linearGradient>
    <linearGradient id="colour-registers" bx:pinned="true">
      <stop style="stop-color: #a5e0dd"/>
    </linearGradient>
    <linearGradient id="colour-standards" bx:pinned="true">
      <stop style="stop-color: #8fd8d4"/>
    </linearGradient>

    <path id="users-path" d="M-140,375a780,475 0 1,0 1560,0a780,475 0 1,0 -1560,0"/>
    <path id="path-1" d="M-140,375a780,475 0 1,0 1560,0a780,475 0 1,0 -1560,0"/>
    <path id="path-2" d="M-140,375a780,475 0 1,0 1560,0a780,475 0 1,0 -1560,0"/>
    <path id="path-3" d="M-140,375a780,475 0 1,0 1560,0a780,475 0 1,0 -1560,0"/>

    <style type="text/css">
    #users-path {
        startOffset: 540px;
    }
""")
    print(open('weepeople.css').read())
    print("""</style></defs>""")

def grid():
    lines = 50
    step = int(page_width / lines)
    minx = 0
    maxx = page_width
    miny = -600
    maxy = page_height

    print("""  <svg id="grid">""")

    for x in range(0, maxx, step):
        print("""    <line x1="%d" x2="%d" y1="%d" y2="%d"/>""" % (page_width/2, x, miny, maxy))

    for y in range(0, maxy, step):
        print("""<line x1="%d" x2="%d" y1="%d" y2="%d"/>""" % (minx, maxx, y, y))

    print("""  </svg>""")

def layers():
    print("""  <ellipse style="fill: url(#colour-users);" cx="640" cy="375" rx="780" ry="475"/>""")
    print("""  <ellipse style="fill: url(#colour-services);" cx="640" cy="275" rx="780" ry="475"/>""")
    print("""  <ellipse style="fill: url(#colour-platforms);" cx="640" cy="75" rx="780" ry="475"/>""")
    print("""  <ellipse style="fill: url(#colour-processes);" cx="640" cy="-100" rx="780" ry="475"/>""")
    print("""  <ellipse style="fill: url(#colour-registers);" cx="640" cy="-250" rx="780" ry="475"/>""")
    print("""  <ellipse style="fill: url(#colour-standards);" cx="640" cy="-350" rx="780" ry="475"/>""")



def text():
    print("""

  <text style="font-family: Roboto; font-size: 26px; white-space: pre;" x="101.015" y="862.154">People finding information about land, planning and housing where they are already looking</text>
  <text transform="matrix(0.999971, 0.007456, -0.007456, 0.999971, -27.460264, -261.957458)" style="fill: rgb(51, 51, 51); font-family: Roboto; font-size: 26px; letter-spacing: 1px; white-space: pre;" bx:origin="0.489 0.483"><textPath startOffset="806" xlink:href="#users-path">A marketplace of digital services</textPath></text>
  <text transform="matrix(0.999971, 0.007456, -0.007456, 0.999971, -6.077383, -431.321106)" style="fill: rgb(51, 51, 51); font-family: Roboto; font-size: 26px; letter-spacing: 1px; white-space: pre;" bx:origin="0.489 0.483"><textPath startOffset="658" xlink:href="#path-1">Platforms: services which help people build digital services</textPath></text>
  <text transform="matrix(0.999971, 0.007456, -0.007456, 0.999971, 6.116228, -581.278748)" style="fill: rgb(51, 51, 51); font-family: Roboto; font-size: 26px; letter-spacing: 1px; white-space: pre;" bx:origin="0.489 0.483"><textPath startOffset="407" xlink:href="#path-2">                 Devolved land and planning services                        Other government services</textPath></text>
  <text transform="matrix(0.999971, 0.007456, -0.007456, 0.999971, -6.077364, -681.278748)" style="fill: rgb(51, 51, 51); font-family: Roboto; font-size: 26px; letter-spacing: 1px; white-space: pre;" bx:origin="0.489 0.483"><textPath startOffset="434" xlink:href="#path-3">Shared evidence Bases          Registers: authoratitve data you can trust         Monitoring information</textPath></text>
  <text x="674.855" y="180.571" style="white-space: pre; fill: rgb(51, 51, 51); font-family: &quot;Roboto Slab&quot;; font-size: 28px;"> </text>
  <text style="font-family: Roboto; font-size: 26px; white-space: pre;" x="400.008" y="46.164">Data standards, policies and regulations</text>


  <text style="font-family: Roboto; font-size: 26px; white-space: pre;" x="400.008" y="46.164">Data standards, policies and regulations</text>
  <text x="1149.047" y="706.594" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">k</text>
  <text x="1128.061" y="736.313" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">h</text>
  <text x="1087.28" y="706.594" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" bx:origin="-2.624 0.762">i</text>
  <text x="1000" y="736.313" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" bx:origin="-0.779 0.975">j</text>
  <text x="880.919" y="775" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" bx:origin="-0.988 1">d</text>
  <text x="946.794" y="824.625" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">a</text>
  <text x="741.513" y="775" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">x</text>
  <text x="1028.837" y="756.469" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">m</text>
  <text x="709.61" y="794.604" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">q</text>
  <text x="621.301" y="804.406" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">x</text>
  <text x="559.216" y="786.25" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" bx:origin="-1.254 0.395">p</text>
  <text x="426.74" y="775" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">g</text>
  <text x="392.67" y="768.264" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" bx:origin="-0.237 0.517">h</text>
  <text x="275.571" y="775" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">l</text>
  <text x="248.085" y="754.406" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">m</text>
  <text x="741.513" y="775" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;" transform="matrix(1, 0, 0, 1, -576.106531, -8.453928)">n</text>
  <text x="316.357" y="815.854" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">o</text>
  <text x="487.087" y="804.406" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">p</text>
  <text x="487.087" y="804.406" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">r</text>
  <text x="47.03" y="672.765" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">s</text>
  <text x="81.1" y="698.39" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">t</text>
  <text x="144.781" y="686.25" style="white-space: pre; fill: rgb(51, 51, 51); font-family: WeePeople; font-size: 68px;">u</text>
    """)

if __name__ == "__main__":
    header()
    defs()
    layers()
    text()
    footer()
