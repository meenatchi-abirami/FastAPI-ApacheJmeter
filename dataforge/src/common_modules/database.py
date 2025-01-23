from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy import MetaData

class DatabaseManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self.database_url = "mysql+aiomysql://root:ABiee99#@localhost/Power_data"  
        self.engine = create_async_engine(
            self.database_url,
            pool_size=10,
            max_overflow=5,
            pool_timeout=30,
            pool_recycle=1800,
            poolclass=AsyncAdaptedQueuePool,
            echo=False,  
        )
        self.session_local = sessionmaker(
            bind=self.engine, class_=AsyncSession, expire_on_commit=False
        )
        self.metadata = MetaData()

    async def get_db(self):
        async with self.session_local() as session:
            try:
                yield session
            finally:
                await session.close()
