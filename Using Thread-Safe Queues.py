# thread_safe_queues.py
#queue.Queue
def main(args):
    buffer = QUEUE_TYPES[args.queue]()
    producers = [
        Producer(args.producer_speed, buffer, PRODUCTS)
        for _ in range(args.producers)
    ]
    consumers = [
        Consumer(args.consumer_speed, buffer) for _ in range(args.consumers)
    ]

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()

    #queue.PriorityQueue

    from dataclasses import dataclass, field
    from enum import IntEnum

    # ...

    @dataclass(order=True)
    class Product:
        priority: int
        label: str = field(compare=False)

        def __str__(self):
            return self.label

    class Priority(IntEnum):
        HIGH = 1
        MEDIUM = 2
        LOW = 3

    PRIORITIZED_PRODUCTS = (
        Product(Priority.HIGH, ":1st_place_medal:"),
        Product(Priority.MEDIUM, ":2nd_place_medal:"),
        Product(Priority.LOW, ":3rd_place_medal:"),
    )

    def main(args):
        buffer = QUEUE_TYPES[args.queue]()
        products = PRIORITIZED_PRODUCTS if args.queue == "heap" else PRODUCTS
        producers = [
            Producer(args.producer_speed, buffer, products)
            for _ in range(args.producers)
        ]

