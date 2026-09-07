# Defines a new class named EventDispatcher that will manage subscriptions and trigger events.
class EventDispatcher:

    def __init__(self):
        # Dictionary storing event types and their callbacks
        self.events = {}

    # Defines a method to register a function (callback) to a specific event name (event_type).
    def subscribe(self, event_type: str, callback: callable):
        """Register a callback for an event."""
        if event_type not in self.events:
            self.events[event_type] = []

        self.events[event_type].append(callback)

    # Defines a method to remove a previously registered callback function from an event.
    def unsubscribe(self, event_type: str, callback: callable):
        """Remove a registered callback."""
        if event_type in self.events:
            if callback in self.events[event_type]:
                self.events[event_type].remove(callback)

    def dispatch(self, event_type: str, *args, **kwargs):
        """Execute all callbacks registered for an event."""
        if event_type not in self.events:
            return

        # Use a copy so callbacks can safely modify subscriptions
        for callback in self.events[event_type][:]:
            try:
                callback(*args, **kwargs)
            except Exception as error:
                print(f"Error in callback {callback.__name__}: {error}")

# -------------------------
# Example Usage
# -------------------------

# Instantiates a new EventDispatcher object.
dispatcher = EventDispatcher()

# Defines three simple listener functions that accept a user_id parameter.
def on_user_created(user_id):
    print(f"User created: {user_id}")


def send_email(user_id):
    print(f"Sending welcome email to user {user_id}")


def update_database(user_id):
    print(f"Updating database for user {user_id}")


# Subscribe callbacks
dispatcher.subscribe("user_created", on_user_created)
dispatcher.subscribe("user_created", send_email)
dispatcher.subscribe("user_created", update_database)

# Dispatch event
dispatcher.dispatch("user_created", 101)
