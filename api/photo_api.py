from fastapi import APIRouter, UploadFile, File
import random
from database.postservice import add_photo_post_db
from schemas import PhotoPostSchema

photo_router = APIRouter(prefix="/photo", tags=["Photo API"])


@photo_router.post("/add_photo")
async def add_photo_api(pid: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1_000_000)
    if photo_file:
        try:
            with open(f"database/images/photo_{file_id}_{pid}.jpg", "wb") as photo:
                photo_to_save = await photo_file.read()
                photo.write(photo_to_save)

                photo_schema = PhotoPostSchema(
                photo_path=photo.name,
                pid=pid
                )

                result = add_photo_post_db(photo_schema)
                if result:
                    return {"status": 1, "message": result}
                return {"status": 0, "message": False}
        except Exception as e:
            return {"status": 0, "message": False}

