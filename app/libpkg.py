import platform
import re
import sys
import time

import pkg_resources


def get_platform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


def filename2permalink(title):
    permalink = title.replace('+', ' ').replace('%', ' ').replace('(', ' ').replace(')', ' ').replace("'", '').replace(
        "?", '')
    permalink = permalink.replace(' - ', ' ')
    permalink = re.sub(r'[+()\'\[\],.&!@#$%^*_=:]', ' ', permalink)
    permalink = re.sub(r'\bAnd\b|\bThe\b|\bOngoing\b', ' ', permalink, flags=re.I)
    permalink = permalink.replace(' ', '-').replace('.', '-')
    permalink = re.sub(r'[-]{2,}', '-', permalink)
    permalink = permalink.strip('-')
    return permalink


# ================运行时间计时================
def run_time(start_time):
    run_time = time.time() - start_time
    if run_time < 60:  # 两位小数的秒
        show_run_time = "{:.2f}秒".format(run_time)
    elif run_time < 3600:  # 分秒取整
        show_run_time = "{:.0f}分{:.0f}秒".format(run_time // 60, run_time % 60)
    else:  # 时分秒取整
        show_run_time = "{:.0f}时{:.0f}分{:.0f}秒".format(run_time // 3600, run_time % 3600 // 60, run_time % 60)
    return show_run_time


# ================当前时间================
def current_time():
    now_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 当前日期戳
    return now_time_str


def get_dists():
    dists = [d for d in pkg_resources.working_set]
    dists.sort(key=lambda x: x.project_name)
    info_list = []
    for i in range(len(dists)):
        dist_info = dists[i]
        dist_name = dist_info.project_name
        try:
            dist_version = dist_info.version
        except:
            dist_version = ''
        tup = (dist_name, dist_version)
        info_list.append(tup)
        print(i + 1, dist_name, dist_version)

    dist_names = [tup[0] for tup in info_list]
    dist_name_slugs = [filename2permalink(dist_name).lower() for dist_name in dist_names]
    return dist_names, dist_name_slugs, info_list


if __name__ == '__main__':
    start_time = time.time()  # 初始时间戳

    target_dir = ''

    os_info = get_platform()
    python_ver = platform.python_version()

    print(os_info)
    print(python_ver)

    dist_names, dist_name_slugs, info_list = get_dists()

    # ================运行时间计时================
    print(run_time(start_time))
    print(current_time())
