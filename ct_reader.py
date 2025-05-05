import time
import numpy as np
from mcc118 import MCC118
import threading
from queue import Queue
import datetime

class CTReader:
    def __init__(self, sample_rate=5000, buffer_size=1000):
        self.sample_rate = sample_rate
        self.buffer_size = buffer_size
        self.data_queue = Queue()
        self.running = False
        self.mcc = MCC118()
        self.channel = 0  # Channel 1 (0-based index)
        
    def start(self):
        """Start the data acquisition thread"""
        self.running = True
        self.acquisition_thread = threading.Thread(target=self._acquire_data)
        self.acquisition_thread.start()
        
    def stop(self):
        """Stop the data acquisition"""
        self.running = False
        if hasattr(self, 'acquisition_thread'):
            self.acquisition_thread.join()
            
    def _acquire_data(self):
        """Main data acquisition loop"""
        while self.running:
            # Read a batch of samples
            samples = []
            timestamps = []
            
            for _ in range(self.buffer_size):
                if not self.running:
                    break
                    
                # Read voltage from MCC118
                voltage = self.mcc.a_in_read(self.channel)
                timestamp = datetime.datetime.now()
                
                samples.append(voltage)
                timestamps.append(timestamp)
                
                # Calculate sleep time to maintain desired sample rate
                time.sleep(1.0 / self.sample_rate)
            
            if samples:
                # Put the batch of data in the queue
                self.data_queue.put({
                    'timestamps': timestamps,
                    'voltages': samples
                })
                
    def get_data(self):
        """Get the latest batch of data from the queue"""
        if not self.data_queue.empty():
            return self.data_queue.get()
        return None

if __name__ == "__main__":
    # Test the CT reader
    reader = CTReader()
    reader.start()
    
    try:
        while True:
            data = reader.get_data()
            if data:
                print(f"Received {len(data['voltages'])} samples")
            time.sleep(0.1)
    except KeyboardInterrupt:
        reader.stop()
        print("Stopped data acquisition") 