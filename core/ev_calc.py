#coding:utf-8
import math

def luminance_to_ev(luminance, iso=100):
    """
    将平均光度转换成曝光值 (EV).
    Convert average luminance to EV.
    公式: EV = log2((Luminance * 100) / ISO)
    """
    if luminance <= 0:
        return 0
    ev = math.log2((luminance * 100) / iso)
    return round(ev, 2)