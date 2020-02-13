from collections import defaultdict

random = {
    "command": "add",
    "animName": "My Random Animation",
    "animType": "random",
    "colorType": "HSB",
    "animData": None,
    "palette": [
        {
            "hue": 0,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 120,
            "saturation": 100,
            "brightness": 100
        },
        {
            "hue": 240,
            "saturation": 100,
            "brightness": 100
        }
    ],
    "brightnessRange": {
        "minValue": 25,
        "maxValue": 100
    },
    "transTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "delayTime": {
        "minValue": 25,
        "maxValue": 100
    },
    "loop": True
}

def bar_effect(nl, fraction, r, g, b, w, t):
    num_panels = nl.panel_positions["numPanels"]
    pp = nl.panel_positions["positionData"]

    groups = defaultdict(list)

    for pos in pp:
        groups[pos["y"]].append(pos["panelId"])
    

    panel_groups = groups.values()
    pp_sorted = sorted(panel_groups, key=lambda k:(k["x"], k["y"]))
    panel_ids = [ panel["panelId"] for panel in pp_sorted ]
    on_panels = panel_ids[: int(fraction * len(panel_ids))]
    off_panels = [id for id in panel_ids if id not in on_panels]
    animData = [num_panels]
    num_frames = 1

    for id in off_panels:
        animData.extend([id, num_frames, 0, 0, 0, w, t])

    for id in on_panels:
        animData.extend([id, num_frames, r, g, b, w, t])


    effect = {
        "command": "display",
        "animType": "static",
        "loop": False
    }

    effect["animData"] = " ".join(map(str, animData))

    return effect


def flash_effect(nl):
    num_panels = nl.panel_positions["numPanels"]
    pp = nl.panel_positions["positionData"]
    panel_ids = [ panel["panelId"] for panel in pp ]
    animData = [num_panels]
    num_frames = 255
    for id in panel_ids:
        animData.extend([id, num_frames])
        for i in range(num_frames):
            b = 255 - int(abs(i))
            animData.extend([b, b, b, 255, 1])

    
    effect = {
        "command": "display",
        "animType": "static",
        "loop": False
    }

    effect["animData"] = " ".join(map(str, animData))
    return effect
        

def fire_effect():
    effect = {
        "command": "displayTemp",
        "duration": 3,
        "version": "2.0",
        "animName": "Fire",
        "animType": "plugin",
        "colorType": "HSB", "palette": [
            {"hue": 30, "saturation": 100, "brightness": 100, "probability": 0.0},
            {"hue": 22, "saturation": 100, "brightness": 100, "probability": 0.0},
            {"hue": 12, "saturation": 100, "brightness": 100, "probability": 0.0},
            {"hue": 19, "saturation": 100, "brightness": 74, "probability": 0.0},
            {"hue": 38, "saturation": 97, "brightness": 100, "probability": 0.0},
            {"hue": 40, "saturation": 83, "brightness": 100, "probability": 0.0},
            {"hue": 28, "saturation": 100, "brightness": 100, "probability": 0.0},
            {"hue": 16, "saturation": 100, "brightness": 100, "probability": 0.0}],
        "pluginType": "color",
        "pluginUuid": "ba632d3e-9c2b-4413-a965-510c839b3f71","pluginOptions": [
            {"name": "delayTime", "value": 0},
            {"name": "transTime", "value": 0}],
        "hasOverlay": False
    }

    return effect

