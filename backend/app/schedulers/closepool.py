# backend/app/services/scheduler.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import SessionLocal
from app.db.models.pool import Pool

async def close_active_pools():
    db = SessionLocal()
    try:
        # Get all active pools
        active_pools = db.query(Pool).filter(Pool.status == True).all()
        
        # Close each pool
        for pool in active_pools:
            pool.status = False
            pool.closed_at = datetime.utcnow()
        
        db.commit()
        print(f"Closed {len(active_pools)} pools at {datetime.utcnow()}")
    except Exception as e:
        print(f"Error closing pools: {e}")
    finally:
        db.close()

def init_scheduler():
    scheduler = AsyncIOScheduler()
    
    # Add job to run at midnight
    scheduler.add_job(
        close_active_pools,
        CronTrigger(hour=0, minute=0),  # Run at 00:00 every day
        id='close_pools',
        name='Close all active pools',
        replace_existing=True
    )
    
    return scheduler