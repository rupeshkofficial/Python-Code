from collections import defaultdict
from datetime import datetime, timedelta
import queue  # Import the queue module

# Initialize dictionary to hold queues for different intervals
interval_queues = defaultdict(queue.Queue)

# Function to perform dequeuing, calculation, and enqueueing
def process_trades(localTime, avg_bid_ask):
    for interval, queue in interval_queues.items():
        current_time = (datetime.strptime(localTime, '%H%M%S') + timedelta(seconds=interval)).strftime('%H%M%S')
        if localTime <= current_time:
            item = queue.get()  # Dequeue trade
            # Perform calculation
            interval_return = avg_bid_ask - item['avg_bid_ask']
            interval_queues[interval].put(interval_return)  # Enqueue return to same interval queue
            # Enqueue dequeued trade to next intervals queues
            for next_interval in interval_queues.keys():
                if next_interval > interval:
                    interval_queues[next_interval].put(item)

# Enqueue the trade event
if should_print:
    mainQueue.put({
        'localTime': localTime,
        'exchange_symbol': exchange_symbol,
        'bid': instrument.bid,
        'ask': instrument.ask,
        'avg_bid_ask': avg_bid_ask
    })

    # Process trades for different intervals
    process_trades(localTime, avg_bid_ask)

    # Print the contents of the mainQueue
    item = mainQueue.get()
    print(f"{item['localTime']},{item['exchange_symbol']},{item['bid']},{item['ask']},{item['avg_bid_ask']}", end=',')

    # Print returns for different intervals
    return_values = []
    for interval, queue in interval_queues.items():
        return_values.append(str(queue.get()))
    print(','.join(return_values))
