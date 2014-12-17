# i3timer

This is a very simple timer.

# Installation
```bash
sudo python3 setup.py install
```

# Configuration

## i3pystatus
```python
import i3timer.i3pystatus_module

status.register(i3timer.i3pystatus_module.TimerModule,
        interval=1,
        missing_color='#ff0000',
        running_color='#00fff00',
        paused_color='#888888',
    )
```

## i3 config

A typical bindings would be similar to these:

```
exec_always --no-startup-id i3timer --daemon

bindsym Shift+Pause exec --no-startup-id "i3timer --toggle"
bindsym $mod+Shift+Pause exec --no-startup-id "i3timer --stop"
```

