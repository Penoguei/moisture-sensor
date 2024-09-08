let Moisture = 0
basic.forever(function () {
    Moisture = pins.analogReadPin(AnalogReadWritePin.P1)
    if (Moisture <= 300) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    } else {
        if (Moisture <= 600) {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                . # # # .
                . . . . .
                `)
        } else {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
                `)
        }
        basic.pause(2500)
    }
})
