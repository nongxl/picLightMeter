#coding:utf-8
import math

def compute_aperture(ev, iso=100, shutter=1/60):
    """
    快门优先模式S，通过曝光值（EV）和给定的iso、快门速度计算出光圈值
    Compute aperture (f-number) given EV, ISO and shutter speed.
    公式: N = sqrt((ISO * t * 2^EV) / 100)
    """
    ev_corrected = ev - math.log2(iso / 100)
    f_number = math.sqrt((2 ** ev_corrected) * shutter)
    return round(f_number, 2)

def compute_shutter_speed(ev, iso=100, aperture=2.8):
    """
    光圈优先模式A，通过曝光值（EV）和给定的iso、光圈计算出快门速度
    Compute shutter speed given EV, ISO and aperture.
    公式: t = (100 * N^2) / (ISO * 2^EV)
    """
    ev_corrected = ev - math.log2(iso / 100)
    t = (aperture ** 2) / (2 ** ev_corrected)
    return round(t, 4)

def simulate_aperture_priority(ev, iso=100, aperture=2.8):
    shutter = compute_shutter_speed(ev, iso, aperture)
    return f"A模式：设定光圈 f/{aperture}，推荐快门速度：1/{round(1/shutter)} 秒"

def simulate_shutter_priority(ev, iso=100, shutter=1/125):
    aperture = compute_aperture(ev, iso, shutter)
    return f"S模式：设定快门 1/{int(1/shutter)} 秒，推荐光圈：f/{aperture}"
