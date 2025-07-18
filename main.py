from core.image_analyzer import calculate_center_luminance, is_exposure_valid, plot_histogram
from core.ev_calc import luminance_to_ev
from utils.exposure_model import simulate_aperture_priority, simulate_shutter_priority

def run_lightmeter(image_path, iso, mode='A', aperture=2.8, shutter=1/125,histogram=''):
    valid, status = is_exposure_valid(image_path)
    print(f"曝光分析结果：{status}")
    if histogram == 'y':
        plot_histogram(image_path)#如需保存为文件而非显示，也可改为 plt.savefig()
    if not valid:
        return

    lum = calculate_center_luminance(image_path)
    ev = luminance_to_ev(lum, iso=iso)
    print(f"中心区域平均亮度: {lum:.2f}")
    print(f"估算 EV 值（ISO {iso}）: {ev}")

    if mode == 'A':
        print(simulate_aperture_priority(ev, iso=iso, aperture=aperture))
    elif mode == 'S':
        print(simulate_shutter_priority(ev, iso=iso, shutter=shutter))

if __name__ == '__main__':
    # 示例调用
    run_lightmeter('data/dark.JPG', iso=400, mode='A', aperture=1.4, histogram='y')
    run_lightmeter('data/dark.JPG', iso=400, mode='S', shutter=1/8, histogram='y')