import signal 
import time
from HardwareController import HardwareController
from screens.TransitScreen import TransitScreen
from screens.ModeScreen import ModeScreen


def SHUTDOWN_Handler(displays):
    print("=== Cleaning up Display Threads ===")
    for display in displays:
        display.DESTROY_THREAD()
    print("Shuting down & Exiting...")
    exit(0)

def main():
    
    #TODO: put this .env
    GTFS_Source = "https://drtonline.durhamregiontransit.com/gtfsrealtime/TripUpdates"


    hw_controller = HardwareController(3,2) # SCL pin 3, SDA pin 2

    display0 = hw_controller.spawnScreenAt(0)
    display1 = hw_controller.spawnScreenAt(1)
    display2 = hw_controller.spawnScreenAt(2)

    right_disp  = TransitScreen(display0, 20, GTFS_Source, "America/Toronto", "2242:1", "900")
    middle_disp =  TransitScreen(display2, 20, GTFS_Source, "America/Toronto", "2242:1", "920")
    left_disp   = ModeScreen(display1, 10, "America/Toronto")

    active_displays = [left_disp, middle_disp, right_disp]

    #* Upon Termination or Interrupt Signals, Initiate Shutdown

    signal.signal(signal.SIGTERM, lambda x, frame: SHUTDOWN_Handler(active_displays))
    signal.signal(signal.SIGINT, lambda x, frame: SHUTDOWN_Handler(active_displays))


    # Keep Lifetime of main function

    try:
        while True:
            time.sleep(1)  
    except Exception:
        pass

if __name__ == "__main__":
    main()