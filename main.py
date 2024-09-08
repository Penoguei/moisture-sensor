Moisture = 0

def on_forever():
    global Moisture
    Moisture = pins.analog_read_pin(AnalogReadWritePin.P1)
    if Moisture <= 300:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            """)
    else:
        if Moisture <= 600:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                . # # # .
                . . . . .
                """)
        else:
            basic.show_leds("""
                . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                """)
        basic.pause(2500)
basic.forever(on_forever)
