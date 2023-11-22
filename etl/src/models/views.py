from pydantic import BaseModel


class KafkaMessage(BaseModel):
    user_id: str
    film_id: str
    viewed_frame: int
