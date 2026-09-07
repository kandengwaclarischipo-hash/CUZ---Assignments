import time
import functools
import threading

def rate_limit(max_calls: int, period: float):
    def decorator(func):
        # Closure-level lock to ensure thread safety during state checks
        lock = threading.Lock()
        calls = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls
            now = time.time()
            
            with lock:
                # Remove timestamps older than the period window
                calls = [t for t in calls if now - t < period]
                
                if len(calls) >= max_calls:
                    raise Exception("Rate limit exceeded")
                
                calls.append(now)
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage Example
@rate_limit(max_calls=3, period=10)
def fetch_user_data(user_id):
    return f"Data for {user_id}"