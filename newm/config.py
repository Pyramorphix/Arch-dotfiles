from __future__ import annotations
from typing import Callable, Any

import os
import pwd
import time
import logging

from newm.layout import Layout
from newm.helper import BacklightManager, WobRunner, PaCtl

from pywm.pywm import (
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT
)

logger = logging.getLogger(__name__)

corner_radius = 14 
anim_time = .15

view = {
    'corner_radius': 12,
    'ssd': {
        'enabled': False
    }
}

background = {
    'path': '/home/pyramorphix/wallpapers/2.jpg',
    'anim': True,
}

outputs = [
    { 'name': 'eDP-1' },
    { 'name': 'virt-1', 'pos_x': -1920, 'pos_y': 0, 'width': 1920, 'height': 1080 }
]

focus = {
    'enabled': True,
    'color': '#772a4c',
    'distance': 1,
    'width': 5,
    'animate_on_change': False,
}
wob_runner = WobRunner("wob -a bottom -M 100")
backlight_manager = BacklightManager(anim_time=1., bar_display=wob_runner)
kbdlight_manager = BacklightManager(args="--device='*::kbd_backlight'", anim_time=1., bar_display=wob_runner)
def synchronous_update() -> None:
    backlight_manager.update()
    kbdlight_manager.update()

pactl = PaCtl(0, wob_runner)

def key_bindings(layout: Layout) -> list[tuple[str, Callable[[], Any]]]:
    return [
        ("L-h", lambda: layout.move(-1, 0)),
        ("L-j", lambda: layout.move(0, 1)),
        ("L-k", lambda: layout.move(0, -1)),
        ("L-l", lambda: layout.move(1, 0)),
        ("L-u", lambda: layout.basic_scale(1)),
        ("L-n", lambda: layout.basic_scale(-1)),
        # ("L-t", lambda: layout.move_in_stack(1)),

        ("L-H", lambda: layout.move_focused_view(-1, 0)),
        ("L-J", lambda: layout.move_focused_view(0, 1)),
        ("L-K", lambda: layout.move_focused_view(0, -1)),
        ("L-L", lambda: layout.move_focused_view(1, 0)),

        ("L-C-h", lambda: layout.resize_focused_view(-1, 0)),
        ("L-C-j", lambda: layout.resize_focused_view(0, 1)),
        ("L-C-k", lambda: layout.resize_focused_view(0, -1)),
        ("L-C-l", lambda: layout.resize_focused_view(1, 0)),

        # Keybindings for opening apps
        ("L-Return", lambda: os.system("alacritty &")),
        ("L-c", lambda: os.system("firefox &")),
        ("L-t", lambda: os.system("telegram-desktop &")),

        ("L-q", lambda: layout.close_focused_view()),

        ("L-l", lambda: layout.ensure_locked(dim=True)),
        ("L-M", lambda: layout.terminate()),
        ("L-C", lambda: layout.update_config()),

        ("L-f", lambda: layout.toggle_fullscreen()),

        ("L-", lambda: layout.toggle_overview()),

        ("L-S", lambda: os.system("grim -g \"$(slurp)\" - | swappy -f - &")),
        ("L-C-o", lambda: os.system("obsidian --ozone-platform=wayland --enable-features=UseOzonePlatform &")),

        ("XF86MonBrightnessUp", lambda: backlight_manager.set(backlight_manager.get() + 0.1)),
        ("XF86MonBrightnessDown", lambda: backlight_manager.set(backlight_manager.get() - 0.1)),
        ("XF86KbdBrightnessUp", lambda: kbdlight_manager.set(kbdlight_manager.get() + 0.1)),
        ("XF86KbdBrightnessDown", lambda: kbdlight_manager.set(kbdlight_manager.get() - 0.1)),
        ("XF86AudioRaiseVolume", lambda: pactl.volume_adj(5)),
        ("XF86AudioLowerVolume", lambda: pactl.volume_adj(-5)),
        ("XF86AudioMute", lambda: pactl.mute()),
    ]

panels = {
    'lock': {
        'cmd': 'alacritty -e newm-panel-basic lock',
    },
    'launcher': {
        'cmd': 'alacritty -e newm-panel-basic launcher'
    },
    'bar': {
        'cmd': "waybar",
        'visible_normal': False
    },
    'top_bar': {
        'native': {
            'enabled': False,
        }
    },
    'bottom_bar': {
        'native': {
            'enabled': False,
        }
    },
}

energy = {
    'idle_callback': backlight_manager.callback
}

pywm = {
    'xkb_layout' : "us, ru",
    'xkb_options' : "grp:rctrl_toggle, lv3:caps_switch",
    'xcursor_theme' : 'GoogleDot-Black',
    'xcursor_size' : 14
}
