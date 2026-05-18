import json
import logging
from typing import Any, Callable

import pika
from pika.exceptions import AMQPConnectionError

from app.core.config import settings

logger = logging.getLogger(__name__)


class RabbitMQQueue:
    """Thin RabbitMQ adapter for publishing and consuming summary jobs."""

    def __init__(self, url: str = settings.RABBITMQ_URL, queue_name: str = settings.SUMMARY_QUEUE_NAME):
        self._url = url
        self._queue_name = queue_name

    def publish(self, payload: dict[str, Any]) -> None:
        connection = pika.BlockingConnection(pika.URLParameters(self._url))
        try:
            channel = connection.channel()
            channel.queue_declare(queue=self._queue_name, durable=True)
            channel.basic_publish(
                exchange="",
                routing_key=self._queue_name,
                body=json.dumps(payload).encode("utf-8"),
                properties=pika.BasicProperties(delivery_mode=2),
            )
        finally:
            connection.close()

    def consume(self, on_message: Callable[[dict[str, Any]], None]) -> None:
        connection = pika.BlockingConnection(pika.URLParameters(self._url))
        channel = connection.channel()
        channel.queue_declare(queue=self._queue_name, durable=True)
        channel.basic_qos(prefetch_count=1)

        def _handler(ch: pika.adapters.blocking_connection.BlockingChannel, method, _properties, body: bytes) -> None:
            try:
                payload = json.loads(body.decode("utf-8"))
                on_message(payload)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception:
                logger.exception("Error handling queue message")
                ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

        channel.basic_consume(queue=self._queue_name, on_message_callback=_handler)
        logger.info("Waiting for messages in queue %s", self._queue_name)
        channel.start_consuming()


def wait_for_rabbitmq(max_attempts: int = 60, delay_seconds: int = 2) -> None:
    """Block until RabbitMQ is reachable to avoid crashing on startup races."""
    import time

    for attempt in range(1, max_attempts + 1):
        try:
            connection = pika.BlockingConnection(pika.URLParameters(settings.RABBITMQ_URL))
            connection.close()
            logger.info("Connected to RabbitMQ")
            return
        except AMQPConnectionError:
            logger.warning(
                "RabbitMQ not ready yet (attempt %d/%d)",
                attempt,
                max_attempts,
            )
            time.sleep(delay_seconds)

    raise RuntimeError("RabbitMQ did not become available in time")
