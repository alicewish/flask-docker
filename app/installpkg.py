# -*- coding: utf-8 -*-
import platform
import re
import subprocess
import sys
import time

import pkg_resources

do_not_upgrade = {'pip', }

library_STRING = '''
pyperclip
arrow
beautifulsoup4
Chronyk
clipboard
copyheaders
html2text
html5print
jieba
json2yaml
markdown
markdown2
markdownify
mistune
pep8
Pillow
Pygments
pyinstaller
python-pushover
python-wordpress-xmlrpc
pyyaml
qiniu
rarfile
requests
requests-html

selenium
shadowsocks
stagger
tomd
torrentool
transmissionrpc
tweepy
you-get
youtube-dl
zhihu_oauth
basc-py4chan
pysrt
webvtt-py
python-frontmatter
pypandoc

pypinyin
pyecharts
echarts-python
json2yaml
bencode-python3
bencoder
bendercoder
wxPython
regex
langdetect
xmltodict
untangle
xmljson
pygeoip
appjar

pytesseract
imutils
opencv-contrib-python
tensorflow
h5py
keras
ImageAI

pyzbar
pydot

psd-tools2

pygame

wand

tifffile
tiffreader
libtiff
imageio



torrent_parser

js2py

Django
Flask

ahk

pyscreeze
pymsgbox
pytweening
pygetwindow
pyautogui

webcolors

autopy

wagtail
autocorrect

cfscrape
dicttoxml

uWSGI
redis
gunicorn
pymysql

alembic
bleach
blinker
click
dominate
Flask
Flask-Bootstrap
Flask-HTTPAuth
Flask-Login
Flask-Mail
Flask-Migrate
Flask-Moment
Flask-PageDown
Flask-SQLAlchemy
Flask-WTF
html5lib
itsdangerous
Jinja2
Mako
Markdown
MarkupSafe
python-dateutil
python-dotenv
python-editor
six
SQLAlchemy
visitor
webencodings
Werkzeug
WTForms

'''


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
        # print(i + 1, dist_name, dist_version)

    dist_names = [tup[0] for tup in info_list]
    dist_name_slugs = [filename2permalink(dist_name).lower() for dist_name in dist_names]
    return dist_names, dist_name_slugs, info_list


def upgrade_library(info_list):  # 更新
    for i in range(len(info_list)):
        tup = info_list[i]
        dist_name, dist_version = tup

        print(str(i + 1) + '/' + str(len(info_list)))
        print(dist_name, '/', dist_version)

        command = command_PREFIX + ' ' + dist_name

        if dist_name.lower() not in do_not_upgrade:
            print(command)
            subprocess.call(command, shell=True)
            print('================完成================')


def install_library(libraries):  # 安装

    for i in range(len(libraries)):
        library = libraries[i]
        print(str(i + 1) + '/' + str(len(libraries)), library)

        command = command_PREFIX + library

        print(command)
        subprocess.call(command, shell=True)
        print('================完成================')


if __name__ == '__main__':
    start_time = time.time()  # 初始时间戳

    os_info = get_platform()
    python_ver = platform.python_version()

    print(os_info)
    print(python_ver)

    dist_names, dist_name_slugs, info_list = get_dists()

    raw_libraries = [line.strip() for line in library_STRING.splitlines() if line.strip() != '']

    command_PREFIX = "pip3 install --upgrade "

    raw_libraries.sort()

    libraries = [library for library in raw_libraries if filename2permalink(library).lower() not in dist_name_slugs]

    install_library(libraries)
    upgrade_library(info_list)

    # ================运行时间计时================
    print(run_time(start_time))
    print(current_time())
