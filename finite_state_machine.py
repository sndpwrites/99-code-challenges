class AutomaticGateFSM:
    def __init__(self):
        # Define the initial state
        self.state = "Locked"
    
    # Define the transitions based on the current state and input
    def on_event(self, event):
        if self.state == "Locked":
            if event == "push_button":
                self.state = "Unlocked"
            elif event == "ring_bell":
                self.state = "Locked"
        elif self.state == "Unlocked":
            if event == "push_button":
                self.state = "Locked"
    
    # To get the current state of the FSM
    def current_state(self):
        return self.state

# Usage example
if __name__ == "__main__":
    fsm = AutomaticGateFSM()
    
    print(f"Initial State: {fsm.current_state()}")
    
    fsm.on_event("push_button")
    print(f"State after button pushed: {fsm.current_state()}")
    
    fsm.on_event("push_button")
    print(f"State after button pushed: {fsm.current_state()}")
    
    fsm.on_event("ring_bell")
    print(f"State after bell ring: {fsm.current_state()}")
