from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from submission import model, schemas
from typing import List
import json

router = APIRouter(prefix="/test", tags=["submission"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/submit")
def receive_submission(submission: schemas.SubmissionCreate, db: Session = Depends(get_db)):
    try:
        json_text = json.dumps(submission.answers, ensure_ascii=False)
        db_sub = model.Submission(section=submission.section, data=json_text)
        db.add(db_sub)
        db.commit()
        db.refresh(db_sub)
        
        return {
            "id": db_sub.id,
            "section": db_sub.section,
            "data": json.loads(db_sub.data),
            "created_at": db_sub.created_at
        }
    except Exception as e:
        db.rollback()
        print(f"❌ Ошибка сохранения: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# === GET /user/submissions ===
@router.get("/submissions")
def get_all_submissions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        submissions = db.query(model.Submission).order_by(
            model.Submission.created_at.desc()
        ).offset(skip).limit(limit).all()
        
        result = []
        for sub in submissions:
            try:
                data = {}
                if sub.data:
                    if isinstance(sub.data, str):
                        data = json.loads(sub.data)
                    else:
                        data = sub.data
                else:
                    data = {}
                    
                result.append({
                    "id": sub.id,
                    "section": sub.section,
                    "data": data,
                    "created_at": sub.created_at.isoformat() if sub.created_at else None
                })
            except Exception as e:
                print(f"⚠️ Пропущена запись {sub.id}: {e}")
                continue
        
        print(f"✅ Возвращаю {len(result)} отправок")
        return result
        
    except Exception as e:
        print(f"❌ Ошибка в get_all_submissions: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

# === GET /user/submissions/{id} ===
@router.get("/submissions/{submission_id}")
def get_submission(submission_id: int, db: Session = Depends(get_db)):
    sub = db.query(model.Submission).filter(model.Submission.id == submission_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Отправка не найдена")
    
    try:
        data = {}
        if sub.data:
            data = json.loads(sub.data) if isinstance(sub.data, str) else sub.data
        else:
            data = {}
            
        return {
            "id": sub.id,
            "section": sub.section,
            "data": data,
            "created_at": sub.created_at.isoformat() if sub.created_at else None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка парсинга: {str(e)}")

@router.delete("/submissions/{submission_id}")
def delete_submission(submission_id: int, db: Session = Depends(get_db)):
    try:
        sub = db.query(model.Submission).filter(model.Submission.id == submission_id).first()
        if not sub:
            raise HTTPException(status_code=404, detail="Отправка не найдена")
        
        db.delete(sub)
        db.commit()
        
        print(f"✅ Удалена отправка ID={submission_id}")
        return {"message": "Успешно удалено", "id": submission_id}
        
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print(f"❌ Ошибка удаления: {e}")
        raise HTTPException(status_code=500, detail=str(e))