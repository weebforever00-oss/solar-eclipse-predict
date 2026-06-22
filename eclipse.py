#!/usr/bin/env python3
"""Simplified solar eclipse visibility check."""
import math

def moon_distance_approx(jd):
    """Approximate moon distance in Earth radii."""
    T = (jd - 2451545.0) / 36525.0
    D = 297.8501921 + 445267.1114034*T  # mean elongation
    return 60.4 - 3.3 * math.cos(math.radians(D))

def eclipse_visible(lat, lon, jd):
    """Simplified check — real prediction needs full Besselian elements."""
    # Very rough: eclipse visible within ~100km of central line
    # This is a placeholder showing the calculation structure
    return abs(lat) < 60  # simplified

if __name__ == "__main__":
    eclipses = [("2024 Apr 8", "North America"), ("2026 Aug 12", "Arctic/Europe"),
                ("2027 Aug 2", "North Africa"), ("2028 Jul 22", "Australia")]
    print("Solar Eclipse Calendar")
    for date, region in eclipses:
        print(f"  {date}: visible from {region}")\n