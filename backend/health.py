from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware


from db import engine, Base, get_db





@app.get("/health/db")
def check_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "db_response": result.scalar(),
            "database": str(engine.url),  # покажет куда реально подключились
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

