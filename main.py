
basic.show_number(0)
def on_gesture_shake():
    pass
input.on_gesture(Gesture.Shake, on_gesture_shake)
hummingbird.set_led(ThreePort.ONE)
hummingbird.set_tri_led(TwoPort.ONE)