# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

try:
    from typing import List  # noqa: F401
except ImportError:
    pass

mod = "mod4"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "o", lazy.layout.right()),

    # Move windows up or down in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    
    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("xfce4-terminal")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "d", lazy.spawn("rofi -show drun")),
    #Key([mod], "r", lazy.spawn("rofi -show run")),
    
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.Bsp(border_focus='#739fcf',border_normal='#000000',border_width=1,margin=7),
    layout.Matrix(margin=7,border_focus='#739fcf',border_normal='#000000'),
    #layout.Wmii(margin=8,border_focus='#729fcf',border_focus_stack='#000000',border_normal='#000000',border_normal_stack='#000000'),
    #layout.Floating(),
    #layout.Stack(num_stacks=2)
]

widget_defaults = dict(
    font='Ubuntu Mono derivative Powerline Regular', #'DEC Terminal Regular','IBM 3270 Narrow Medium', #'sans',
    fontsize=15,
    padding=1,
    background='000000',
    foreground='88bfff'
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.AGroupBox(border='000000',borderwidth=15,padding=3,center_aligned=True,markup=True),
                widget.TextBox("🌀",fontsize=15),
                widget.GroupBox(active='88bfff',inactive='#ffffff',fontsize=13,borderwidth=2,
                                padding=1,this_current_screen_border='88bfff',),
                widget.TextBox("[",fontsize=15,foreground='88bfff'),
                widget.TextBox("💤",fontsize=15,foreground='88bfff'),
                widget.Prompt(foreground='88bfff'),
                widget.CurrentLayout(foreground='88bfff',fontsize=16),
                widget.TextBox("]",fontsize=15,foreground='88bfff'),
                #widget.TextBox("🚦",fontsize=15,foreground='88bfff'),
                #widget.TextBox("💻",foreground='88bfff'),
                #widget.TextBox(text='♏',fontsize=15,foreground='bf2a2a'),
                widget.WindowTabs(selected=('[😃',']'),separator='🚦',fontsize=15,foreground='88bfff'),
                #widget.TextBox("default config", name="default"),
                #widget.Moc(),
                widget.TextBox("🚅",fontsize=16,foreground='eee9e9'),
                widget.Net(interface='enp0s3',foreground='88bfff'),
                widget.TextBox("🐻",fontsize=15,foreground='88bfff'),
                widget.CPUGraph(graph_color='88bfff',border_color='88bfff',border_width=1),
                #widget.MemoryGraph(graph_color='34e2e2',border_color='34e2e2',border_width=1),
                widget.TextBox("📅",fontsize=15,foreground='23e2e2'),
                widget.Clock(format='%Y-%m-%d[%a]',foreground='88bfff'),
                widget.TextBox("⏰",fontsize=15,foreground='fce94f'),
                widget.Clock(format='%I:%M:%S[%p]',foreground='88bfff'),
                widget.TextBox("💬",fontsize=15,foreground='23e2e2'),
                widget.Systray(),
            ],
            20,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = False #True 
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, github issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
